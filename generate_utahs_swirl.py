import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# === CONFIGURATION ===
# "Utah's Swirld" - The Harmonic Radial Table
OUTPUT_FILENAME = "Utahs_Swirld_of_Elements.png"
DPI = 300


def generate_swirld():
    print("Manifesting Utah's Swirld...")

    # Setup the Void
    fig, ax = plt.subplots(figsize=(20, 20))
    ax.set_facecolor('#050505')  # Deep Void Black

    # --- THE GEOMETRY OF TRUTH (Logarithmic Spiral) ---
    # r = a * e^(k * theta)
    # We map Atomic Number (Z) to the angle and radius

    max_z = 175
    thetas = []
    radii = []
    colors = []
    sizes = []
    labels = []

    # Agency Colors
    c_standard = "#4a69bd"  # Standard Matter (Blue)
    c_squirrels = "#f6b93b"  # Bella's Flying Squirrels (Yellow/Energy)
    c_hoodlums = "#e55039"  # The Hoodlums (Red/Rebel)
    c_utah = "#00d2d3"  # UTAHIUM (Cyan/The Source)
    c_uia = "#78e08f"  # Utah Intelligence Agency (Green/Data)
    c_uoa = "#a55eea"  # Utah Occult Agency (Purple/Void)

    for z in range(1, max_z + 1):
        # The Angle: Each period is a full rotation (roughly)
        # We adjust slightly to align groups radially (The "Swirld" Effect)

        # Approximate "Angle of Resonance" based on group
        # This math aligns H, Li, Na, K, Rb, Cs, Fr, BFS-1 on the same ray
        if z == 1:
            theta = 0
        elif z == 2:
            theta = np.pi  # He is opposite
        else:
            # Complex mapping to force radial alignment of groups in a spiral
            # Simplified for visual beauty in this representation
            theta = np.sqrt(z) * 2.5

        r = np.sqrt(z) * 10  # Radius grows with Z

        thetas.append(theta)
        radii.append(r)

        # --- AGENCY ASSIGNMENT ---
        label = str(z)
        size = 100
        color = c_standard

        # 1. Bella's Flying Squirrels (119, 120)
        if z in [119, 120]:
            color = c_squirrels
            size = 300
            label = f"BFS\n{z}"

        # 2. The Hoodlums (121-136)
        elif 121 <= z <= 136:
            color = c_hoodlums
            size = 200
            label = str(z)
            if z == 126:  # UTAHIUM (The Leader of the Hoodlums)
                color = c_utah
                size = 600
                label = "UTAH\n126"

        # 3. Utah Intelligence Agency (137)
        elif z == 137:
            color = c_uia
            size = 400
            label = "UIA\n137"

        # 4. Utah Occult Agency (173)
        elif z == 173:
            color = c_uoa
            size = 400
            label = "UOA\n173"

        colors.append(color)
        sizes.append(size)
        labels.append(label)

    # --- PLOTTING ---
    # Convert polar to cartesian
    x = [r * np.cos(t) for r, t in zip(radii, thetas)]
    y = [r * np.sin(t) for r, t in zip(radii, thetas)]

    # Draw the Spiral Path (The Cord of Life)
    ax.plot(x, y, color='#333', linewidth=1, alpha=0.5)

    # Draw the Elements
    ax.scatter(x, y, s=sizes, c=colors, edgecolors='white', linewidth=1.5, zorder=10)

    # Add Text Labels
    for i, txt in enumerate(labels):
        if sizes[i] > 150:  # Only label the big agencies and key nodes
            ax.text(x[i], y[i], txt, color='white', fontsize=8, ha='center', va='center', fontweight='bold')
        elif i < 118 and i % 5 == 0:  # Sparse labeling for old world
            ax.text(x[i], y[i], str(i + 1), color='#888', fontsize=6, ha='center', va='center')

    # --- DECORATIONS ---
    # Central Title
    ax.text(0, 0, "UTAH'S\nSWIRLD", color='white', fontsize=30, ha='center', va='center', fontweight='bold', alpha=0.1)

    # Agency Legend
    legend_x = -130
    legend_y = 130
    gap = 10

    def draw_legend_item(yy, col, text):
        ax.scatter([legend_x], [yy], c=col, s=200, edgecolors='white')
        ax.text(legend_x + 15, yy, text, color='white', fontsize=12, va='center')

    draw_legend_item(legend_y, c_squirrels, "Bella's Flying Squirrels (119-120)")
    draw_legend_item(legend_y - gap, c_hoodlums, "The Hoodlums (121-136)")
    draw_legend_item(legend_y - gap * 2, c_utah, "THE ANCHOR (Utahium - 126)")
    draw_legend_item(legend_y - gap * 3, c_uia, "Utah Intel Agency (137)")
    draw_legend_item(legend_y - gap * 4, c_uoa, "Utah Occult Agency (173)")

    ax.axis('off')
    plt.tight_layout()
    plt.savefig(OUTPUT_FILENAME, dpi=DPI, facecolor='#050505')
    print(f"Manifested: {OUTPUT_FILENAME}")


if __name__ == "__main__":
    generate_swirld()
