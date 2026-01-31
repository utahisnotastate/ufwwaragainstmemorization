import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap

# === DIRECTORY SETUP ===
REPO_NAME = "Utah_Science_Directorate_Archives"
PAPERS_DIR = os.path.join(REPO_NAME, "Golden_Master_Papers")
IMAGES_DIR = os.path.join(REPO_NAME, "Visual_Data_Manifests")

if not os.path.exists(PAPERS_DIR): os.makedirs(PAPERS_DIR)
if not os.path.exists(IMAGES_DIR): os.makedirs(IMAGES_DIR)


# ==========================================================
# PART 1: UTAH'S SWIRLD (INFOGRAPHIC EDITION)
# ==========================================================
def generate_advanced_swirld():
    print("Generating High-Fidelity Swirld Visualization...")
    fig = plt.figure(figsize=(24, 24), facecolor='#0B0C10')
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor('#0B0C10')

    # --- CONFIGURATION ---
    # We use a logarithmic spiral: r = a * e^(b * theta)
    # But for periodic elements, we want 'shells' to be distinct rings.
    # We will use a "Quantized Spiral" mapping.

    max_z = 174

    # Agency Colors (Professional Palette)
    colors = {
        's': '#45A29E',  # Standard (Teal)
        'BFS': '#F7CE5B',  # Bella's Flying Squirrels (Gold)
        'Hood': '#C34A36',  # Hoodlums (Rust Red)
        'Utah': '#66FCF1',  # Utahium (Neon Cyan)
        'UIA': '#A29BFE',  # Intel Agency (Periwinkle)
        'UOA': '#6C5CE7'  # Occult Agency (Deep Violet)
    }

    # --- PLOTTING LOOP ---
    for z in range(1, max_z + 1):
        # MAPPING Z TO GEOMETRY
        # Determine Period (n) and Group approximately
        if z <= 2:
            n = 1
        elif z <= 10:
            n = 2
        elif z <= 18:
            n = 3
        elif z <= 36:
            n = 4
        elif z <= 54:
            n = 5
        elif z <= 86:
            n = 6
        elif z <= 118:
            n = 7
        elif z <= 138:
            n = 8  # G-Block Expansion
        else:
            n = 9  # Supercritical

        # Radius correlates to Principle Quantum Number (n)
        # We add a small spiral factor based on Z to make it flow
        r = n * 10 + (z / max_z) * 5

        # Theta correlates to Group/Chemical Property
        # We group them so similar elements align radially
        # This is a simplified hash for visual "Swirl" alignment
        if n == 1:
            theta = (z - 1) * np.pi
        elif n <= 3:
            theta = ((z % 8) / 8) * 2 * np.pi
        elif n <= 5:
            theta = ((z % 18) / 18) * 2 * np.pi
        elif n <= 7:
            theta = ((z % 32) / 32) * 2 * np.pi
        else:
            theta = ((z % 50) / 50) * 2 * np.pi  # G-block density

        # --- DATA & AGENCY LOGIC ---
        color = colors['s']
        size = 80
        label = str(z)
        marker = 'o'

        # Bella's Flying Squirrels (119-120)
        if z in [119, 120]:
            color = colors['BFS']
            size = 350
            label = f"BFS\n{z}"
            marker = 'D'  # Diamond for high energy

        # The Hoodlums (121-136)
        elif 121 <= z <= 136:
            color = colors['Hood']
            size = 200

        # UTAHIUM (126) - THE ANCHOR
        if z == 126:
            color = colors['Utah']
            size = 800
            label = "UTAH\n126"
            marker = '*'  # Star

        # Utah Intelligence Agency (137)
        if z == 137:
            color = colors['UIA']
            size = 500
            label = "UIA\n137"
            marker = 'H'  # Hexagon

        # Utah Occult Agency (173)
        if z == 173:
            color = colors['UOA']
            size = 600
            label = "UOA\n173"
            marker = 'X'

        # Plot Point
        ax.scatter(theta, r, s=size, c=color, marker=marker, edgecolors='white', linewidth=1.5, zorder=10, alpha=0.9)

        # Label High Value Targets
        if size > 100:
            ax.text(theta, r, label, color='white', fontsize=9, fontweight='bold', ha='center', va='center')

    # --- INFOGRAPHIC OVERLAYS ---
    # Draw "Shell" Rings
    for i in range(1, 10):
        circle = plt.Circle((0, 0), i * 10, transform=ax.transData._b, color='#1F2833', fill=False, linestyle='--',
                            linewidth=1)
        ax.add_artist(circle)

    # --- LEGEND & INFO ---
    plt.title("UTAH'S SWIRLD: THE HARMONIC RESONANCE MAP\nTimeline Omega // Verified Physics", color='white',
              fontsize=28, pad=40)

    # Custom Legend Box (drawn as text block)
    legend_text = """
    AGENCY LEGEND:

    [119-120] BELLA'S FLYING SQUIRRELS
    Physics: Relativistic 8s Tunneling
    Status: Hyper-Reactive

    [121-136] THE HOODLUMS (G-Block)
    Physics: 5g Orbital Collapse
    Status: Anomalous Filling

    [126] UTAHIUM (THE ANCHOR)
    Physics: Tensor-Stabilized Shell Closure
    Status: ETERNAL

    [137] UTAH INTELLIGENCE (UIA)
    Physics: Sommerfeld Limit (v ~ c)
    Status: Information Horizon

    [173] UTAH OCCULT (UOA)
    Physics: Vacuum Polarization > 2mc^2
    Status: Matter Genesis
    """
    plt.text(1.2, 0.1, legend_text, transform=ax.transAxes, color='#C5C6C7', fontsize=12,
             bbox=dict(facecolor='#1F2833', edgecolor='#66FCF1', boxstyle='round,pad=1'))

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(False)

    plt.savefig(os.path.join(IMAGES_DIR, "Utahs_Swirld_Master.png"), dpi=300, facecolor='#0B0C10', bbox_inches='tight')
    plt.close()


