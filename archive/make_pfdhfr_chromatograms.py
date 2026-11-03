from pathlib import Path
import matplotlib.pyplot as plt
from sanger import Chromatogram

outdir = Path("chromatogram_figures")
outdir.mkdir(exist_ok=True)

# Chromatogram base coordinates obtained from the Sanger alignment TSVs
samples = {
    "IFO-01": {
        "file": "Sample 1F.ab1",
        "sites": [
            (69,  "N51I",  "A152T", "A", "T"),
            (92,  "C59R",  "T175C", "T", "C"),
            (238, "S108N", "G323?", "G", "?"),
        ],
    },
    "IFO-02": {
        "file": "Sample 2F.ab1",
        "sites": [
            (59,  "N51I",  "A152T", "A", "T"),
            (82,  "C59R",  "T175C", "T", "C"),
            (230, "S108N", "G323A", "G", "A"),
        ],
    },
    "IFO-03": {
        "file": "Sample 3F.ab1",
        "sites": [
            (61,  "N51I",  "A152T", "A", "T"),
            (84,  "C59R",  "T175C", "T", "C"),
            (232, "S108N", "G323A", "G", "A"),
        ],
    },
    "IFO-04": {
        "file": "Sample 4F.ab1",
        "sites": [
            (61,  "N51I",  "A152T", "A", "T"),
            (84,  "C59R",  "T175C", "T", "C"),
            (232, "S108N", "G323A", "G", "A"),
        ],
    },
    "IFO-05": {
        "file": "Sample 5F.ab1",
        "sites": [
            (62,  "N51I",  "A152T", "A", "T"),
            (85,  "C59R",  "T175C", "T", "C"),
            (233, "S108N", "G323A", "G", "A"),
        ],
    },
}

# Store individual panels
all_figures = []

for sample, data in samples.items():

    cg = Chromatogram.from_abi(data["file"])

    for peak, aa_change, nuc_change, ref_base, sample_base in data["sites"]:

        start = max(1, peak - 12)
        end = min(cg.length, peak + 12)

        fig, ax = cg.plot(region=(start, end))

        ax.axvline(
            peak,
            linestyle="--",
            linewidth=1.5
        )

        ax.set_title(
            f"{sample}  |  {aa_change} ({nuc_change})",
            fontsize=12,
            fontweight="bold"
        )

        ax.text(
            peak,
            ax.get_ylim()[1] * 0.88,
            f"{ref_base} → {sample_base}",
            ha="center",
            va="center",
            fontsize=11,
            fontweight="bold"
        )

        fig.tight_layout()

        outfile = outdir / f"{sample}_{nuc_change}.png"
        fig.savefig(outfile, dpi=300, bbox_inches="tight")
        plt.close(fig)

        print(f"Created: {outfile}")

print("\nDone.")
