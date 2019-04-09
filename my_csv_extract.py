import csv
from my_row import *


def extract_data(filename):
    table = open(filename, 'r')
    reader = csv.DictReader(table)
    data = list()
    fieldnames = reader.fieldnames
    for row in reader:
        data.append(Row(row, len(fieldnames) - 2))
    table.close()
    return data, fieldnames


def write_data(data, fieldnames, filename):
    output = open(filename[:-4] + "_result.csv", 'w')
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(data)):
        writer.writerow(data[i].csv_row)
    output.close()
