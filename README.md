
# Molecular Characterisation of the *Plasmodium falciparum dhfr* Gene in Clinical Isolates from Ifo, Ogun State, Nigeria

## Project Overview

This repository contains bioinformatics scripts and supporting information for the molecular characterisation of the *Plasmodium falciparum dihydrofolate reductase* (*Pfdhfr*) gene in five clinical isolates obtained from symptomatic malaria patients in Ifo Local Government Area, Ogun State, southwestern Nigeria.

The study investigated sequence variation in *Pfdhfr*, a molecular marker associated with antifolate antimalarial drug resistance, and examined the genetic relationships between the Nigerian isolates and published global *Pfdhfr* sequences.

The project combines Sanger sequence analysis, reference-based variant identification, multiple sequence alignment, and phylogenetic analysis to characterise mutations in the target gene.

## Research Objectives

1. To obtain and analyse *Pfdhfr* consensus sequences from five clinical isolates.
2. To identify nucleotide substitutions and corresponding amino acid changes in the gene.
3. To characterise the observed mutation profile in relation to the *P. falciparum* 3D7 reference sequence.
4. To compare the Nigerian sequences with published global *Pfdhfr* sequences.
5. To investigate sequence-based genetic relationships among the study isolates and global reference sequences.

## Key Molecular Findings

All five clinical isolates carried the same triple-mutant *Pfdhfr* profile:

| Nucleotide substitution | Amino acid substitution |
|---|---|
| A152T | N51I |
| T175C | C59R |
| G323A | S108N |

These substitutions correspond to the N51I, C59R and S108N mutations commonly investigated in relation to pyrimethamine resistance.

Nucleotide positions are reported relative to the reference sequence, *P. falciparum* 3D7 (*XM_001351443.1*).

## Study Dataset

- Clinical isolates: 5
- Study location: Ifo Local Government Area, Ogun State, Nigeria
- Target gene: *Pfdhfr*
- Reference sequence: *P. falciparum* 3D7 (XM_001351443.1)
- Global comparative dataset: 29 sequences, comprising five study isolates, 23 published sequences and one 3D7 reference sequence.
- Multiple sequence alignment: MAFFT
- Phylogenetic analysis: IQ-TREE

## Bioinformatics Workflow

The analysis involved the following major stages:

1. **Sanger sequencing data processing:** Examination and processing of forward and reverse chromatogram files.
2. **Consensus sequence generation:** Preparation of consensus sequences for the five clinical isolates.
3. **Reference-based analysis:** Comparison of the consensus sequences against the 3D7 reference sequence.
4. **Variant identification:** Identification of nucleotide substitutions and their corresponding amino acid changes.
5. **Multiple sequence alignment:** Alignment of study sequences and published global sequences using MAFFT.
6. **Phylogenetic analysis:** Reconstruction of phylogenetic relationships using IQ-TREE.
7. **Visualisation:** Generation and examination of chromatograms and phylogenetic outputs.

## Repository Structure

```text
Pfdhfr-Molecular-Analysis/
│
├── README.md
│
├── scripts/
│   └── make_pfdhfr_chromatograms_fixed.py
│
└── archive/
    └── make_pfdhfr_chromatograms.py
```

### Scripts

- `scripts/make_pfdhfr_chromatograms_fixed.py`: Script for generating annotated Sanger sequencing chromatograms.
- `archive/make_pfdhfr_chromatograms.py`: Earlier version of the chromatogram-generation script, retained for reference.

## Software and Tools

The broader analysis involved the following bioinformatics tools:

- Biopython
- FastQC
- SeqKit
- CAP3
- BWA-MEM
- SAMtools
- BCFtools
- MAFFT
- IQ-TREE
- iTOL

The specific software versions and installation instructions will be documented alongside the corresponding workflow components.

## Reproducibility

This repository is intended to support transparency and reproducibility of the molecular analysis.

Scripts, workflow documentation, and selected analysis outputs will be made available as the repository is developed.

Raw sequence files and clinical metadata are not included in this initial repository release.

## Research Significance

Characterising mutations in the *Pfdhfr* gene contributes to understanding the molecular epidemiology of antifolate-associated resistance in *P. falciparum*.

The comparison of local clinical isolates with published global sequences provides additional context for examining the distribution and sequence-based relationships of *Pfdhfr* variants.

## Author

**Samuel Adeniyi Oyegbade**

Research interests: Molecular parasitology, malaria genomics, antimalarial drug resistance, and bioinformatics.

GitHub: [@oyegbadesam-pixel](https://github.com/oyegbadesam-pixel)

## Repository

[https://github.com/oyegbadesam-pixel/Pfdhfr-Molecular-Analysis](https://github.com/oyegbadesam-pixel/Pfdhfr-Molecular-Analysis)
