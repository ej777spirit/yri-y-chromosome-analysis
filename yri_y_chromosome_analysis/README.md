# YRI Y-Chromosome Haplogroup Analysis

This directory contains a comprehensive analysis of Y-chromosome haplogroups in the Yoruba in Ibadan, Nigeria (YRI) population using authentic data from the 1000 Genomes Project.

## Overview

This analysis provides detailed insights into the paternal genetic diversity of the YRI population, revealing the distribution and frequency of Y-chromosome haplogroups and their subclades. The study confirms the predominance of Haplogroup E in West African populations and provides fine-scale resolution of E subclade diversity.

## Directory Structure

```
yri_y_chromosome_analysis/
├── README.md                           # This file
├── data/                              # Raw and processed data files
│   ├── ALL.chrY.phase3_integrated_v2b.20130502.genotypes.vcf.gz  # Original Y-chr VCF
│   ├── YRI_males_chrY.vcf.gz          # Filtered VCF for YRI males
│   ├── integrated_call_samples_v3.20130502.ALL.panel  # Sample metadata
│   ├── yri_male_samples.txt           # List of YRI male sample IDs
│   └── yri_haplogroup_analysis_summary.txt  # Summary statistics
├── scripts/                           # Analysis scripts
│   ├── extract_yri_males.py           # Extract YRI male samples
│   ├── analyze_yri_haplogroups.py     # Frequency analysis
│   └── visualize_yri_haplogroups.py   # Generate visualizations
├── results/                           # Analysis outputs
│   ├── yri_haplogroups/               # yhaplo output directory
│   ├── yri_haplogroups_analyzed.csv   # Processed haplogroup data
│   ├── yri_*_frequencies.csv          # Frequency tables
│   └── ...
├── visualizations/                    # Charts and plots
│   ├── yri_haplogroup_dashboard.png   # Comprehensive dashboard
│   ├── yri_ycc_haplogroup_pie_chart.png  # Pie chart
│   ├── yri_haplogroup_bar_chart.png   # Bar chart
│   ├── yri_phylogenetic_tree.png      # Phylogenetic tree
│   └── yri_e_subclade_analysis.png    # E subclade breakdown
├── reports/                           # Final reports
│   └── yri_haplogroup_report.md       # Complete technical report
└── yhaplo/                           # yhaplo tool installation
```

## Key Findings

- **Total Samples:** 52 YRI male individuals
- **Haplogroup E Frequency:** 100% (all samples belong to Haplogroup E)
- **Unique YCC Haplogroups:** 12 distinct haplogroups identified
- **Unique Terminal SNPs:** 13 different terminal SNPs
- **Most Common Subclade:** E1b1a1a1c1a1 (30.8% of samples)
- **E1b1a1a1 Dominance:** 98.1% of samples belong to E1b1a1a1 subclades

## Methodology

1. **Data Acquisition:** Downloaded Y-chromosome VCF and sample metadata from 1000 Genomes Project
2. **Sample Selection:** Identified and extracted 52 YRI male samples
3. **Haplogroup Calling:** Used yhaplo tool with ISOGG Y-DNA tree for accurate classification
4. **Statistical Analysis:** Generated comprehensive frequency tables and diversity metrics
5. **Visualization:** Created multiple chart types to illustrate haplogroup distribution
6. **Reporting:** Compiled findings into detailed technical report

## Tools and Dependencies

- **yhaplo:** Y-chromosome haplogroup calling (23andMe)
- **bcftools:** VCF file processing
- **tabix:** VCF indexing
- **Python 3.7+** with packages:
  - pandas (data analysis)
  - matplotlib (plotting)
  - seaborn (statistical visualization)
  - numpy (numerical computing)

## Usage

### Quick Start

1. Navigate to the analysis directory:
   ```bash
   cd yri_y_chromosome_analysis/
   ```

