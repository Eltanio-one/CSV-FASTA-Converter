import sys
import csv


def main():
    # check command-line argument passed
    if len(sys.argv) != 3:
        print("Usage: main.py <excel file> <output file>")
        return
    # open csv
    with open(sys.argv[1], "r") as file:
        # create reader object
        reader = csv.reader(file)
        # make temp list to store id and sequence
        temp_list = []
        # append all rows to temp list
        for row in reader:
            temp_list.append(row)
        # pop header
        temp_list.pop(0)
    # create output file
    with open(sys.argv[2], "w") as file:
        for row in temp_list:
            # reformat id and sequence into fasta format
            file.write(f">{row[0]}\n{row[1]}\n")


if __name__ == "__main__":
    main()
