import sys,os
import cytnx
import numpy as np

if len(sys.argv[1]) < 2:
    print("python analysis.py <Dir>")
    exit(1)

Dir = sys.argv[1]

A = [os.path.join(sys.argv[1],x) for x in os.listdir(sys.argv[1]) if 'cytn' in x]
A = np.sort(A)

Data = []
param = []
for i in A:
    fn = i.strip().split("/")[-1]
    fn = fn.replace(".e.cytn","")
    fn = fn.split("_")
    param.append(np.array([float(fn[0].split('s')[-1]), float(fn[1].split("L")[-1])]))
    tmp = cytnx.Tensor.Load(i)
    Data.append(tmp.numpy())

Data = np.array(Data)
Data = np.hstack([param,Data])
np.savetxt(os.path.join(sys.argv[1],"result"),Data)




