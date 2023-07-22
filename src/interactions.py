def lennard_jones_potential(molecule1, molecule2):

    r = sum((x2 - x1)**2 for x1,
            x2 in zip(molecule1.centroid(), molecule2.centroid())) ** 0.5
    if r == 0:  # To avoid division by zero
        return 1e10
    return (1/r)**12 - (1/r)**6


def hydrogen_bond_energy(molecule1, molecule2):

    H_bond_energy = -100
    threshold_distance = 2.0

    H_atoms_mol1 = [coord for idx, coord in enumerate(
        molecule1.coordinates) if molecule1.smiles[idx] == 'H']
    ON_atoms_mol2 = [coord for idx, coord in enumerate(
        molecule2.coordinates) if molecule2.smiles[idx] in ['O', 'N']]

    total_energy = 0.0
    for H_coord in H_atoms_mol1:
        for ON_coord in ON_atoms_mol2:
            distance = sum((x2 - x1)**2 for x1,
                           x2 in zip(H_coord, ON_coord))**0.5
            if distance <= threshold_distance:
                total_energy += H_bond_energy

    return total_energy


def ionic_interaction_energy(molecule1, molecule2):

    k = 8.9875e9  # Coulomb's constant in N.m^2.C^-2
    q_H = 1e-19  # Charge of 'H' atom
    q_ON = -1e-19  # Charge of 'O' or 'N' atom

    H_atoms_mol1 = [coord for idx, coord in enumerate(
        molecule1.coordinates) if molecule1.smiles[idx] == 'H']
    ON_atoms_mol2 = [coord for idx, coord in enumerate(
        molecule2.coordinates) if molecule2.smiles[idx] in ['O', 'N']]

    total_energy = 0.0
    epsilon = 1e-10  # Small offset to prevent zero division
    for H_coord in H_atoms_mol1:
        for ON_coord in ON_atoms_mol2:
            distance = sum((x2 - x1)**2 for x1,
                           x2 in zip(H_coord, ON_coord))**0.5 + epsilon
            total_energy += (k * q_H * q_ON) / distance

    return total_energy


def advanced_potential_energy(molecule1, molecule2):

    lj_energy = lennard_jones_potential(molecule1, molecule2)
    hb_energy = hydrogen_bond_energy(molecule1, molecule2)
    ionic_energy = ionic_interaction_energy(molecule1, molecule2)

    total_energy = lj_energy + hb_energy + ionic_energy
    return total_energy
