import csv
import os

def remove_titles_by_tail(input_file: str, output_file: str) -> None:
    # Get path to the root directory
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(root_dir, input_file)
    output_path = os.path.join(root_dir, output_file)
    
    output_rows = []
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if len(row) >= 6:
                tail = row[-6:]  
                output_rows.append(tail)
            else:
                print(f"⚠️ Line {i+1} has less than 6 columns: {row}")

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)

    print(f"✅ Saved as {output_file} with {len(output_rows)} clean rows.")

# Example usage:
# remove_titles_by_tail("ML-gigs.csv", "no_titles_ML-gigs.csv")
