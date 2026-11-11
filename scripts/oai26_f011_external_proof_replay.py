#!/usr/bin/env python3
"""Exact-pinned independent Erdos 821 Lean replay for GCL's owned Colab supervisor."""
import argparse, datetime, hashlib, json, os, pathlib, shutil, subprocess, sys, tempfile, time

UPSTREAM = "https://github.com/cadamcat/totient-fibers-lean4.git"
REV = "f75d4f2c2d6685a0547f17fa07240377aa2c2ed4"
MANIFEST = "8df0747916e81c4d13f3ed226a6ffa5dd04760ffc13668241d603a3595c634cf"
MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
TOOLCHAIN = "leanprover/lean4:v4.34.1"

def digest(b): return hashlib.sha256(b).hexdigest()
def write(path,obj):
    raw=(json.dumps(obj,sort_keys=True,indent=2)+"\n").encode()
    fd,name=tempfile.mkstemp(prefix=path.name+".",dir=path.parent)
    with os.fdopen(fd,"wb") as f:
        f.write(raw);f.flush();os.fsync(f.fileno())
    os.replace(name,path)

def execute(label,cmd,cwd,env,limit=9000,mandatory=True):
    print("COMMAND",label,cmd,flush=True)
    with (OUT/(label+".log")).open("ab") as log:
        log.write(("BEGIN "+datetime.datetime.now(datetime.timezone.utc).isoformat()+" "+json.dumps(cmd)+"\n").encode())
        log.flush()
        try:
            r=subprocess.run(cmd,cwd=cwd,env=env,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,timeout=limit)
            status=r.returncode
        except subprocess.TimeoutExpired:
            status=124
        log.write(("EXIT "+str(status)+" "+datetime.datetime.now(datetime.timezone.utc).isoformat()+"\n").encode())
        log.flush();os.fsync(log.fileno())
    print("EXIT",label,status,flush=True)
    if status!=0 and mandatory:raise RuntimeError(label+" exit="+str(status))
    return status

def check_pins(root,env):
    got=subprocess.check_output(["git","rev-parse","HEAD"],cwd=root,text=True,env=env).strip()
    if got!=REV:raise RuntimeError("HEAD_MISMATCH "+got)
    raw=(root/"lake-manifest.json").read_bytes()
    got=digest(raw)
    if got!=MANIFEST:raise RuntimeError("MANIFEST_MISMATCH "+got)
    return {"head":got,"manifest_sha256":MANIFEST}

def checkpoint(step,detail):
    record={"record_type":"GCL_GPU_CHECKPOINT_SOURCE/1","job_id":args.job_id,"source_sha256":args.source_sha256,
      "step":step,"source_commit":REV,"lake_manifest_sha256":MANIFEST,"detail":detail}
    raw=(json.dumps(record,sort_keys=True)+"\n").encode()
    (OUT/"checkpoint.pt").write_bytes(raw)
    write(OUT/"checkpoint.json",{"record_type":"GCL_GPU_CHECKPOINT/1","job_id":args.job_id,
      "source_sha256":args.source_sha256,"step":step,"sha256":digest(raw)})
    print("CHECKPOINT",step,flush=True)

a=argparse.ArgumentParser()
for x in ("job-id","source-sha256","out"):a.add_argument("--"+x,required=True)
a.add_argument("--steps",required=True,type=int)
a.add_argument("--resume")
args=a.parse_args()
OUT=pathlib.Path(args.out);OUT.mkdir(parents=True,exist_ok=True)
ROOT=OUT/"src"
ENV=dict(os.environ)
ENV["PATH"]=str(pathlib.Path.home()/".elan/bin")+":"+ENV.get("PATH","")
ENV["LEAN_NUM_THREADS"]="4"
ENV["GIT_TERMINAL_PROMPT"]="0"
if args.steps!=4:raise RuntimeError("EXACT_STEP_COUNT_REQUIRED_4")
start=0
if args.resume:
    x=json.loads(pathlib.Path(args.resume).read_text())
    if x.get("job_id")!=args.job_id or x.get("source_sha256")!=args.source_sha256:raise RuntimeError("BAD_CHECKPOINT")
    start=x["step"]
