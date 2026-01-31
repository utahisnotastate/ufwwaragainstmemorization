import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# === CONFIGURATION ===
REPO_NAME = "ufwwaragainstmemorization"
AUTHOR = "General Utah-1 (Omega Archive)"

# Create Directory Structure
if not os.path.exists(REPO_NAME):
    os.makedirs(REPO_NAME)
    os.makedirs(os.path.join(REPO_NAME, "Element_Papers"))
    os.makedirs(os.path.join(REPO_NAME, "Images"))


# ==========================================
# 1. GENERATE THE "OMEGA TABLE" (VISUAL)
# ==========================================
def generate_omega_table():
    print("Manifesting the Omega Periodic Table...")
    fig, ax = plt.subplots(figsize=(24, 14))
    ax.set_facecolor('#0f0f0f')  # Void Black

    # --- ELEMENT DATA (Z, Symbol, Name, Category) ---
    # We rename 137 and 173 as requested
    elements = [
        (119, "Ufw-I", "Ufw-Alpha (The Igniter)", "Alkali"),
        (120, "Ubn", "Unbinilium", "Alkaline Earth"),
        (121, "Ubu", "Unbiunium", "Superactinide Start"),
        (126, "Ut", "UTAHIUM (The Anchor)", "Island of Stability"),
        (137, "Ufw-L", "UFW-LIMITLESS (Formerly Feynmanium)", "Relativistic Limit"),
        (155, "Kh", "Khalsium", "Hyper-Actinide"),
        (173, "Ufw-V", "UFW-VOID (Formerly Skyrmium)", "Vacuum Collapse"),
    ]

    # Draw "Old World" Ghost (Period 7)
    rect = patches.Rectangle((0, 2), 18, 1, linewidth=1, edgecolor='#444', facecolor='#222')
    ax.add_patch(rect)
    ax.text(9, 2.5, "OLD WORLD (Periods 1-7) - OBSOLETE", color='#555', ha='center', va='center', fontsize=20,
            fontweight='bold')

    # Draw Period 8 (The G-Block)
    y_pos = 0.5
    start_x = 0

    # Draw logic
    for i in range(18):  # Placeholder boxes for the row
        rect = patches.Rectangle((i, 0), 1, 1.5, linewidth=1, edgecolor='#333', facecolor='#1a1a1a')
        ax.add_patch(rect)

    # Place Specific Omega Elements
    # Mappings (approximate column for visual)
    locations = {
        119: 0,
        120: 1,
        121: 2,
        126: 7,  # Center of G-Block
        137: 17,  # End of Period 8 (Hypothetical)
    }

    # Period 9 (The Vacuum Limit)
    rect_void = patches.Rectangle((10, -2), 1, 1.5, linewidth=3, edgecolor='#8e44ad', facecolor='#1a1a1a')
    ax.add_patch(rect_void)
    locations[173] = (10, -2)  # Special placement

    # Draw Elements
    for z, sym, name, cat in elements:
        if z == 173:
            x, y = locations[z]
        else:
            x = locations.get(z, -1)
            y = 0

        if x != -1:
            # Color Logic
            if z == 126:
                color = "#00d2d3"  # Cyan for Utahium
            elif z == 137:
                color = "#ff6b6b"  # Red for Limitless
            elif z == 173:
                color = "#a29bfe"  # Purple for Void
            elif z == 119:
                color = "#feca57"
            else:
                color = "#54a0ff"

            rect = patches.Rectangle((x, y), 1, 1.5, linewidth=3 if z in [126, 137, 173] else 1, edgecolor=color,
                                     facecolor='#2d3436')
            ax.add_patch(rect)

            ax.text(x + 0.1, y + 1.2, str(z), color='white', fontsize=12, fontweight='bold')
            ax.text(x + 0.5, y + 0.8, sym, color=color, fontsize=22, fontweight='bold', ha='center')
            ax.text(x + 0.5, y + 0.4, name.split()[0], color='white', fontsize=8, ha='center')

            # Annotations
            if z == 126:
                ax.annotate("THE ANCHOR\n(Half-Life > 10^9 yrs)", xy=(x + 0.5, y + 1.5), xytext=(x + 0.5, y + 3),
                            arrowprops=dict(facecolor=color, shrink=0.05), color=color, ha='center', fontsize=12)
            if z == 137:
                ax.annotate("SPEED OF LIGHT\nBROKEN HERE", xy=(x + 0.5, y + 1.5), xytext=(x + 0.5, y + 2.5),
                            arrowprops=dict(facecolor=color, shrink=0.05), color=color, ha='center', fontsize=12)
            if z == 173:
                ax.annotate("VACUUM COLLAPSE\n(Matter from Nothing)", xy=(x + 0.5, y), xytext=(x + 0.5, y - 1),
                            arrowprops=dict(facecolor=color, shrink=0.05), color=color, ha='center', fontsize=12)

    ax.set_xlim(-1, 19)
    ax.set_ylim(-3, 4)
    ax.axis('off')
    ax.set_title("FUTURE DISCLOSURE: THE OMEGA TABLE (Period 8 & 9)", color='white', fontsize=25, pad=20)

    plt.savefig(os.path.join(REPO_NAME, "Images", "Omega_Table.png"), dpi=150, facecolor='#0f0f0f')
    plt.close()


generate_omega_table()

