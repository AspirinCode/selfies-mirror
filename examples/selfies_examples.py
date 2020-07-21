"""This file contains examples of how to use the ``selfies`` library.
"""

from rdkit import Chem

import selfies as sf

# 1. First we try translating SMILES --> SELFIES --> SMILES.

# Test SMILES: non-fullerene acceptors for organic solar cells.
smiles = "CN1C(=O)C2=C(c3cc4c(s3)-c3sc(-c5ncc(C#N)s5)cc3C43OCCO3)N(C)C(=O)" \
         "C2=C1c1cc2c(s1)-c1sc(-c3ncc(C#N)s3)cc1C21OCCO1"
encoded_selfies = sf.encoder(smiles)  # SMILES --> SEFLIES
decoded_smiles = sf.decoder(encoded_selfies)  # SELFIES --> SMILES

print(f"Original SMILES: {smiles}")
print(f"Translated SELFIES: {encoded_selfies}")
print(f"Translated SMILES: {decoded_smiles}")
print()

# When comparing the original and decoded SMILES, do not use == equality. Use
# RDKit to check both SMILES correspond to the same molecule.
print(f"== Equals: {smiles == decoded_smiles}")

can_smiles = Chem.CanonSmiles(smiles)
can_decoded_smiles = Chem.CanonSmiles(decoded_smiles)
print(f"RDKit Equals: {can_smiles == can_decoded_smiles}")
print()

# 2. Let's view the SELFIES alphabet.

new_alphabet = sf.get_alphabet()
print(f"Default Alphabet:\n {new_alphabet}")
print()

new_atom_dict = sf.get_atom_dict()
print(f"Default Atom Dict:\n {new_atom_dict}")
print()


# Advanced Usage:
# 3. Let's customize the SELFIES alphabet

# We have two compounds here, C#S and Li=CCC in SELFIES form
c_s_compound = sf.encoder("CS=CC#S")
li_compound = sf.encoder("[Li]=CC")

# Under the default SELFIES settings, they are translated as
print("Default SELFIES:")
print(f"\t CS=CC#S --> {sf.decoder(c_s_compound)}")
print(f"\t [Li]=CC --> {sf.decoder(li_compound)}")

# Now we add [Li] to the SELFIES alphabet, and restrict it to 1 bond only
# Also, let's restrict S to 2 bonds (instead of its default 6).
atom_dict = new_atom_dict
atom_dict['[Li]'] = 1
atom_dict['S'] = 2

sf.set_alphabet(atom_dict)  # update alphabet

# Under our new settings, they are translated as
print("Customized SELFIES:")
print(f"\t CS=CC#S --> {sf.decoder(c_s_compound)}")
print(f"\t [Li]=CC --> {sf.decoder(li_compound)}")
print()
# Notice that all the bond constraints are met.

# Let's check on the SELFIES alphabet an atom dict to see if they
# are updated. Note that [Li] is now in the SELFIES alphabet (see
# [Liexpl], [=Liexpl], [#Liexpl], ...)

new_alphabet = sf.get_alphabet()
print(f"Updated Alphabet:\n {new_alphabet}")
print()

new_atom_dict = sf.get_atom_dict()
print(f"Updated Atom Dict:\n {new_atom_dict}")
print()

# 4. Let's revert the SELFIES alphabet back to the default settings
sf.set_alphabet()
