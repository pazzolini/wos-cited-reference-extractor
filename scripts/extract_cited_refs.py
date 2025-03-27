import pandas as pd
import os
import sys

def parse_wos_plain_text_with_cited_refs(filepath):
    records = []
    current_refs = []
    inside_refs = False

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            stripped = line.rstrip()

            if stripped.startswith('PT '):
                if current_refs:
                    records.append(current_refs)
                    current_refs = []
                inside_refs = False

            elif stripped.startswith('CR '):
                inside_refs = True
                current_refs.append(stripped[3:].strip())

            elif inside_refs and (line.startswith('   ') or line.startswith('\t')):
                current_refs.append(stripped.strip())

            elif stripped.startswith('NR ') or stripped.startswith('ER'):
                inside_refs = False
                if current_refs:
                    records.append(current_refs)
                    current_refs = []

    if current_refs:
        records.append(current_refs)

    exploded = []
    for idx, ref_list in enumerate(records):
        for ref in ref_list:
            if len(ref) > 5:
                exploded.append({'Article_Index': idx, 'Cited_Reference': ref})

    return pd.DataFrame(exploded)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python extract_cited_refs.py <path_to_wos_txt_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    df = parse_wos_plain_text_with_cited_refs(input_path)

    os.makedirs("outputs", exist_ok=True)
    output_path = "outputs/exploded_references.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Extracted cited references saved to: {output_path}")