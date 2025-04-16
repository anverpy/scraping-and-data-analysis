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
                print(f"⚠️ Línea {i+1} con menos de 7 columnas: {row}")
            
            if i % 1000 == 0:
                print(f"Procesadas {i} líneas...")

    df_titles = pd.DataFrame(titles, columns=['title'])
    df_titles.to_csv(output_filename, index=False)
    print(f"✅ Archivo guardado como {output_filename} con {len(titles)} títulos extraídos.")

# Ejecutar desde el mismo directorio
extract_titles_only("ML-gigs.csv", "titles-ML-gigs.csv")