generate_advanced_swirld()

# ==========================================================
# PART 2: PAPER 1 - BELLA'S FLYING SQUIRRELS (119-120)
# ==========================================================
paper_119 = r"""
\documentclass[11pt, reqno]{amsart}
\usepackage{amsmath, amssymb, physics, graphicx}
\title[Dynamics of 8s Valence States]{Relativistic Tunneling and Valence Delocalization in Elements Z=119 and Z=120}
\author{Utah Science Directorate (Agency: B.F.S.)}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
We investigate the electronic structure of Ununennium ($Z=119$) and Unbinilium ($Z=120$). Standard Dirac-Fock calculations predict a relativistic contraction of the $8s$ orbital. However, we demonstrate that the "tail" of the wavefunction exhibits an anomalously high tunneling probability into the vacuum continuum. We designate these elements as the "Flying Squirrel" series due to the hyper-mobile nature of the valence charge density.
\end{abstract}

\section{Introduction}
The breakdown of the Aufbau principle in the superheavy regime is well documented. For $Z > 118$, the relativistic enhancement of the electron mass ($m = \gamma m_0$) significantly contracts the $s_{1/2}$ orbitals.
However, for the $8s$ shell, a secondary effect emerges: \textbf{Vacuum-Assisted Tunneling}.

\section{The Squirrel Hamiltonian}
We model the $8s$ electron using a modified radial Dirac equation:
\begin{equation}
    \left( \frac{d}{dr} + \frac{\kappa}{r} \right) G(r) - (E + m - V(r))F(r) = 0
\end{equation}
In the "Bella's Flying Squirrel" (BFS) regime, the potential $V(r)$ includes a shielding term from the core 118 electrons that effectively "launches" the $8s$ electron.
Calculations show the ionization energy is remarkably low ($I_p \approx 3.5$ eV), making these atoms capable of "jumping" reaction barriers that would block standard alkali metals.

\section{Conclusion}
Elements 119 and 120 represent a new class of "Tunneling Metals." Their chemistry is dominated not by sharing electrons, but by projecting them.

\end{document}
"""

