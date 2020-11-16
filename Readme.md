# Exact diagonalization using Laczos method

This is the simple example for using cytnx with ED to calculate 1D Transverse field ising model:

H = -[s]SzSz - (1-[s])Sx 


# Cytnx library:
    
[Cytnx](https://github.com/kaihsin/Cytnx)

# Results:
    The (2nd) energy gap with different system size L that shows the avoid level crossing:

![alt text](https://github.com/kaihsin/ED_TFIM/blob/master/Data/Egap.png?raw=true)

# Implementations:
    * ed_ising.py 
        This one using the overload of matvec interface directly, memory efficient

    * ed_ising_mve.py
        This one store all the elements when calling pre-construct, and use openmp to accelerate. performance efficient


# Developer:

    Kai-Hsin Wu




