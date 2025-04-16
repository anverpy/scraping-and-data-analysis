import csv
import pandas as pd

def extract_titles_only(filepath: str, output_filename: str) -> None:
    titles = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if len(row) > 6:
                idx_of_second_column = len(row) - 6
                title_parts = row[:idx_of_second_column]
                raw_title = ','.join(title_parts).strip()
                titles.append([raw_title])
            else:
                print(f"⚠️ Line {i+1} <7 {row}")
            
            if i % 1000 == 0:
                print(f"Processed {i} lines...")

    df_titles = pd.DataFrame(titles, columns=['title'])
    df_titles.to_csv(output_filename, index=False)
    print(f"✅ Saved as {output_filename} with {len(titles)} extracted titles.")

extract_titles_only("ML-gigs.csv", "titles-ML-gigs.csv")


