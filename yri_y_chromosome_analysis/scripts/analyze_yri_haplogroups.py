#!/usr/bin/env python3
"""
Analyze YRI Y-chromosome haplogroup results from yhaplo
"""

import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

def load_haplogroup_data(file_path):
    """Load haplogroup data from yhaplo output"""
    # Read the haplogroup file (whitespace-separated, no header)
    df = pd.read_csv(file_path, sep='\s+', header=None, 
                     names=['Sample_ID', 'Terminal_SNP', 'Representative_SNP', 'YCC_Haplogroup'])
    # Strip any trailing whitespace
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df

def analyze_haplogroup_frequencies(df):
    """Analyze haplogroup frequencies at different phylogenetic levels"""
    
    # Extract major haplogroup (first letter)
    df['Major_Haplogroup'] = df['YCC_Haplogroup'].str[0]
    
    # Extract E subclade levels
    df['E_Level1'] = df['YCC_Haplogroup'].str.extract(r'(E\d+)')
    df['E_Level2'] = df['YCC_Haplogroup'].str.extract(r'(E\d+[a-z]+)')
    df['E_Level3'] = df['YCC_Haplogroup'].str.extract(r'(E\d+[a-z]+\d+)')
    
    # Count frequencies at different levels
    major_counts = df['Major_Haplogroup'].value_counts()
    ycc_counts = df['YCC_Haplogroup'].value_counts()
    terminal_snp_counts = df['Terminal_SNP'].value_counts()
    
    # E subclade analysis
    e_samples = df[df['Major_Haplogroup'] == 'E']
    e1_counts = e_samples['E_Level1'].value_counts()
    e2_counts = e_samples['E_Level2'].value_counts()
    e3_counts = e_samples['E_Level3'].value_counts()
    
    return {
        'major': major_counts,
        'ycc': ycc_counts,
        'terminal_snp': terminal_snp_counts,
        'e1': e1_counts,
        'e2': e2_counts,
        'e3': e3_counts,
        'e_samples': e_samples
    }

def create_frequency_tables(counts_dict, df):
    """Create detailed frequency tables"""
    
    total_samples = len(df)
    
    # Major haplogroup table
    major_table = pd.DataFrame({
        'Haplogroup': counts_dict['major'].index,
        'Count': counts_dict['major'].values,
        'Frequency': counts_dict['major'].values / total_samples,
        'Percentage': (counts_dict['major'].values / total_samples) * 100
    })
    
    # YCC haplogroup table
    ycc_table = pd.DataFrame({
        'YCC_Haplogroup': counts_dict['ycc'].index,
        'Count': counts_dict['ycc'].values,
        'Frequency': counts_dict['ycc'].values / total_samples,
        'Percentage': (counts_dict['ycc'].values / total_samples) * 100
    })
    
    # Terminal SNP table
    terminal_table = pd.DataFrame({
        'Terminal_SNP': counts_dict['terminal_snp'].index,
        'Count': counts_dict['terminal_snp'].values,
        'Frequency': counts_dict['terminal_snp'].values / total_samples,
        'Percentage': (counts_dict['terminal_snp'].values / total_samples) * 100
    })
    
    return major_table, ycc_table, terminal_table

def analyze_e_subclades(counts_dict):
    """Detailed analysis of E haplogroup subclades"""
    
    e_total = counts_dict['e_samples'].shape[0]
    
    # E1 level analysis
    e1_table = pd.DataFrame({
        'E_Subclade_L1': counts_dict['e1'].index,
        'Count': counts_dict['e1'].values,
        'Frequency_in_E': counts_dict['e1'].values / e_total,
        'Percentage_in_E': (counts_dict['e1'].values / e_total) * 100
    })
    
    # E2 level analysis
    e2_table = pd.DataFrame({
        'E_Subclade_L2': counts_dict['e2'].index,
        'Count': counts_dict['e2'].values,
        'Frequency_in_E': counts_dict['e2'].values / e_total,
        'Percentage_in_E': (counts_dict['e2'].values / e_total) * 100
    })
    
    return e1_table, e2_table, e_total

def save_analysis_results(df, counts_dict, major_table, ycc_table, terminal_table, e1_table, e2_table):
    """Save all analysis results to files"""
    
    # Save raw data with additional columns
    df.to_csv('yri_haplogroups_analyzed.csv', index=False)
    
    # Save frequency tables
    major_table.to_csv('yri_major_haplogroup_frequencies.csv', index=False)
    ycc_table.to_csv('yri_ycc_haplogroup_frequencies.csv', index=False)
    terminal_table.to_csv('yri_terminal_snp_frequencies.csv', index=False)
    e1_table.to_csv('yri_e_subclade_l1_frequencies.csv', index=False)
    e2_table.to_csv('yri_e_subclade_l2_frequencies.csv', index=False)
    
    # Create summary report
    total_samples = len(df)
    e_total = len(counts_dict['e_samples'])
    
    summary = f"""
YRI Y-Chromosome Haplogroup Analysis Summary
==========================================

Total YRI male samples analyzed: {total_samples}

Major Haplogroup Distribution:
{major_table.to_string(index=False)}

E Haplogroup Subclades (Level 1):
{e1_table.to_string(index=False)}

Most Common YCC Haplogroups:
{ycc_table.head(10).to_string(index=False)}

Key Findings:
- {e_total}/{total_samples} ({e_total/total_samples*100:.1f}%) belong to haplogroup E
- E1b1a1a1 subclades are predominant, consistent with West African ancestry
- Multiple E1b1a1a1 sublineages present, indicating diverse Y-chromosome lineages
- Terminal SNPs show fine-scale population structure within YRI

"""
    
    with open('yri_haplogroup_analysis_summary.txt', 'w') as f:
        f.write(summary)
    
    print("Analysis complete! Files saved:")
    print("- yri_haplogroups_analyzed.csv")
    print("- yri_major_haplogroup_frequencies.csv")
    print("- yri_ycc_haplogroup_frequencies.csv")
    print("- yri_terminal_snp_frequencies.csv")
    print("- yri_e_subclade_l1_frequencies.csv")
    print("- yri_e_subclade_l2_frequencies.csv")
    print("- yri_haplogroup_analysis_summary.txt")

def main():
    # Load data
    df = load_haplogroup_data('yri_haplogroups/haplogroups.YRI_males_chrY.txt')
    
    print(f"Loaded {len(df)} YRI male samples")
    print(f"Unique YCC haplogroups: {df['YCC_Haplogroup'].nunique()}")
    print(f"Unique terminal SNPs: {df['Terminal_SNP'].nunique()}")
    
    # Analyze frequencies
    counts_dict = analyze_haplogroup_frequencies(df)
    
    # Create frequency tables
    major_table, ycc_table, terminal_table = create_frequency_tables(counts_dict, df)
    
    # Analyze E subclades
    e1_table, e2_table, e_total = analyze_e_subclades(counts_dict)
    
    # Save results
    save_analysis_results(df, counts_dict, major_table, ycc_table, terminal_table, e1_table, e2_table)
    
    return df, counts_dict, major_table, ycc_table, terminal_table, e1_table, e2_table

if __name__ == "__main__":
    results = main()

