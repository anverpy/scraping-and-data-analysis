import csv

def join_parts(part1_file: str, part2_file: str, output_file: str) -> None:
    with open(part1_file, 'r', encoding='utf-8') as f1, \
         open(part2_file, 'r', encoding='utf-8') as f2:

        reader1 = list(csv.reader(f1))
        reader2 = list(csv.reader(f2))

        # Asegurarse que ambas partes tengan la misma estructura de cabecera
        header1 = reader1[0]
        header2 = reader2[0]

        if header1 != header2:
            print("❌ Las cabeceras de los archivos no coinciden.")
            print("Parte 1:", header1)
            print("Parte 2:", header2)
            return

        merged = [header1] + reader1[1:] + reader2[1:]

    with open(output_file, 'w', newline='', encoding='utf-8') as fout:
        writer = csv.writer(fout)
        writer.writerows(merged)

    print(f"✅ Archivos combinados en {output_file} con {len(merged)-1} registros.")
join_parts("da-p1.csv", "da-p2.csv", "merged-final.csv")

