import pandas as pd
import os

def fill_gaps(input_file: str, output_file: str) -> None:
    """
    Fill empty fields in the CSV with default values.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    # Get path to the root directory (one level up from scripts)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(root_dir, input_file)
    output_path = os.path.join(root_dir, output_file)
    
    df = pd.read_csv(input_path)
    
    df['rating'].fillna('Unranked Gig', inplace=True)
    df['reviews'].fillna('No Reviewed', inplace=True)
    df['seller_level'].fillna('Unleveled', inplace=True)
    
    df.to_csv(output_path, index=False)
    print(f"✅ Filled gaps and saved as {output_file}")

# Example usage:
# fill_gaps('input.csv', 'output.csv')
