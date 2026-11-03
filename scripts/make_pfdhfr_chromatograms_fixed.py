from pathlib import Path
import matplotlib.pyplot as plt
from sanger import Chromatogram

outdir = Path("chromatogram_figures_fixed")
outdir.mkdir(exist_ok=True)

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

for sample, data in samples.items():

    cg = Chromatogram.from_abi(data["file"])

    # Actual chromatogram peak coordinates
    peaks = cg.record.annotations["peak positions"]

    for cf_location, aa_change, nuc_change, ref_base, sample_base in data["sites"]:

        # CfLocation is 1-based; Python list is 0-based
        peak_index = cf_location - 1

        if peak_index >= len(peaks):
            print(f"WARNING: {sample} {nuc_change}: peak not found")
            continue

        actual_peak = peaks[peak_index]

        # Plot around the base position
        start = max(1, cf_location - 12)
        end = min(cg.length, cf_location + 12)

        fig, ax = cg.plot(region=(start, end))

        # Correct marker: use actual chromatogram peak coordinate
        ax.axvline(
            actual_peak,
            linestyle="--",
            linewidth=1.5
        )

        # Mutation annotation
        ax.text(
            actual_peak,
            0.88,
            f"{ref_base} → {sample_base}",
            transform=ax.get_xaxis_transform(),
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold"
        )

        ax.set_title(
            f"{sample}  |  {aa_change} ({nuc_change})",
            fontsize=13,
            fontweight="bold"
        )

        fig.tight_layout()

        outfile = outdir / f"{sample}_{nuc_change}.png"
        fig.savefig(
            outfile,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close(fig)

        print(
            f"{sample} {nuc_change}: "
            f"CfLocation={cf_location}, "
            f"peak={actual_peak}, "
            f"saved={outfile}"
        )

print("\nAll corrected chromatograms created.")