# ==========================================
# 2. GENERATE THE MANIFESTO (README.md)
# ==========================================
readme_content = f"""
# UFW: THE WAR AGAINST MEMORIZATION
### Future Disclosure of the True Periodic Table
**Status:** DECLASSIFIED (Omega Archive)
**Architect:** {AUTHOR}

## 1. THE LIE OF COMPLEXITY
In 2025, chemistry is taught as a list of rules to memorize. 
* "Memorize the orbitals."
* "Memorize the exceptions."
* "Memorize the names of dead physicists."

**This ends today.**

In the Omega Timeline, we know that atoms are not complex. They are **Musical Geometries**.
* Protons are simply localized vibrations in the vacuum density.
* Stability occurs at "Perfect Chords" (Magic Numbers: 2, 8, 20, 28, 50, 82, 126).
* **Utahium (126)** is the final "Perfect Chord." It is the C-Major chord of the universe.

## 2. THE NEW ELEMENTS (RENAMED)
We have discarded the names of the "Old World" heroes who said these elements were impossible.
We honor the **Future Warriors** who broke the limits.

| Z | Old Name | **NEW NAME (UFW Designation)** | The Physics |
|---|---|---|---|
| **119** | Ununennium | **Ufw-Alpha (The Igniter)** | An alkali metal so reactive it ionizes vacuum fluctuations. |
| **126** | Unbihexium | **UTAHIUM (The Anchor)** | The "Island of Stability." A primordial, non-decaying super-metal. |
| **137** | Feynmanium | **UFW-LIMITLESS** | At Z=137, the 1s electron must move at $c$. Standard physics breaks. We fixed it. |
| **173** | Skyrmium | **UFW-VOID** | The nucleus is so positive it rips electrons out of empty space. Free energy. |

## 3. HOW TO USE THIS REPO
Review the `Element_Papers` folder. Each paper provides the **mathematical proof** (Tensor-RMF Theory) that these elements exist and explains why the old world missed them.

**The War is Over. The Future is Here.**
"""

with open(os.path.join(REPO_NAME, "README.md"), "w") as f:
    f.write(readme_content)

# ==========================================
# 3. GENERATE PAPER: Z=137 (UFW-LIMITLESS)
# ==========================================
paper_137 = r"""
# ELEMENT 137: UFW-LIMITLESS (Formerly Feynmanium)
### The Death of Standard Relativity

**ABSTRACT**
Old World physics (Dirac Equation) predicts a catastrophe at $Z=137$.
The energy of the 1s electron is given by:
$$ E_{1s} = mc^2 \sqrt{1 - (Z\alpha)^2} $$
where $\alpha \approx 1/137$. 
If $Z > 137$, the term inside the square root becomes negative. The math breaks. They called it "Feynmanium" and said it was the end.

**THE UFW SOLUTION**
We rename this **Ufw-Limitless** because it is not a limit; it is a transition.
In the Omega timeline, we treat the nucleus not as a point, but as a **Charged Torus**.
When you account for the *finite size* of the nucleus (using the Fermi distribution), the singularity disappears. 
The electron does not "crash"; it enters a **super-critical resonance state**.

**CONCLUSION**
Ufw-Limitless is not matter. It is a **Bosonic Bridge**. It allows electrons to pair up in the 1s shell and behave like light.
"""
with open(os.path.join(REPO_NAME, "Element_Papers", "137_Ufw_Limitless.md"), "w") as f:
    f.write(paper_137)

# ==========================================
# 4. GENERATE PAPER: Z=173 (UFW-VOID)
# ==========================================
paper_173 = r"""
# ELEMENT 173: UFW-VOID (Formerly Skyrmium)
### The Vacuum Boiler

**ABSTRACT**
At $Z=173$, the binding energy of the 1s electron reaches $2mc^2$ (approx 1.022 MeV).
This is the exact energy required to create an electron-positron pair from nothing.

**OLD WORLD FEAR**
Physicists feared this element because it would "decay the vacuum." If a 1s slot is empty, the atom pulls an electron *out of empty space* to fill it, spitting out a positron.

**THE UFW APPLICATION**
We do not fear this. We use it.
**Ufw-Void** is the engine of the Omega Timeline.
1.  Strip the electrons from a Ufw-Void nucleus.
2.  The nucleus "eats" the vacuum to replenish its shells.
3.  It emits positrons.
4.  We harvest the positrons for antimatter fuel.

**NOMENCLATURE**
We strip the name "Skyrmium" (based on the Skyrme model which failed to predict this utility). 
We name it **Ufw-Void** to honor the warriors who harness the nothingness.
"""
with open(os.path.join(REPO_NAME, "Element_Papers", "173_Ufw_Void.md"), "w") as f:
    f.write(paper_173)

# ==========================================
# 5. GENERATE PAPER: Z=126 (UTAHIUM)
# ==========================================
paper_126 = r"""
# ELEMENT 126: UTAHIUM (The Anchor)
### The Center of the G-Block

**THE DISCOVERY**
Discovered by General Utah-1 via the Akashic Record.
While the world looked for stability at 114, Utah-1 applied **Tensor Couplings** to the Relativistic Mean Field.
The result was unambiguous:
* Proton Shell Closure: **126**
* Neutron Shell Closure: **184**

**PROPERTIES**
* **Density:** 28.4 g/cm³ (2.5x denser than Lead).
* **Melting Point:** > 3000 K.
* **Radiation Shielding:** 1mm of Utahium blocks gamma rays equivalent to 1m of Lead.

**USAGE**
Utahium is the "Chassis Material" for Timeline Omega technology. It does not vibrate. It does not bend. It anchors reality.
"""
with open(os.path.join(REPO_NAME, "Element_Papers", "126_Utahium.md"), "w") as f:
    f.write(paper_126)

print(f"✅ UFW PROTOCOL COMPLETE. Repository generated at: {os.path.abspath(REPO_NAME)}")
