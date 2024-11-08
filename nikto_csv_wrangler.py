import pandas as pd
import os
import glob
import chardet
import argparse

# Detect file encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        return result['encoding']

# Combine CSV files into one file with a heading
def combine_csv_files(input_dir, output_file):
    # Get a list of all CSV files in the directory
    all_files = glob.glob(os.path.join(input_dir, "*.csv"))
    
    # List to store dataframes
    dfs = []

    # Define expected column names (adjust these if your data has specific column names)
    # sullo doesn't want to give us headings but I think this is what he means
    column_names = ["Hostname", "IP Address", "Port", "Reference", "Verb", "Path", "Description"]

    # Loop through each file, detect encoding, and read it if not empty
    for file in all_files:
        # Check if the file is empty
        if os.path.getsize(file) == 0:
            print(f"Skipping empty file: {file}")
            continue
        
        # Detect encoding
        encoding = detect_encoding(file)
        # print(f"Detected encoding for {file}: {encoding}")
        
        # Read the CSV file with the detected encoding, handling errors in lines
        try:
            # Skip the first row, specify column names, and set the delimiter
            df = pd.read_csv(file, encoding=encoding, sep=',', skiprows=1, names=column_names, on_bad_lines="skip")
            # print(f"Columns in {file}: {df.columns.tolist()}")
            dfs.append(df)
        except pd.errors.EmptyDataError:
            print(f"Skipping empty or unreadable file: {file}")
        except pd.errors.ParserError as e:
            print(f"Parser error in file {file}: {e}")
            continue

    # Concatenate all dataframes, filling missing columns with NaN
    combined_df = pd.concat(dfs, ignore_index=True)

    # Save the combined file as CSV
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSV saved as {output_file}")

# Main function to handle argument parsing
def main():
    parser = argparse.ArgumentParser(description="Combine multiple CSV files from a directory into a single output file.")
    parser.add_argument("input_dir", type=str, help="Directory containing the CSV files to combine")
    parser.add_argument("output_file", type=str, help="Path for the combined output CSV file")
    
    args = parser.parse_args()
    combine_csv_files(args.input_dir, args.output_file)

if __name__ == "__main__":
    main()