print("GCL_OAI26_F011_CLOUD_REPLAY_START",args.job_id,"start",start,flush=True)
try:
    if start<1:
        if not shutil.which("git"):raise RuntimeError("GIT_UNAVAILABLE")
        if not shutil.which("curl"):raise RuntimeError("CURL_UNAVAILABLE")
        if not (pathlib.Path.home()/".elan/bin/lake").exists():
            execute("elan_install",["bash","-c","curl -fsSL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --no-modify-path"],OUT,ENV,600)
        execute("toolchain",["elan","toolchain","install",TOOLCHAIN],OUT,ENV,1200)
        if not ROOT.exists():
            execute("clone",["git","clone","--filter=blob:none",UPSTREAM,str(ROOT)],OUT,ENV,900)
        execute("checkout",["git","checkout","--detach",REV],ROOT,ENV,600)
        check_pins(ROOT,ENV)
        checkpoint(1,{"source":"exact head and manifest","toolchain":TOOLCHAIN})
    if start<2:
        lake_rc=execute("lake_update",["lake","update"],ROOT,ENV,3600,mandatory=False)
        check_pins(ROOT,ENV)
        if lake_rc!=0:
            # The pinned upstream repository explicitly documents this exact
            # OAI post-update guard after the manifest has been written.
            # No other error or revision drift is admissible.
            errors=[line.strip() for line in (OUT/"lake_update.log").read_text(errors="replace").splitlines()
                    if line.strip().startswith("error: ")]
            expected=f"error: iut: Lake resolved an unexpected checkout at {ROOT/'.lake/packages/iut'}."
            if lake_rc!=1 or errors!=[expected]:
                raise RuntimeError(f"UNEXPECTED_LAKE_UPDATE_FAILURE exit={lake_rc} errors={errors!r}")
            for package,revision in (
                ("OAI","adc7f1241b42e322a6451854ab7e4b4c146bf78a"),
                ("iut","d9465c111ec4073709f67e9fccec7e3eb374a816"),
                ("mathlib",MATHLIB)):
                actual=subprocess.check_output(["git","-C",str(ROOT/".lake/packages"/package),"rev-parse","HEAD"],env=ENV,text=True).strip()
                if actual!=revision:
                    raise RuntimeError("PINNED_POSTUPDATE_REVISION_DRIFT "+package+" "+actual)
            print("DOCUMENTED_OAI_POSTUPDATE_GUARD_ACCEPTED_WITH_EXACT_PINS",flush=True)
        execute("apply_patches",["bash","scripts/apply-oai-patches.sh"],ROOT,ENV,1000)
        cache_status=execute("cache_get",["lake","exe","cache","get"],ROOT,ENV,4800,mandatory=False)
        checkpoint(2,{"dependencies":"pinned","cache_exit":cache_status,"mathlib_expected":MATHLIB})
    if start<3:
        check_pins(ROOT,ENV)
        execute("build",["lake","build","Erdos821","Challenge","Verification"],ROOT,ENV,16000)
        checkpoint(3,{"build":"success","source":REV})
    if start<4:
        check_pins(ROOT,ENV)
        execute("verify",["bash","scripts/verify.sh"],ROOT,ENV,5400)
        execute("leanchecker",["lake","env","leanchecker","--fresh","Erdos821.Theorem"],ROOT,ENV,3600)
        if not all((OUT/f).is_file() for f in ("build.log","verify.log","leanchecker.log")):
            raise RuntimeError("MISSING_CRITICAL_LOG")
        evidence={"theorem":"Erdos821.erdos_821","source_head":REV,
            "manifest_sha256":MANIFEST,
            "build_sha256":digest((OUT/"build.log").read_bytes()),
            "verify_sha256":digest((OUT/"verify.log").read_bytes()),
            "leanchecker_sha256":digest((OUT/"leanchecker.log").read_bytes())}
        write(OUT/"scientific_evidence.json",evidence)
        checkpoint(4,evidence)
        write(OUT/"result.json",{"record_type":"GCL_GPU_RESULT/1","job_id":args.job_id,
            "source_sha256":args.source_sha256,"step":4,"completed":True,"evidence":evidence})
        print("GCL_F011_CLOUD_REPLAY_SUCCESS",flush=True)
except BaseException as ex:
    write(OUT/"failure.json",{"record_type":"GCL_GPU_FAILURE/1","job_id":args.job_id,
       "source_sha256":args.source_sha256,"last_checkpoint_step":start,
       "reason":str(ex),"time":datetime.datetime.now(datetime.timezone.utc).isoformat()})
    print("GCL_F011_CLOUD_REPLAY_FAILURE",type(ex).__name__,str(ex),flush=True)
    raise

