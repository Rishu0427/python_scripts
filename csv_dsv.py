import csv

def convert_csv(input_file, output_file, delimiter):
    """
    Convert a CSV file to a delimiter-separated file, handling multiline fields and errors.

    Parameters:
    - input_file: str, path to the input CSV file.
    - output_file: str, path to the output delimiter-separated file.
    - delimiter: str, delimiter to be used in the output file.
    """
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            
            # Use the csv.DictReader to handle multiline fields correctly
            reader = csv.reader(infile)
            writer = csv.writer(outfile, delimiter=delimiter)
            
            # Write the header row
            header = next(reader)
            writer.writerow(header)
            
            # Write the data rows
            for row in reader:
                writer.writerow(row)
                
        print(f"File '{input_file}' successfully converted to '{output_file}' with '{delimiter}' as delimiter.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = 'start.csv'
output_file = 'end.csv'
delimiter = '\t'  # Change this to the desired delimiter, e.g., '\t' for tab

convert_csv(input_file, output_file, delimiter)
