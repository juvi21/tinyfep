# tinyfep

`tinyfep` aims to be a simplified and abstracted version of the FEP+ method for molecular simulations. Some algorithms are simplifications or approximations of the original ones, yet they provide a glimpse into the core functionality. For now, it's primary purpose is educational, catering to those eager to gain an intuition about how these simulations work. Also, `tinyfep` will always stay under 400 lines of core code.

### DISCLAIMER
I'm not a chemist so take everything with a grain of salt. 

### 🌟 Features:

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
- **Support for More Complex SMILES:** Handling aromaticity, ring closures, and branched structures.
- **Enhanced Error Estimations:** Adopting more sophisticated techniques for error calculations.
