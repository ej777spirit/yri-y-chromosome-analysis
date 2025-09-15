#!/usr/bin/env python3
"""
Extract YRI male samples from 1000 Genomes panel file
"""

import pandas as pd

def extract_yri_males(panel_file):
    """Extract YRI male sample IDs from panel file"""
    # Read the panel file
    panel = pd.read_csv(panel_file, sep='\t')
    
    # Filter for YRI males
    yri_males = panel[(panel['pop'] == 'YRI') & (panel['gender'] == 'male')]
    
    print(f"Total samples in panel: {len(panel)}")
    print(f"YRI samples: {len(panel[panel['pop'] == 'YRI'])}")
    print(f"YRI male samples: {len(yri_males)}")
    
    # Save YRI male sample IDs
    yri_male_ids = yri_males['sample'].tolist()
    
    with open('yri_male_samples.txt', 'w') as f:
        for sample_id in yri_male_ids:
            f.write(f"{sample_id}\n")
    
    print(f"YRI male sample IDs saved to yri_male_samples.txt")
    print(f"First 10 YRI male samples: {yri_male_ids[:10]}")
    
    return yri_male_ids

if __name__ == "__main__":
    panel_file = "integrated_call_samples_v3.20130502.ALL.panel"
    yri_males = extract_yri_males(panel_file)

