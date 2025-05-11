import csv
import os

def join_parts(part1_file: str, part2_file: str, output_file: str) -> None:
    # Get path to the root directory
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    part1_path = os.path.join(root_dir, part1_file)
    part2_path = os.path.join(root_dir, part2_file)
    output_path = os.path.join(root_dir, output_file)
    
    with open(part1_path, 'r', encoding='utf-8') as f1, \
         open(part2_path, 'r', encoding='utf-8') as f2:

        reader1 = list(csv.reader(f1))
        reader2 = list(csv.reader(f2))

        header1 = reader1[0]
        header2 = reader2[0]

        if header1 != header2:
            print("❌ Headers don't match.")
            print("P1:", header1)
            print("P2:", header2)
            return

        merged = [header1] + reader1[1:] + reader2[1:]

    with open(output_path, 'w', newline='', encoding='utf-8') as fout:
        writer = csv.writer(fout)
        writer.writerows(merged)

    print(f"✅ Merged files in {output_file} with {len(merged)-1} records.")
    
# Example usage:
# join_parts("da-p1.csv", "da-p2.csv", "DA-gigs.csv")

