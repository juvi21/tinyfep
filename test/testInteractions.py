import unittest
from src.interactions import lennard_jones_potential, hydrogen_bond_energy, ionic_interaction_energy, advanced_potential_energy
from src.molecule import Molecule


class TestInteractions(unittest.TestCase):

    def test_lennard_jones_potential(self):
        mol1 = Molecule("COH")
        mol2 = Molecule("CONH")

        self.assertIsInstance(lennard_jones_potential(mol1, mol2), float)

    def test_hydrogen_bond_energy(self):
        mol1 = Molecule("COH")
        mol2 = Molecule("CONH")

        self.assertIsInstance(hydrogen_bond_energy(mol1, mol2), float)

    # TODO: Write tests for leaving leaving out functions


if __name__ == '__main__':
    unittest.main()
