import tabulate
import sys
import csv

def read_csv(fname: str) -> list[list[str]]:
    with open(fname) as file:
        data = [row for row in csv.reader(file, delimiter='|')]
    return data

if __name__ == '__main__':
    data = read_csv(sys.argv[1])
    print(tabulate.tabulate(data[0:5]))