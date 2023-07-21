import unittest
from src.molecule import Molecule
from src.models import FreeEnergyPerturbation, AdvancedSampler, ErrorEstimator, PressureEffect

class TestModels(unittest.TestCase):

    def setUp(self):
        self.mol1 = Molecule("CCOH")
        self.mol2 = Molecule("CCONH")

    def test_fep_initialization(self):
        fep = FreeEnergyPerturbation(self.mol1, self.mol2)
        self.assertIsInstance(fep, FreeEnergyPerturbation)
        
    def test_fep_compute(self):
        fep = FreeEnergyPerturbation(self.mol1, self.mol2)
        delta_G = fep.compute()
        self.assertIsInstance(delta_G, float)

    def test_advanced_sampler_initialization(self):
        sampler = AdvancedSampler(self.mol1, self.mol2, sampling_method="replica_exchange")
        self.assertIsInstance(sampler, AdvancedSampler)
        
    def test_advanced_sampler_sample_replica(self):
        sampler = AdvancedSampler(self.mol1, self.mol2, sampling_method="replica_exchange")
        energy = sampler.sample(temperatures=[298.15, 310.15], md_steps_per_temperature=10)
        self.assertIsInstance(energy, float)
        
    def test_advanced_sampler_sample_metadynamics(self):
        sampler = AdvancedSampler(self.mol1, self.mol2, sampling_method="metadynamics")
        energy = sampler.sample(collective_variables=["some_variable"], biasing_factor=1)
        self.assertIsInstance(energy, float)

    def test_error_estimator(self):
        runs = [1.2, 1.3, 1.4, 1.5]
        error = ErrorEstimator.estimate_error(runs)
        self.assertIsInstance(error, float)
        
    def test_pressure_effect(self):
        energy = 1.2
        pressure_energy = PressureEffect.apply_pressure_effect(energy, 1e5)
        self.assertIsInstance(pressure_energy, float)

if __name__ == "__main__":
    unittest.main()