2. Run the complete analysis pipeline:
   ```bash
   # Extract YRI samples
   python3 scripts/extract_yri_males.py
   
   # Filter VCF for YRI males
   bcftools view -S data/yri_male_samples.txt data/ALL.chrY.phase3_integrated_v2b.20130502.genotypes.vcf.gz -O z -o data/YRI_males_chrY.vcf.gz
   
   # Index VCF
   tabix -p vcf data/YRI_males_chrY.vcf.gz
   
   # Call haplogroups
   yhaplo -i data/YRI_males_chrY.vcf.gz -o results/yri_haplogroups --all_aux_output
   
   # Analyze results
   python3 scripts/analyze_yri_haplogroups.py
   
   # Generate visualizations
   python3 scripts/visualize_yri_haplogroups.py
   ```

### Individual Steps

Each script can be run independently:

- **Extract YRI samples:** `python3 scripts/extract_yri_males.py`
- **Analyze haplogroups:** `python3 scripts/analyze_yri_haplogroups.py`
- **Create visualizations:** `python3 scripts/visualize_yri_haplogroups.py`

## Results Files

### Data Tables
- `yri_major_haplogroup_frequencies.csv` - Major haplogroup frequencies
- `yri_ycc_haplogroup_frequencies.csv` - YCC haplogroup frequencies
- `yri_terminal_snp_frequencies.csv` - Terminal SNP frequencies
- `yri_e_subclade_l1_frequencies.csv` - E subclade level 1 frequencies
- `yri_e_subclade_l2_frequencies.csv` - E subclade level 2 frequencies

### Visualizations
- `yri_haplogroup_dashboard.png` - Comprehensive analysis dashboard
- `yri_ycc_haplogroup_pie_chart.png` - YCC haplogroup distribution pie chart
- `yri_haplogroup_bar_chart.png` - Top haplogroups bar chart
- `yri_phylogenetic_tree.png` - Simplified phylogenetic tree
- `yri_e_subclade_analysis.png` - Detailed E subclade analysis

### Reports
- `yri_haplogroup_report.md` - Complete technical report with methodology, results, and discussion

## Scientific Significance

This analysis provides:

1. **Authentic Data:** Uses real genomic data from a well-established international project
2. **Population Specificity:** Focuses on YRI population for targeted insights
3. **Fine-scale Resolution:** Identifies specific subclades within major haplogroups
4. **Reproducible Methods:** All scripts and methodology are documented and shareable
5. **Comprehensive Visualization:** Multiple chart types for different analytical perspectives

## Data Sources

- **1000 Genomes Project Phase 3:** Y-chromosome VCF data
- **ISOGG Y-DNA Tree:** Haplogroup classification system (via yhaplo)
- **Sample Metadata:** Population and demographic information

## Citation

If you use this analysis in your research, please cite:

```
Manus AI. (2025). Y-Chromosome Haplogroup Analysis of the Yoruba (YRI) Population 
from the 1000 Genomes Project. Genomics Analysis Repository.
```

## License

This analysis is released under the MIT License. Data from the 1000 Genomes Project is publicly available under their terms of use.

---

**Analysis Date:** September 15, 2025  
**Data Version:** 1000 Genomes Project Phase 3  
**Tool Versions:** yhaplo 2.1.14, bcftools 1.13

## Notebooks

Interactive Jupyter notebooks are available to reproduce and explore the analysis pipeline:

- [Notebook 1: Extract YRI Males](../yri_y_chromosome_analysis/notebooks/01_extract_yri_males.ipynb) – transfer sample IDs and prepare input.
- [Notebook 2: Analyze Haplogroups](../yri_y_chromosome_analysis/notebooks/02_analyze_haplogroups.ipynb) – run haplogroup calling and summary stats.
- [Notebook 3: Visualize Haplogroups](../yri_y_chromosome_analysis/notebooks/03_visualize_haplogroups.ipynb) – render charts and figures.
