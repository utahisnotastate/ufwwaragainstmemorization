import os
import json

# === CONFIGURATION ===
SUBMISSION_DIR = "PubChem_Submission_Package"
AUTHOR_NAME = "Utah Hans"  # UPDATED IDENTITY

if not os.path.exists(SUBMISSION_DIR):
    os.makedirs(SUBMISSION_DIR)

def generate_pubchem_sdf():
    print(f"Generatng SDF for {AUTHOR_NAME}...")
    sdf_content = f"""
310Ut
  {AUTHOR_NAME.replace(" ", "")}0204202610302D 1   1.00000     0.00000

  1  0  0  0  0  0  0  0  0  0999 V2000
    0.0000    0.0000    0.0000 Ut  0  0  0  0  0  0  0  0  0  0  0  0
M  END
> <PUBCHEM_SUBSTANCE_SYNONYM>
Utahium
Element 126
Unbihexium
Ufw-Anchor

> <PUBCHEM_SUBSTANCE_COMMENT>
Proposed stable superheavy element Z=126 based on Tensor-Optimized Relativistic Mean Field Theory.
Predicted Half-life > 10^9 years.
Valence configuration: [Og] 5g6 8s2.

> <SUBMITTER_NAME>
{AUTHOR_NAME}

> <SUBMITTER_AFFILIATION>
Independent AI Developer

$$$$
"""
    sdf_path = os.path.join(SUBMISSION_DIR, "structure_126_utahium.sdf")
    with open(sdf_path, "w") as f:
        f.write(sdf_content.strip())
    return sdf_path

generate_pubchem_sdf()
print(f"✅ Data Manifest Updated. Submitter: {AUTHOR_NAME}")
