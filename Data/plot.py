import os,sys
import numpy as np
import matplotlib.pyplot as plt

Rp = []
Rp.append("./L4")
Rp.append("./L6")
Rp.append("./L8")

Data = []
for f in Rp:
    Data.append(np.loadtxt(os.path.join(f,"result")))



for i in range(len(Data)):
    plt.plot(Data[i][:,1],Data[i][:,5]-Data[i][:,3],'o',label="L%d"%(int(Data[i][0,2])))
    
plt.xlabel("Hx")
plt.ylim(bottom=0)
plt.ylabel(r"$\Delta E_{20}$")
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig("Egap.png",format="png",dpi=300)
plt.show()

