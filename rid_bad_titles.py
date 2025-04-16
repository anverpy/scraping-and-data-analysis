import csv

def remove_titles_by_tail(input_file: str, output_file: str) -> None:
    output_rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if len(row) >= 6:
                tail = row[-6:]  # Tomar las últimas 6 columnas (las válidas)
                output_rows.append(tail)
            else:
                print(f"⚠️ Línea {i+1} con menos de 6 columnas: {row}")

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)

    print(f"✅ Archivo guardado como {output_file} con {len(output_rows)} líneas limpias.")

# Ejecutar desde el mismo directorio
remove_titles_by_tail("ML-gigs.csv", "no_titles_ML-gigs.csv")
