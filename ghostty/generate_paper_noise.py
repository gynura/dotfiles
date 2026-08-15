#!/usr/bin/env python3
"""Generate a tileable, subtle "paper grain" texture for Ghostty.

Add the result to your Ghostty config (background-image = paper-noise.png)
with background-image-opacity ~0.06, fit = none, repeat = true.

Rerun after tweaking the tunables below:
    python3 ghostty/generate_paper_noise.py
"""

import os
import random
import struct
import zlib

# --- Tunables ---------------------------------------------------------------
OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "paper-noise.png"
)
SIZE = 512                # texture size in pixels (square). Bigger = smoother on HiDPI.
BASE = 128                # center gray (128 = neutral, works over any theme).
AMPLITUDE = 26            # grain contrast: max deviation from BASE (1-127). Lower = subtler.
OCTAVE_GRIDS = (4, 8, 16) # value-noise grid sizes per octave. Smaller = coarser fibers.
SEED = 7                  # change to get a different grain pattern.
# ----------------------------------------------------------------------------

def make_cell(rng, grid):
    return [[rng.uniform(0.0, 1.0) for _ in range(grid + 1)] for _ in range(grid + 1)]


def octave_value(x, y, grid, cell):
    # wrapped (tileable) value noise in [0,1]
    fx = x * grid / SIZE
    fy = y * grid / SIZE
    i = int(fx) % grid
    j = int(fy) % grid
    u = fx - i
    v = fy - j
    u = u * u * (3.0 - 2.0 * u)
    v = v * v * (3.0 - 2.0 * v)
    g00 = cell[j][i]
    g10 = cell[j][(i + 1) % grid]
    g01 = cell[(j + 1) % grid][i]
    g11 = cell[(j + 1) % grid][(i + 1) % grid]
    return g00 + (g10 - g00) * u + (g01 - g00) * v + (g11 - g10 - g01 + g00) * u * v


def make_png():
    rng = random.Random(SEED)
    cells = [make_cell(rng, g) for g in OCTAVE_GRIDS]
    weights = [1.0 / (i + 1) for i in range(len(OCTAVE_GRIDS))]
    total_weight = sum(weights)

    rows = []
    for y in range(SIZE):
        row = bytearray()
        for x in range(SIZE):
            value = 0.0
            for cell, grid, weight in zip(cells, OCTAVE_GRIDS, weights):
                value += octave_value(x, y, grid, cell) * weight
            value /= total_weight
            gray = int(BASE + (value - 0.5) * 2.0 * AMPLITUDE)
            gray = max(0, min(255, gray))
            row += bytes((gray, gray, gray))
        rows.append(b"\x00" + bytes(row))

    def chunk(kind, data):
        return (
            struct.pack(">I", len(data))
            + kind
            + data
            + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
        )

    ihdr = struct.pack(">IIBBBBB", SIZE, SIZE, 8, 2, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", ihdr)
    png += chunk(b"IDAT", zlib.compress(b"".join(rows), 9))
    png += chunk(b"IEND", b"")
    return png


def main():
    png = make_png()
    with open(OUTPUT_PATH, "wb") as f:
        f.write(png)
    print(f"wrote {OUTPUT_PATH} ({SIZE}x{SIZE}, gray {BASE}+/-{AMPLITUDE})")


if __name__ == "__main__":
    main()
