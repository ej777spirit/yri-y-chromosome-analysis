#!/usr/bin/env python3
"""
Create visualizations for YRI Y-chromosome haplogroup analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Wedge
import matplotlib.patches as mpatches

# Set style and color palette
plt.style.use('default')
sns.set_palette("husl")

def load_analysis_data():
    """Load the analyzed haplogroup data"""
    df = pd.read_csv('yri_haplogroups_analyzed.csv')
    major_freq = pd.read_csv('yri_major_haplogroup_frequencies.csv')
    ycc_freq = pd.read_csv('yri_ycc_haplogroup_frequencies.csv')
    terminal_freq = pd.read_csv('yri_terminal_snp_frequencies.csv')
    e1_freq = pd.read_csv('yri_e_subclade_l1_frequencies.csv')
    e2_freq = pd.read_csv('yri_e_subclade_l2_frequencies.csv')
    
    return df, major_freq, ycc_freq, terminal_freq, e1_freq, e2_freq

def create_ycc_haplogroup_pie_chart(ycc_freq):
    """Create pie chart of YCC haplogroup distribution"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Use top 8 haplogroups and group others
    top_hgs = ycc_freq.head(8)
    others_count = ycc_freq.iloc[8:]['Count'].sum() if len(ycc_freq) > 8 else 0
    
    if others_count > 0:
        labels = list(top_hgs['YCC_Haplogroup']) + ['Others']
        sizes = list(top_hgs['Count']) + [others_count]
    else:
        labels = list(top_hgs['YCC_Haplogroup'])
        sizes = list(top_hgs['Count'])
    
    # Create color palette
    colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))
    
    # Create pie chart
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', 
                                      startangle=90, colors=colors,
                                      textprops={'fontsize': 10})
    
    # Enhance text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title('YRI Y-Chromosome Haplogroup Distribution\n(n=52 males)', 
                 fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('yri_ycc_haplogroup_pie_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_haplogroup_bar_chart(ycc_freq):
    """Create horizontal bar chart of haplogroup frequencies"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Sort by count and take top 10
    top_hgs = ycc_freq.head(10)
    
    # Create horizontal bar chart
    bars = ax.barh(range(len(top_hgs)), top_hgs['Count'], 
                   color=plt.cm.viridis(np.linspace(0, 1, len(top_hgs))))
    
    # Customize
    ax.set_yticks(range(len(top_hgs)))
    ax.set_yticklabels(top_hgs['YCC_Haplogroup'])
    ax.set_xlabel('Number of Individuals', fontsize=12, fontweight='bold')
    ax.set_ylabel('Y-Chromosome Haplogroup', fontsize=12, fontweight='bold')
    ax.set_title('Top 10 Y-Chromosome Haplogroups in YRI Population', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Add count labels on bars
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
                f'{int(width)}', ha='left', va='center', fontweight='bold')
    
    # Add percentage labels
    total = top_hgs['Count'].sum()
    for i, (idx, row) in enumerate(top_hgs.iterrows()):
        pct = (row['Count'] / 52) * 100
        ax.text(row['Count']/2, i, f'{pct:.1f}%', 
                ha='center', va='center', color='white', fontweight='bold')
    
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('yri_haplogroup_bar_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_e_subclade_analysis(df):
    """Create detailed analysis of E subclade structure"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # E1 vs E2 distribution
    e_major = df['YCC_Haplogroup'].str.extract(r'(E\d+)')[0].value_counts()
    ax1.pie(e_major.values, labels=e_major.index, autopct='%1.1f%%', 
            startangle=90, colors=['#ff9999', '#66b3ff'])
    ax1.set_title('E1 vs E2 Distribution', fontsize=12, fontweight='bold')
    
    # E1b subclades
    e1b_samples = df[df['YCC_Haplogroup'].str.contains('E1b', na=False)]
    e1b_subclades = e1b_samples['YCC_Haplogroup'].str.extract(r'(E1b\d+[a-z]+\d+[a-z]+\d+)')[0].value_counts()
    
    if len(e1b_subclades) > 0:
        ax2.bar(range(len(e1b_subclades)), e1b_subclades.values, 
                color=plt.cm.plasma(np.linspace(0, 1, len(e1b_subclades))))
        ax2.set_xticks(range(len(e1b_subclades)))
        ax2.set_xticklabels(e1b_subclades.index, rotation=45, ha='right')
        ax2.set_title('E1b Subclade Distribution', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Count')
    
    # E1a subclades
    e1a_samples = df[df['YCC_Haplogroup'].str.contains('E1a', na=False)]
    e1a_subclades = e1a_samples['YCC_Haplogroup'].value_counts()
    
    if len(e1a_subclades) > 0:
        ax3.bar(range(len(e1a_subclades)), e1a_subclades.values,
                color=plt.cm.spring(np.linspace(0, 1, len(e1a_subclades))))
        ax3.set_xticks(range(len(e1a_subclades)))
        ax3.set_xticklabels(e1a_subclades.index, rotation=45, ha='right')
        ax3.set_title('E1a Subclade Distribution', fontsize=12, fontweight='bold')
        ax3.set_ylabel('Count')
    
    # Terminal SNP diversity
    terminal_counts = df['Terminal_SNP'].value_counts().head(10)
    ax4.barh(range(len(terminal_counts)), terminal_counts.values,
             color=plt.cm.coolwarm(np.linspace(0, 1, len(terminal_counts))))
    ax4.set_yticks(range(len(terminal_counts)))
    ax4.set_yticklabels(terminal_counts.index)
    ax4.set_title('Top Terminal SNPs', fontsize=12, fontweight='bold')
    ax4.set_xlabel('Count')
    
    plt.suptitle('Detailed E Haplogroup Subclade Analysis in YRI Population', 
                 fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('yri_e_subclade_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_phylogenetic_tree_visualization(df):
    """Create a simplified phylogenetic tree visualization"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Define hierarchical structure
    haplogroups = df['YCC_Haplogroup'].value_counts()
    
    # Create a simplified tree structure
    y_positions = {}
    colors = {}
    
    # E root
    ax.text(0, 0.5, 'E', fontsize=16, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue'))
    
    # E1 and E2 branches
    ax.plot([0.1, 0.3], [0.5, 0.7], 'k-', linewidth=2)
    ax.plot([0.1, 0.3], [0.5, 0.3], 'k-', linewidth=2)
    
    ax.text(0.3, 0.7, 'E1', fontsize=14, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen'))
    ax.text(0.3, 0.3, 'E2', fontsize=14, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightcoral'))
    
    # E1a and E1b branches
    ax.plot([0.4, 0.6], [0.7, 0.8], 'k-', linewidth=2)
    ax.plot([0.4, 0.6], [0.7, 0.6], 'k-', linewidth=2)
    
    ax.text(0.6, 0.8, 'E1a', fontsize=12, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow'))
    ax.text(0.6, 0.6, 'E1b', fontsize=12, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightpink'))
    
    # Add sample counts
    e1_count = len(df[df['YCC_Haplogroup'].str.contains('E1', na=False)])
    e2_count = len(df[df['YCC_Haplogroup'].str.contains('E2', na=False)])
    e1a_count = len(df[df['YCC_Haplogroup'].str.contains('E1a', na=False)])
    e1b_count = len(df[df['YCC_Haplogroup'].str.contains('E1b', na=False)])
    
    ax.text(0.3, 0.65, f'n={e1_count}', fontsize=10, ha='center', va='center')
    ax.text(0.3, 0.25, f'n={e2_count}', fontsize=10, ha='center', va='center')
    ax.text(0.6, 0.75, f'n={e1a_count}', fontsize=10, ha='center', va='center')
    ax.text(0.6, 0.55, f'n={e1b_count}', fontsize=10, ha='center', va='center')
    
    # Add major subclades
    major_subclades = ['E1b1a1a1c1a1', 'E1b1a1a1d1a', 'E1b1a1a1d1', 'E1b1a1a1c1a1c']
    y_pos = [0.45, 0.35, 0.25, 0.15]
    
    for i, subclade in enumerate(major_subclades):
        if subclade in haplogroups.index:
            count = haplogroups[subclade]
            ax.plot([0.7, 0.9], [0.6, y_pos[i]], 'k-', linewidth=1)
            ax.text(0.9, y_pos[i], f'{subclade}\n(n={count})', fontsize=9, 
                   ha='left', va='center',
                   bbox=dict(boxstyle="round,pad=0.2", facecolor='wheat'))
    
    ax.set_xlim(-0.1, 1.3)
    ax.set_ylim(0, 1)
    ax.set_title('Simplified Y-Chromosome Phylogenetic Tree for YRI Population', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('yri_phylogenetic_tree.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_summary_dashboard(df, ycc_freq):
    """Create a comprehensive summary dashboard"""
    fig = plt.figure(figsize=(20, 12))
    
    # Create grid layout
    gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)
    
    # Main pie chart
    ax1 = fig.add_subplot(gs[0:2, 0:2])
    top_hgs = ycc_freq.head(6)
    others_count = ycc_freq.iloc[6:]['Count'].sum() if len(ycc_freq) > 6 else 0
    
    if others_count > 0:
        labels = list(top_hgs['YCC_Haplogroup']) + ['Others']
        sizes = list(top_hgs['Count']) + [others_count]
    else:
        labels = list(top_hgs['YCC_Haplogroup'])
        sizes = list(top_hgs['Count'])
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))
    wedges, texts, autotexts = ax1.pie(sizes, labels=labels, autopct='%1.1f%%', 
                                       startangle=90, colors=colors)
    ax1.set_title('YCC Haplogroup Distribution', fontsize=14, fontweight='bold')
    
    # E subclade breakdown
    ax2 = fig.add_subplot(gs[0, 2])
    e_major = df['YCC_Haplogroup'].str.extract(r'(E\d+)')[0].value_counts()
    ax2.pie(e_major.values, labels=e_major.index, autopct='%1.1f%%', 
            colors=['#ff9999', '#66b3ff'])
    ax2.set_title('E1 vs E2', fontsize=12, fontweight='bold')
    
    # Sample diversity metrics
    ax3 = fig.add_subplot(gs[1, 2])
    metrics = [
        f"Total Samples: {len(df)}",
        f"Unique YCC Haplogroups: {df['YCC_Haplogroup'].nunique()}",
        f"Unique Terminal SNPs: {df['Terminal_SNP'].nunique()}",
        f"E Haplogroup: {len(df[df['YCC_Haplogroup'].str.contains('E', na=False)])} (100%)",
        f"E1b1a1a1 subclades: {len(df[df['YCC_Haplogroup'].str.contains('E1b1a1a1', na=False)])}"
    ]
    
    for i, metric in enumerate(metrics):
        ax3.text(0.05, 0.9 - i*0.15, metric, fontsize=11, fontweight='bold',
                transform=ax3.transAxes)
    ax3.set_title('Population Metrics', fontsize=12, fontweight='bold')
    ax3.axis('off')
    
    # Top terminal SNPs
    ax4 = fig.add_subplot(gs[0, 3])
    terminal_counts = df['Terminal_SNP'].value_counts().head(5)
    ax4.barh(range(len(terminal_counts)), terminal_counts.values,
             color=plt.cm.viridis(np.linspace(0, 1, len(terminal_counts))))
    ax4.set_yticks(range(len(terminal_counts)))
    ax4.set_yticklabels(terminal_counts.index, fontsize=9)
    ax4.set_title('Top Terminal SNPs', fontsize=12, fontweight='bold')
    
    # Frequency table
    ax5 = fig.add_subplot(gs[2, :])
    table_data = ycc_freq.head(8)[['YCC_Haplogroup', 'Count', 'Percentage']].round(1)
    table = ax5.table(cellText=table_data.values, colLabels=table_data.columns,
                      cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    ax5.axis('off')
    ax5.set_title('Haplogroup Frequency Table', fontsize=12, fontweight='bold', y=0.9)
    
    plt.suptitle('YRI Y-Chromosome Haplogroup Analysis Dashboard', 
                 fontsize=18, fontweight='bold', y=0.98)
    
    plt.savefig('yri_haplogroup_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Create all visualizations"""
    print("Loading analysis data...")
    df, major_freq, ycc_freq, terminal_freq, e1_freq, e2_freq = load_analysis_data()
    
    print("Creating YCC haplogroup pie chart...")
    create_ycc_haplogroup_pie_chart(ycc_freq)
    
    print("Creating haplogroup bar chart...")
    create_haplogroup_bar_chart(ycc_freq)
    
    print("Creating E subclade analysis...")
    create_e_subclade_analysis(df)
    
    print("Creating phylogenetic tree visualization...")
    create_phylogenetic_tree_visualization(df)
    
    print("Creating summary dashboard...")
    create_summary_dashboard(df, ycc_freq)
    
    print("\nVisualization files created:")
    print("- yri_ycc_haplogroup_pie_chart.png")
    print("- yri_haplogroup_bar_chart.png")
    print("- yri_e_subclade_analysis.png")
    print("- yri_phylogenetic_tree.png")
    print("- yri_haplogroup_dashboard.png")

if __name__ == "__main__":
    main()

