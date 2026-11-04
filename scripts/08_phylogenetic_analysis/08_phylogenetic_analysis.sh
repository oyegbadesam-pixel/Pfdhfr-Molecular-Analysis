#!/bin/bash

# ============================================================
# Analysis: Maximum-likelihood phylogenetic reconstruction
# Software: IQ-TREE 3.1.3
# ============================================================

# Accept alignment file as a command-line argument
ALIGNMENT="${1:?Usage: bash 08_phylogenetic_analysis.sh <alignment.fasta>}"

# Check that the input alignment exists
if [[ ! -f "$ALIGNMENT" ]]; then
    echo "Error: Alignment file not found: $ALIGNMENT"
    exit 1
fi

# Run ModelFinder and maximum-likelihood phylogenetic analysis
iqtree3 \
    -s "$ALIGNMENT" \
    -m MFP \
    -B 1000 \
    -alrt 1000 \
    -T AUTO

if [[ $? -eq 0 ]]; then
    echo "Phylogenetic analysis completed successfully."
else
    echo "Error: IQ-TREE analysis failed."
    exit 1
fi
