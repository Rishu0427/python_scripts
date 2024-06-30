import csv

def read_and_display_csv(input_file):
    """
    Read a CSV file and display its contents.

    Parameters:
    - input_file: str, path to the input CSV file.
    """
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            
            for row in reader:
                print(row)

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = 'start.csv'

read_and_display_csv(input_file)
