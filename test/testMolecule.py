import unittest
from src.molecule import Molecule

class TestMolecule(unittest.TestCase):

    def test_initialization(self):
        mol = Molecule("CCOH")
        self.assertIsInstance(mol, Molecule)
        self.assertEqual(mol.smiles, "CCOH")
        
    def test_centroid(self):
        mol = Molecule("CCOH")
        centroid = mol.centroid()
        self.assertIsInstance(centroid, tuple)
        self.assertEqual(len(centroid), 2) 

if __name__ == "__main__":
    unittest.main()