with open(os.path.join(PAPERS_DIR, "119_BFS_Dynamics.tex"), "w") as f:
    f.write(paper_119)

# ==========================================================
# PART 3: PAPER 2 - UIA / FEYNMANIUM (137)
# ==========================================================
paper_137 = r"""
\documentclass[11pt, reqno]{amsart}
\usepackage{amsmath, amssymb, physics}
\title[The Sommerfeld Limit]{Resolution of the Z=137 Catastrophe via Finite Nuclear Size Effects: The "Limitless" Protocol}
\author{Utah Intelligence Agency (UIA)}

\begin{document}
\maketitle

\begin{abstract}
The Dirac equation for a point nucleus predicts a singularity at $Z \approx 137$, where the ground state energy becomes imaginary ($Z\alpha > 1$). This has historically been termed "Feynmanium." We present the "Limitless" solution by treating the nucleus as a charged torus of radius $R_N$. This regularization allows stable bound states to exist beyond $Z=137$, converting the atom into a super-critical bosonic bridge.
\end{abstract}

\section{The Z=137 Singularity}
The energy eigenvalues for a hydrogen-like atom are:
\begin{equation}
    E_{1s} = m_e c^2 \sqrt{1 - (Z\alpha)^2}
\end{equation}
When $Z=137$, $Z\alpha \approx 1$, and $E_{1s} \to 0$. Beyond this, the math breaks for point particles.

\section{The UIA Correction}
By integrating the electron wavefunction inside a finite nuclear volume (The Utah Radius), the potential $V(r)$ is smoothed:
\begin{equation}
    V(r) = -\frac{Ze^2}{2R_N} \left( 3 - \frac{r^2}{R_N^2} \right), \quad r < R_N
\end{equation}
This allows the $1s$ orbital to dive into the negative energy continuum without collapsing. The element UIA-137 acts as a gateway where electronic velocity approaches $c$, allowing for instantaneous quantum correlation (Intelligence gathering) across the atomic radius.

\end{document}
"""

with open(os.path.join(PAPERS_DIR, "137_UIA_Limitless.tex"), "w") as f:
    f.write(paper_137)

# ==========================================================
# PART 4: PAPER 3 - UOA / SKYRMIUM (173)
# ==========================================================
paper_173 = r"""
\documentclass[11pt, reqno]{amsart}
\usepackage{amsmath, amssymb, physics}
\title[Vacuum Decay at Z=173]{The Supercritical Vacuum: Spontaneous Pair Production in Element 173 (UOA-Void)}
\author{Utah Occult Agency (UOA)}

\begin{document}
\maketitle

\begin{abstract}
At $Z_{cr} \approx 173$, the binding energy of the $1s$ shell reaches $2m_e c^2$. We demonstrate that this threshold triggers the "diving" of the bound state into the Dirac Sea, resulting in the spontaneous emission of positrons. This element, designated UOA-Void, effectively harvests matter from the vacuum ground state.
\end{abstract}

\section{The Diving Phenomenon}
As $Z$ approaches 173, the $1s$ energy level $E_{1s}$ descends until:
\begin{equation}
    E_{1s} = -m_e c^2
\end{equation}
At this point, the empty K-shell is degenerate with the negative energy continuum. If the K-shell is empty, an electron from the vacuum spontaneously fills it, leaving a hole (positron) in the continuum which is emitted.

\section{The Occult Mechanism}
We define the "Occult" cross-section $\sigma_{void}$ as the probability of vacuum decay. UOA-173 is not a standard element; it is a permanent resonance in the fabric of spacetime. It does not decay; it breathes the vacuum.

\end{document}
"""

with open(os.path.join(PAPERS_DIR, "173_UOA_Void.tex"), "w") as f:
    f.write(paper_173)

print("GOLDEN MASTER ARCHIVE GENERATED SUCCESSFULLY.")
