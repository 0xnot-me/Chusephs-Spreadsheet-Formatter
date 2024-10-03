import pandas as pd
import csv

def process_csv(input_file, output_file):
    # Read the CSV file, skipping the first 5 rows
    df = pd.read_csv(input_file, skiprows=5, names=['ROW ID', 'ARCHITECTURE', 'KB', 'NAME'])

    # Create a pivot table
    pivot = pd.pivot_table(df, values='ARCHITECTURE', index=['NAME'], 
                           columns=['KB'], aggfunc=lambda x: ', '.join(set(x)))

    # Reset index to make 'NAME' a column
    pivot.reset_index(inplace=True)

    # Rename 'NAME' column to 'URL' and add 'ID' column
    pivot.rename(columns={'NAME': 'URL'}, inplace=True)
    pivot.insert(0, 'ID', range(1, len(pivot) + 1))

    # Save to CSV
    pivot.to_csv(output_file, index=False, quoting=csv.QUOTE_ALL)

    print(f"Processed data saved to {output_file}")

# Usage
input_file = 'input.csv'  # Replace with your input file name
output_file = 'output.csv'  # Replace with your desired output file name

process_csv(input_file, output_file)