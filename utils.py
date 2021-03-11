import csv

def open_file(csv_file_name, HEADER):
    data = []
    with open("data/" + csv_file_name, "r", encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data


def append_to_file(csv_file_name, new_data, HEADER):
    with open("data/" + csv_file_name, "a", encoding="utf8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=HEADER)
        writer.writerow(new_data)


def write_to_file(csv_file_name, new_data, HEADER):
    with open("data/" + csv_file_name, "w", encoding="utf8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=HEADER)
        writer.writeheader()
        for row in new_data:
            writer.writerow(row)