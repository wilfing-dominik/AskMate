import csv

ANSWER_HEADER = ['id','submission_time','vote_number','question_id','message','image']

def open_file(file):
    data = []
    with open('./data/' + file, 'r') as csv_file:
        raw_data = csv.DictReader(csv_file, fieldnames=ANSWER_HEADER)
        for row in raw_data:
            data.append(row)
        return data


def append_to_file(file, data):
    with open('./data/' + file, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=ANSWER_HEADER)
        writer.writerow(data)


def write_to_file(file, data):
    with open('./data/' + file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=ANSWER_HEADER)
        for row in data:
            writer.writerow(row)