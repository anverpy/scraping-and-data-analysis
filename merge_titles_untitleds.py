import csv

def merge_titles_and_data(titles_file: str, data_file: str, output_file: str) -> None:
    with open(titles_file, 'r', encoding='utf-8') as f_titles, \
         open(data_file, 'r', encoding='utf-8') as f_data:

        titles_reader = csv.reader(f_titles)
        data_reader = csv.reader(f_data)

        # Leer y descartar cabecera de títulos si la hay
        title_header = next(titles_reader)
        data_header = next(data_reader)

        if title_header[0].strip().lower() != "title":
            # Si no hay cabecera, se consideran todos como datos
            titles_reader = csv.reader(open(titles_file, 'r', encoding='utf-8'))
            titles = list(titles_reader)
        else:
            titles = list(titles_reader)

        data = list(data_reader)

        # Validar longitud
        if len(titles) != len(data):
            print(f"❌ Los archivos no tienen la misma cantidad de filas: {len(titles)} títulos vs {len(data)} datos.")
            return

        merged = []
        merged.append(["title"] + data_header)  # Cabecera final

        for title_row, data_row in zip(titles, data):
            merged.append(title_row + data_row)

    with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        writer.writerows(merged)

    print(f"✅ Archivo fusionado guardado como {output_file} con {len(merged)-1} registros.")
merge_titles_and_data("titles-ML-gigs.csv", "no_titles_ML-gigs.csv", "fixed_ML-gigs.csv")
