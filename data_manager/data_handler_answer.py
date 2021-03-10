import csv
import datetime

ANSWER_HEADER = ['id','submission_time','vote_number','question_id','message','image']

def get_all_answers_by_latest():
    data = []
    with open('./data/answer.csv', 'r') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            data.append(row)
            data = sorted(data, key=lambda i: i['submission_time'])
    return data


def get_answer_by_question_id(question_id):
    data = []
    with open('./data/answer.csv', 'r') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            if row['question_id'] == question_id:
                data.append(row)
    return data


def add_answer(answer, question_id):
    data = {}  
    with open('./data/answer.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=ANSWER_HEADER)
        
        answers = get_all_answers_by_latest()
        if len(answers) == 0:
            iddd = 1
        else:
            idd = answers[len(answers)-1]['id']
            iddd = int(idd)+1

        data['id'] =  iddd
        data['submission_time'] = datetime.date.today()
        data['vote_number'] = 0
        data['question_id'] = question_id
        data['message'] = answer
        data['image'] =  None

        writer.writerow(data)


def delete_answer_by_id(answer_id):
    lines = []

    with open('./data/answer.csv', 'r',  newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)
            print(row)
            if row[0] == answer_id:
                lines.remove(row)
                
    with open('./data/answer.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(lines)