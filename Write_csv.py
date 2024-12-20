import csv

def write_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
            print(f"Data written to {filename}")
    except Exception as e:
        print(f"Error writing to CSV file: {e}")