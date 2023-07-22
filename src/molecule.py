class Molecule:

    def __init__(self, smiles):
        self.smiles = smiles
        self.atoms, self.coordinates = self.improved_parse_smiles(smiles)

    def improved_parse_smiles(self, smiles):
        """
        Improved method to convert SMILES string to 2D coordinates.
        """
        elements = ["C", "H", "O", "N", "S", "P", "F", "Cl", "Br", "I"]
        bonds = ["-", "=", "#"]

        atoms = []
        i = 0
        while i < len(smiles):
            # Handle two-character elements (e.g., Cl, Br)
            if i < len(smiles) - 1 and smiles[i:i+2] in elements:
                atoms.append(smiles[i:i+2])
                i += 2
            elif smiles[i] in elements:
                atoms.append(smiles[i])
                i += 1
            elif smiles[i] in bonds:
                # we'll skip bonds in the coordinate representation
                i += 1
            else:
                # Raise an error for unhandled characters
                raise ValueError(f"Unhandled character in SMILES: {smiles[i]}")

        # Create a simple 2D coordinate representation (linear on x-axis)
        coordinates = [(i, 0) for i in range(len(atoms))]
        return atoms, coordinates

    def centroid(self):
        """
        Compute the centroid (geometric center) of the molecule.
        """
        x_coords, y_coords = zip(*self.coordinates)
        centroid_x = sum(x_coords) / len(x_coords)
        centroid_y = sum(y_coords) / len(y_coords)
        return centroid_x, centroid_y
