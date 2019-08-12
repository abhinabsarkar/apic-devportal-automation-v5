import csv

with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    # This skips the first row of the CSV file.
    # csvreader.next() also works in Python 2.
    next(csv_reader)
    for row in csv_reader:
        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')

# Read in Dictionary object
with open('input.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(f'\t{row["Developer Org Name"]} works in the {row["App Name"]} department, and was born in {row["Plan Name"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')