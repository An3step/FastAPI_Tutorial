import csv
import sys

def read_csv(fname: str) -> list[list[str]]:
    with open(fname) as file:
        data = [row for row in csv.reader(file, delimiter='|')]
    return data

if __name__ == '__main__':
    data = read_csv(sys.argv[1])
    print(type(data[0]))
    for row in data[0:5]:
        print(row)