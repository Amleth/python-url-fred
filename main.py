import argparse
import csv
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--csv_in")
parser.add_argument("--csv_out")
args = parser.parse_args()

urls = []

with open(args.csv_in, newline='') as f:
    data = csv.reader(f)
    for row in data:
        url = row[0]
        if url[:4] == 'http':
            print(url)
            try:
                _ = requests.head(url)
                to = _.headers['Location']
                print('    ->', to)
            except:
                to = ''
            urls.append([url, to])

with open(args.csv_out, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(urls)
