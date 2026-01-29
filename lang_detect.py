"""
pip install langdetect pandas tqdm

Apply this to the Curated dataset (csv file)

"""

import pandas as pd
import sys
from langdetect import detect
from tqdm import tqdm

def is_english(text):
    try:
        return detect(str(text)) == 'en'
    except:
        return False

input_csv = sys.argv[1]
output_csv = sys.argv[2]

df = pd.read_csv(input_csv)

mask = []
for _, row in tqdm(df.iterrows(), total=len(df)):
    if row['label'] == 1:
        mask.append(True)
    else:
        mask.append(is_english(row['context']))

df = df[mask]
df.to_csv(output_csv, index=False)