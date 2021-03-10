import csv

def open_file(file, header):
    data = []
    with open('./data/' + file, 'r') as csv_file:
        raw_data = csv.DictReader(csv_file, fieldnames=header)
        for row in raw_data:
            data.append(row)
        return data


def append_to_file(file, data, header):
    with open('./data/' + file, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writerow(data)


def write_to_file(file, data, header):
    with open('./data/' + file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        for row in data:
            writer.writerow(row)