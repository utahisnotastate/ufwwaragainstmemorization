import os
import json

# === CONFIGURATION ===
SUBMISSION_DIR = "PubChem_Submission_Package_FINAL"
AUTHOR = "Utah Hans"
REPO_URL = "https://github.com/utahisnotastate/ufwwaragainstmemorization"

if not os.path.exists(SUBMISSION_DIR):
    os.makedirs(SUBMISSION_DIR)

# --- HELPER: GENERATE SDF ---
def create_sdf(element_z, symbol, name, comment, filename):
    sdf = f"""
{symbol}{element_z}
  {AUTHOR.replace(" ", "")}0204202610302D 1   1.00000     0.00000

  1  0  0  0  0  0  0  0  0  0999 V2000
    0.0000    0.0000    0.0000 {symbol}  0  0  0  0  0  0  0  0  0  0  0  0
M  END
> <PUBCHEM_SUBSTANCE_SYNONYM>
{name}
Element {element_z}
UFW-{symbol}

> <PUBCHEM_SUBSTANCE_COMMENT>
{comment}
Data Source: {REPO_URL}

> <SUBMITTER_NAME>
{AUTHOR}

> <SUBMITTER_AFFILIATION>
Independent AI Developer

$$$$
"""
    with open(os.path.join(SUBMISSION_DIR, filename), "w") as f:
        f.write(sdf.strip())

# --- HELPER: GENERATE JSON ---
def create_json(element_z, symbol, name, filename):
    data = {
        "PC_Compounds": [{
            "id": {"id": {"cid": 999000 + element_z}},
            "atoms": {"aid": [1], "element": [element_z]},
            "props": [
                {"urn": {"label": "Preferred Name", "name": name, "datatype": 1}, "value": {"sval": name}},
                {"urn": {"label": "Element Symbol", "name": "Standard", "datatype": 1}, "value": {"sval": symbol}}
            ]
        }]
    }
    with open(os.path.join(SUBMISSION_DIR, filename), "w") as f:
        json.dump(data, f, indent=4)

# --- GENERATE THE MISSING PIECES ---
# 1. Element 119 (Bella's Flying Squirrel / Ufw-Alpha)
create_sdf(119, "Uue", "Ununennium (Ufw-Alpha)",
           "Relativistic 8s valence tunneling variant. Predicted ionization energy < 3.5 eV.",
           "structure_119_ununennium.sdf")
create_json(119, "Uue", "Ununennium", "structure_119_ununennium.json")

# 2. Element 120 (Unbinilium)
create_sdf(120, "Ubn", "Unbinilium",
           "Hyper-reactive alkaline earth analog with 8s contraction.",
           "structure_120_unbinilium.sdf")
create_json(120, "Ubn", "Unbinilium", "structure_120_unbinilium.json")

# 3. Element 126 (Utahium) - REGENERATING JSON to match
create_json(126, "Ut", "Utahium", "structure_126_utahium.json")

print(f"✅ PACKAGE COMPLETE. Files ready in {SUBMISSION_DIR}")
