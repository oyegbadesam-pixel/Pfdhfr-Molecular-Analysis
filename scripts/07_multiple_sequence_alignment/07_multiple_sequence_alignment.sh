#!/bin/bash

# ============================================================
# Analysis: Multiple sequence alignment
# Software: MAFFT
# ============================================================

# Accept input and optional output filenames
INPUT="${1:?Usage: bash 07_multiple_sequence_alignment.sh <input.fasta> [output.fasta]}"
OUTPUT="${2:-pfdhfr_aligned.fasta}"

# Check that the input file exists
if [[ ! -f "$INPUT" ]]; then
    echo "Error: Input file not found: $INPUT"
    exit 1
fi

# Perform multiple sequence alignment
if mafft --auto "$INPUT" > "$OUTPUT"; then
    echo "Multiple sequence alignment completed successfully."
    echo "Output: $OUTPUT"
else
    echo "Error: MAFFT alignment failed."
    exit 1
fi
