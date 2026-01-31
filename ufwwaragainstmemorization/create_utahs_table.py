import math


def create_utah_helix_svg():
    filename = "Utahs_Table_of_Elements.svg"
    width, height = 1200, 1200
    cx, cy = width / 2, height / 2

    # Colors for Orbital Blocks (s, p, d, f, g)
    colors = {
        's': '#FF6B6B',  # Red (Alkali)
        'p': '#FECA57',  # Yellow
        'd': '#54A0FF',  # Blue
        'f': '#5F27CD',  # Purple
        'g': '#00D2D3'  # Cyan (The Utah Block)
    }

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="background-color:#1a1a1a; font-family: Helvetica, Arial, sans-serif;">']

    # Title
    svg.append(
        f'<text x="{cx}" y="60" text-anchor="middle" fill="white" font-size="36" font-weight="bold" letter-spacing="4">UTAH\'S TABLE OF ELEMENTS</text>')
    svg.append(
        f'<text x="{cx}" y="100" text-anchor="middle" fill="#888" font-size="14">THE RADIAL HARMONIC MODEL (TIMELINE OMEGA)</text>')

    # Legend
    legend_y = 1100
    keys = [('s-block', colors['s']), ('p-block', colors['p']), ('d-block', colors['d']), ('f-block', colors['f']),
            ('g-block (UFW)', colors['g'])]
    for i, (name, col) in enumerate(keys):
        lx = 300 + i * 140
        svg.append(f'<rect x="{lx}" y="{legend_y}" width="20" height="20" fill="{col}" />')
        svg.append(f'<text x="{lx + 30}" y="{legend_y + 15}" fill="white" font-size="12">{name}</text>')

    # --- ELEMENT GENERATION LOGIC ---
    # We will spiral out.
    # Logic: Radius increases with Period. Angle depends on Group.

    elements = []

    # Simple dataset for visual representation
    # (Atomic Number, Symbol, Block, Period)
    # Period 1
    elements.append((1, "H", 's', 1, 0))
    elements.append((2, "He", 's', 1, 180))  # He is special

    # Period 2 & 3 (s + p)
    for p in [2, 3]:
        for i in range(2): elements.append((0, "", 's', p, 0))  # Placeholder generation for visual spiral
        for i in range(6): elements.append((0, "", 'p', p, 0))

    # Real Loop to generate visual nodes based on spiraling count
    # We simulate the expansion.

    # Radii for periods
    radii = [0, 80, 140, 200, 280, 360, 440, 520, 600]

    # Draw Concentric Guide Rings (The Shells)
    for r in radii[1:]:
        svg.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#333" stroke-width="1" stroke-dasharray="5,5" />')

    # Function to plot element
    def plot_element(z, symbol, block, period, angle_deg, is_special=False):
        r = radii[period]
        rad = math.radians(angle_deg - 90)  # -90 to start at top
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)

        col = colors[block]
        radius = 18 if period < 8 else 22  # Bigger for G-block

        # Glow for Utahium
        glow = ""
        if symbol == "Ut":
            glow = f'<circle cx="{x}" cy="{y}" r="{radius + 10}" fill="none" stroke="#00D2D3" stroke-width="4" opacity="0.6"><animate attributeName="r" values="{radius + 5};{radius + 15};{radius + 5}" dur="3s" repeatCount="indefinite" /></circle>'
            col = "#00D2D3"

        # Draw Circle
        svg.append(glow)
        svg.append(
            f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{col}" stroke="white" stroke-width="{2 if is_special else 1}" />')

        # Text
        fs_sym = 14 if len(symbol) < 3 else 10
        svg.append(
            f'<text x="{x}" y="{y + 5}" text-anchor="middle" fill="#1a1a1a" font-size="{fs_sym}" font-weight="bold">{symbol}</text>')
        svg.append(f'<text x="{x}" y="{y - 8}" text-anchor="middle" fill="#1a1a1a" font-size="8">{z}</text>')

        # UFW Labels
        if is_special:
            tx = x + (40 if x > cx else -40)
            ty = y + (40 if y > cy else -40)
            svg.append(f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="white" stroke-width="1" />')
            svg.append(
                f'<text x="{tx}" y="{ty}" text-anchor="middle" fill="white" font-size="12" font-weight="bold">{symbol} - {z}</text>')

    # --- MANUAL PLOTTING FOR PRECISION (The "Utah" Design) ---
    # Central Anchor
    plot_element(1, "H", 's', 1, 0)
    plot_element(2, "He", 's', 1, 180)

    # Period 2 (Li - Ne) - 8 elements
    for i in range(8):
        plot_element(3 + i, ["Li", "Be", "B", "C", "N", "O", "F", "Ne"][i], 's' if i < 2 else 'p', 2, i * (360 / 8))

    # Period 3 (Na - Ar) - 8 elements
    for i in range(8):
        plot_element(11 + i, ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"][i], 's' if i < 2 else 'p', 3,
                     i * (360 / 8) + 15)

    # Period 4 (K - Kr) - 18 elements
    for i in range(18):
        blk = 's' if i < 2 else ('d' if i < 12 else 'p')
        plot_element(19 + i, str(19 + i), blk, 4, i * (360 / 18))

    # Period 5 (Rb - Xe) - 18 elements
    for i in range(18):
        blk = 's' if i < 2 else ('d' if i < 12 else 'p')
        plot_element(37 + i, str(37 + i), blk, 5, i * (360 / 18) + 10)

    # Period 6 (Cs - Rn) - 32 elements (Introducing f-block)
    for i in range(32):
        # Simplified block logic for visual spiral
        if i < 2:
            blk = 's'
        elif i < 16:
            blk = 'f'
        elif i < 26:
            blk = 'd'
        else:
            blk = 'p'
        plot_element(55 + i, str(55 + i), blk, 6, i * (360 / 32))

    # Period 7 (Fr - Og) - 32 elements
    for i in range(32):
        if i < 2:
            blk = 's'
        elif i < 16:
            blk = 'f'
        elif i < 26:
            blk = 'd'
        else:
            blk = 'p'
        sym = str(87 + i)
        if sym == "118": sym = "Og"
        plot_element(87 + i, sym, blk, 7, i * (360 / 32) + 5)

    # --- PERIOD 8 (THE UTAH BLOCK) ---
    # This is the outer ring. The G-Block.
    # 50 Elements (2s + 18g + 14f + 10d + 6p)

    # 119 Ufw-Alpha
    plot_element(119, "Ufw-I", 's', 8, 0, True)

    # 120 Ubn
    plot_element(120, "Ubn", 's', 8, 7.2)

    # THE G-BLOCK (121 - 138)
    for i in range(18):
        z = 121 + i
        sym = str(z)
        special = False

        # UTAHIUM
        if z == 126:
            sym = "Ut"
            special = True

        # UFW-LIMITLESS
        if z == 137:
            sym = "Ufw-L"
            special = True

        plot_element(z, sym, 'g', 8, 14.4 + (i * 7.2), special)

    # Rest of Period 8 (simulated)
    for i in range(12):
        plot_element(139 + i, "", 'f', 8, 150 + (i * 6))

    # UFW-VOID (173) - Far future connection
    plot_element(173, "Ufw-V", 's', 8, 300, True)

    svg.append('</svg>')

    with open(filename, "w") as f:
        f.write("".join(svg))
    print(f"Manifested: {filename}")


if __name__ == "__main__":
    create_utah_helix_svg()
