import math
import statistics

from src.interactions import advanced_potential_energy
from src.molecule import Molecule


class FreeEnergyPerturbation:

    def __init__(self, molecule_initial, molecule_final):
        self.molecule_initial = molecule_initial
        self.molecule_final = molecule_final

    def softened_potential_energy(self, lambda_value, max_energy=1e5):
        """
        A softened version of the advanced potential energy function that scales based on lambda.
        """
        energy = advanced_potential_energy(
            self.molecule_initial, self.molecule_final)

        # Soften the energy based on lambda
        scaling_factor = lambda_value**2
        softened_energy = scaling_factor * energy

        # Truncate the energy if it's beyond the max_energy threshold
        if softened_energy > max_energy:
            return max_energy
        return softened_energy

    def compute(self, lambda_windows=10, md_steps_per_window=10, T=298.15):
        """
        Compute the Free Energy Perturbation using alchemical transitions
        """
        # Constants
        k = 8.314462618  # J/mol.K (Boltzmann constant)
        beta = 1 / (k * T)

        # Lambda windows for alchemical transitions
        lambda_values = [
            i/lambda_windows for i in range(1, lambda_windows + 1)]

        total_delta_G = 0.0

        # Loop over lambda windows
        for lambda_val in lambda_values:
            alchemical_molecule = Molecule(self.molecule_initial.smiles)
            alchemical_molecule.coordinates = [
                self.molecule_initial.centroid()]

            # Calculate energies for each MD step
            energies = [self.softened_potential_energy(
                lambda_val) for _ in range(md_steps_per_window)]

            # Calculate the free energy difference for this lambda window
            sum_exp_energies = sum([math.exp(-beta * E) for E in energies])
            delta_G = -k * T * math.log(sum_exp_energies / md_steps_per_window)

            total_delta_G += delta_G

        return total_delta_G


class AdvancedSampler:

    def __init__(self, molecule_initial, molecule_final, sampling_method="replica_exchange"):
        self.molecule_initial = molecule_initial
        self.molecule_final = molecule_final
        self.sampling_method = sampling_method

    def replica_exchange(self, temperatures, md_steps_per_temperature):

        energies = []
        for T in temperatures:
            fep_calculator = FreeEnergyPerturbation(
                self.molecule_initial, self.molecule_final)
            energy = fep_calculator.compute(
                T=T, md_steps_per_window=md_steps_per_temperature)
            energies.append(energy)
        # Swapping logic can be incorporated here
        return sum(energies) / len(energies)

    def metadynamics(self, collective_variables, biasing_factor):

        # Very basic
        energy = advanced_potential_energy(
            self.molecule_initial, self.molecule_final)  # To be imported
        return energy - biasing_factor * len(collective_variables)

    def sample(self, **kwargs):

        if self.sampling_method == "replica_exchange":
            return self.replica_exchange(kwargs.get("temperatures", [298.15]), kwargs.get("md_steps_per_temperature", 10))
        elif self.sampling_method == "metadynamics":
            return self.metadynamics(kwargs.get("collective_variables", []), kwargs.get("biasing_factor", 1))
        else:
            raise ValueError("Unknown sampling method")


class ErrorEstimator:

    @staticmethod
    def estimate_error(runs):

        return statistics.stdev(runs)


class PressureEffect:

    @staticmethod
    def apply_pressure_effect(energy, pressure, volume=1.0):

        return energy + pressure * volume
