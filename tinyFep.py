from src.molecule import Molecule

from src.models import FreeEnergyPerturbation, AdvancedSampler, ErrorEstimator, PressureEffect

import argparse


def main(args):
    mol1 = Molecule(args.smiles[0])
    mol2 = Molecule(args.smiles[1])

    # Compute Free Energy using the FreeEnergyPerturbation class
    fep = FreeEnergyPerturbation(mol1, mol2)
    delta_G = fep.compute()
    print(f"Free Energy Difference (FEP): {delta_G} J/mol")

    # Use advanced sampling techniques
    sampler = AdvancedSampler(mol1, mol2, sampling_method="replica_exchange")
    sampled_energy = sampler.sample(temperatures=[298.15, 310.15], md_steps_per_temperature=10)
    print(f"Energy with Advanced Sampling: {sampled_energy} J/mol")

    # Apply pressure effects
    energy_with_pressure = PressureEffect.apply_pressure_effect(sampled_energy, 1e5)  # Applying 1 atm pressure
    print(f"Energy with Pressure Effects: {energy_with_pressure} J/mol")

    # Estimate error from multiple runs (for simplicity, we mock different runs with slight variations)
    runs = [fep.compute() for _ in range(10)]
    error = ErrorEstimator.estimate_error(runs)
    print(f"Estimated Error: ±{error} J/mol")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process SMILES strings of molecules.')
    parser.add_argument('--smiles', type=str, nargs=2, required=True, help='SMILES strings of the two molecules.')
    args = parser.parse_args()
    main(args)
