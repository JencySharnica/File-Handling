import csv

def read_csv(filename):
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            print(f"Content of {filename}:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error reading from CSV file: {e}")