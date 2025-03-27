import pandas as pd
import os
import sys

def count_reference_frequency(input_csv):
    df = pd.read_csv(input_csv)
    df_unique = df.drop_duplicates(subset=['Article_Index', 'Cited_Reference'])

    ref_counts = df_unique.groupby('Cited_Reference').agg(
        Articles_Citing=('Article_Index', 'nunique')
    ).reset_index()

    ref_counts_sorted = ref_counts.sort_values(by='Articles_Citing', ascending=False)
    return ref_counts_sorted

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python count_reference_frequency.py <exploded_references_csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    df_freq = count_reference_frequency(input_path)

    os.makedirs("outputs", exist_ok=True)
    output_path = "outputs/cited_reference_frequency.csv"
    df_freq.to_csv(output_path, index=False)
    print(f"✅ Frequency table saved to: {output_path}")