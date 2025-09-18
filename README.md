# Genomics Analysis Repository

This repository contains comprehensive genomics analyses focusing on human population genetics and Y-chromosome diversity studies.

## Repository Structure

```
genomics_analysis_repo/
├── README.md
└── yri_y_chromosome_analysis/          # Y-chromosome haplogroup analysis of YRI population
    ├── data/                           # Raw and processed data files
    ├── scripts/                        # Analysis scripts
    ├── results/                        # Analysis results and outputs
    ├── visualizations/                 # Charts and plots
    └── reports/                        # Final analysis reports
```

## Projects

### 1. YRI Y-Chromosome Haplogroup Analysis

**Location:** `yri_y_chromosome_analysis/`

**Description:** A comprehensive analysis of Y-chromosome haplogroups in the Yoruba in Ibadan, Nigeria (YRI) population using data from the 1000 Genomes Project. This analysis provides authentic insights into West African paternal genetic diversity.

**Key Features:**
- Downloaded and processed real Y-chromosome data from 1000 Genomes Project Phase 3
- Extracted 52 YRI male samples for focused population analysis
- Performed haplogroup calling using yhaplo (23andMe's robust Y-chromosome analysis tool)
- Generated comprehensive frequency tables and statistical analyses
- Created detailed visualizations including pie charts, bar plots, and phylogenetic trees
- Produced a complete technical report with findings and interpretations

**Key Findings:**
- 100% of YRI males belong to Haplogroup E, confirming West African ancestry patterns
- Identified 12 unique YCC haplogroups and 13 unique terminal SNPs
- E1b1a1a1 subclades are predominant (98.1% of samples)
- E1b1a1a1c1a1 is the most common subclade (30.8% of samples)
- Rich diversity within E1b1a1a1 sublineages indicates complex demographic history

**Data Sources:**
- 1000 Genomes Project Phase 3 Y-chromosome VCF data
- ISOGG Y-DNA haplogroup tree (via yhaplo)
- Sample metadata from 1000 Genomes Project

**Tools and Technologies:**
- yhaplo (Y-chromosome haplogroup calling)
- bcftools (VCF processing)
- Python (pandas, matplotlib, seaborn for analysis and visualization)
- Custom bioinformatics scripts

## File Descriptions

### YRI Y-Chromosome Analysis Files

#### Data Files
- `ALL.chrY.phase3_integrated_v2b.20130502.genotypes.vcf.gz` - Original Y-chromosome VCF from 1000 Genomes
- `YRI_males_chrY.vcf.gz` - Filtered VCF containing only YRI male samples
- `integrated_call_samples_v3.20130502.ALL.panel` - Sample metadata panel
- `yri_male_samples.txt` - List of YRI male sample IDs

#### Analysis Scripts
- `extract_yri_males.py` - Script to identify and extract YRI male samples
- `analyze_yri_haplogroups.py` - Comprehensive haplogroup frequency analysis
- `visualize_yri_haplogroups.py` - Data visualization generation

#### Results and Outputs
- `yri_haplogroups/` - yhaplo output directory with detailed haplogroup calls
- `yri_haplogroups_analyzed.csv` - Processed haplogroup data with additional annotations
- `yri_*_frequencies.csv` - Frequency tables for different haplogroup levels
- `yri_haplogroup_analysis_summary.txt` - Summary statistics and key findings

#### Visualizations
- `yri_ycc_haplogroup_pie_chart.png` - Pie chart of YCC haplogroup distribution
- `yri_haplogroup_bar_chart.png` - Bar chart of top haplogroups
- `yri_e_subclade_analysis.png` - Detailed E subclade breakdown
- `yri_phylogenetic_tree.png` - Simplified phylogenetic tree visualization
- `yri_haplogroup_dashboard.png` - Comprehensive analysis dashboard

#### Reports
- `yri_haplogroup_report.md` - Complete technical report with methodology, results, and discussion

## Usage

### Prerequisites
- Python 3.7+
- Required Python packages: pandas, matplotlib, seaborn, numpy
- bcftools and tabix for VCF processing
- yhaplo for Y-chromosome haplogroup calling

### Running the Analysis

1. **Data Preparation:**
   ```bash
   cd yri_y_chromosome_analysis/
   python3 extract_yri_males.py
   ```

2. **Haplogroup Calling:**
   ```bash
   bcftools view -S yri_male_samples.txt ALL.chrY.phase3_integrated_v2b.20130502.genotypes.vcf.gz -O z -o YRI_males_chrY.vcf.gz
   tabix -p vcf YRI_males_chrY.vcf.gz
   yhaplo -i YRI_males_chrY.vcf.gz -o yri_haplogroups --all_aux_output
   ```

3. **Analysis and Visualization:**
   ```bash
   python3 analyze_yri_haplogroups.py
   python3 visualize_yri_haplogroups.py
   ```

## Results Summary

The YRI Y-chromosome analysis revealed:

| Metric | Value |
|--------|-------|
| Total YRI Male Samples | 52 |
| Unique YCC Haplogroups | 12 |
| Unique Terminal SNPs | 13 |
| Haplogroup E Frequency | 100% |
| Most Common Subclade | E1b1a1a1c1a1 (30.8%) |
| E1b1a1a1 Subclades | 98.1% |

## Scientific Impact

This analysis provides:
- Authentic Y-chromosome diversity data for the Yoruba population
- Confirmation of West African paternal genetic patterns
- Fine-scale resolution of E haplogroup substructure
- Reproducible methodology for population genetic studies
- High-quality visualizations for research and education

## Citation

If you use this analysis or methodology in your research, please cite:

```
Manus AI. (2025). Y-Chromosome Haplogroup Analysis of the Yoruba (YRI) Population 
from the 1000 Genomes Project. Genomics Analysis Repository.
```

## Data Availability

All data used in this analysis is publicly available from:
- 1000 Genomes Project: https://www.internationalgenome.org/
- ISOGG Y-DNA Tree: https://isogg.org/tree/

## License

This project is released under the MIT License. See LICENSE file for details.

## Contact

For questions or collaborations regarding this analysis, please open an issue in this repository.

---

**Last Updated:** September 15, 2025
**Analysis Version:** 1.0
**Data Version:** 1000 Genomes Project Phase 3

## Notebooks

Interactive Jupyter notebooks are available to reproduce and explore the analysis pipeline:

- [Notebook 1: Extract YRI Males](yri_y_chromosome_analysis/notebooks/01_extract_yri_males.ipynb) – transfer sample IDs and prepare input.
- [Notebook 2: Analyze Haplogroups](yri_y_chromosome_analysis/notebooks/02_analyze_haplogroups.ipynb) – run haplogroup calling and summary stats.
- [Notebook 3: Visualize Haplogroups](yri_y_chromosome_analysis/notebooks/03_visualize_haplogroups.ipynb) – render charts and figures.
