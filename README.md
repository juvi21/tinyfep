# tinyfep

tinyfep aims to be an simplified abstracted  and short version of the FEB+ method for molecular simulations. Some of the Algorithms are also just simplifications/approximations of the orignal ones but roughly give the core functionality. For now it's main purpose is to be viewed as an educational repo, for those who want to gather a better intuition about how this simumlations work.
Also Tinyrep will be always under 400 lines of core code.

# DISCLAIMER
I'm not a chemist so take everything with a grain of salt. 

## 🌟 Features:

- **SMILES String Parsing:** Convert basic SMILES strings into recognizable molecular structures. (TODO: not every Element is currently supported)
- **Mock Molecular Dynamics:** Simulate molecular behavior using abstracted energy calculations.
- **Energy Functions:** Simplified calculations for Lennard-Jones, hydrogen bonds, and ionic interactions.
- **Advanced Sampling Techniques:** Get a taste of methods like Replica Exchange and Metadynamics.
    
## 📘 Usage:
    git clone https://github.com/juvi21/tinyrep
    cd tinyfep
    python3 tinyfep.py --smiles <SMILES> <SMILES>
    ./run_tests.sh 
  
## ⚠️ Limitations:

- The SMILES parser is elementary, focusing mainly on elements found in proteins.
- Molecular dynamics simulations are more "mock" than "dynamics".
- The energy calculations, though enlightening, are a far cry from real-world complexities.
- The advanced sampling techniques are more illustrative than functional.


## 🚀 Future Plans:


- **Integration with Real MD Engines:** Incorporating tools like GROMACS or CHARMM.
- **Advanced Visualization:** Introducing 3D visualizations and interactive features.
- **Support for More Complex SMILES:** Handling aromaticity, ring closures, and branched structures.
- **Enhanced Error Estimations:** Adopting more sophisticated techniques for error calculations.
