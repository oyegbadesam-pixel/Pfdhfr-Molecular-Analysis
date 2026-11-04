#!/bin/bash

# ============================================================
# Analysis: Reference sequence comparison using BLAST
# Software: NCBI BLAST+
# ============================================================

# Accept query, reference and optional output filenames
QUERY="${1:?Usage: bash 05_reference_sequence_comparison.sh <query.fasta> <reference.fasta> [output.tsv]}"
REFERENCE="${2:?Usage: bash 05_reference_sequence_comparison.sh <query.fasta> <reference.fasta> [output.tsv]}"
OUTPUT="${3:-blastn_results.tsv}"

# Check that BLAST+ is installed
if ! command -v blastn >/dev/null 2>&1; then
    echo "Error: BLAST+ is not installed or blastn is not in PATH."
    exit 1
fi

# Check that input files exist
if [[ ! -f "$QUERY" ]]; then
    echo "Error: Query file not found: $QUERY"
    exit 1
fi

if [[ ! -f "$REFERENCE" ]]; then
    echo "Error: Reference file not found: $REFERENCE"
    exit 1
fi

# Perform nucleotide sequence comparison
if blastn \
    -query "$QUERY" \
    -subject "$REFERENCE" \
    -out "$OUTPUT" \
    -outfmt "6 qseqid sseqid pident length qstart qend sstart send evalue bitscore"; then

    echo "BLAST sequence comparison completed successfully."
    echo "Output: $OUTPUT"

else
    echo "Error: BLAST sequence comparison failed."
    exit 1
fi
