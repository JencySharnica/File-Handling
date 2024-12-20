from text_operations.write_text import write_to_file
from text_operations.read_text import read_from_file
from text_operations.append_text import append_to_file
from csv_operations.write_csv import write_csv
from csv_operations.read_csv import read_csv

if _name_ == "_main_":
    # Text File Operations
    write_to_file("example.txt", "This is the first line of text.\n")
    read_from_file("example.txt")
    append_to_file("example.txt", "This is an appended line.\n")
    read_from_file("example.txt")

    # CSV File Operations
    csv_data = [["Name", "Age", "City"], ["Alice", 30, "New York"], ["Bob", 25, "Los Angeles"]]
    write_csv("example.csv", csv_data)
    read_csv("example.csv")