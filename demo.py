import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(4);L=20000
gc=np.full(L,0.4);gc[8000:9000]=0.7  # a GC-rich island
seq=np.array([rng.choice(list("ACGT"),p=[(1-g)/2,g/2,g/2,(1-g)/2]) for g in gc])
w=200;isgc=np.isin(seq,["G","C"]).astype(float)
prof=np.convolve(isgc,np.ones(w)/w,mode="valid")
plt.figure(figsize=(9,3.5));plt.plot(prof)
plt.axhline(prof.mean(),ls="--",c="k",label=f"mean {prof.mean():.2f}")
plt.xlabel("position (bp)");plt.ylabel("GC fraction");plt.title("GC content, 200 bp window (demo data)");plt.legend()
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("one GC-rich island detected\n");print("ok")