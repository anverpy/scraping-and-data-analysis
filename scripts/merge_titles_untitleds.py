import csv
import os

def merge_titles_and_data(titles_file: str, data_file: str, output_file: str) -> None:
    # Get path to the root directory
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    titles_path = os.path.join(root_dir, titles_file)
    data_path = os.path.join(root_dir, data_file)
    output_path = os.path.join(root_dir, output_file)
    
    with open(titles_path, 'r', encoding='utf-8') as f_titles, \
         open(data_path, 'r', encoding='utf-8') as f_data:

        titles_reader = csv.reader(f_titles)
        data_reader = csv.reader(f_data)

        title_header = next(titles_reader)
        data_header = next(data_reader)

        if title_header[0].strip().lower() != "title":
            titles_reader = csv.reader(open(titles_path, 'r', encoding='utf-8'))
            titles = list(titles_reader)
        else:
            titles = list(titles_reader)

        data = list(data_reader)

        if len(titles) != len(data):
            print(f"❌ Row count doesn't match: {len(titles)} titles vs {len(data)} data.")
            return

        merged = []
        merged.append(["title"] + data_header) 

        for title_row, data_row in zip(titles, data):
            merged.append(title_row + data_row)

    with open(output_path, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        writer.writerows(merged)

    print(f"✅ Merged file saved as {output_file} with {len(merged)-1} records.")

# Example usage:
# merge_titles_and_data("titles-ML-gigs.csv", "no_titles_ML-gigs.csv", "fixed_ML-gigs.csv")
