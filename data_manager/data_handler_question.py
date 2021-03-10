import csv
import datetime

QUESTION_HEADER = ['id','submission_time','view_number','vote_number','title','message','image']

def get_all_quetions_by_latest():
    data = []
    with open('./data/question.csv', 'r') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            data.append(row)
            data = sorted(data, key=lambda i: i['submission_time'])
    return data


def get_question_by_id(question_id):
    with open('./data/question.csv', 'r') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            if row['id'] == question_id:
                return row


def add_question(question):
    data = {}
    with open('./data/question.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=QUESTION_HEADER)
        data['id'] = question['id']
        data['submission_time'] = datetime.datetime.now()
        data['view_number'] = 0
        data['vote_number'] = 0 
        data['title'] = question['title']
        data['message'] = question['message'] 
        data['image'] = None
        
        writer.writerow(data)
    

def increment_view_number(question):
    pass
         

def delete_question_by_id(question_id):
    question_lines = []
    answer_lines = []

    with open('./data/question.csv', 'r',  newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            question_lines.append(row)
            if row[0] == question_id:
                question_lines.remove(row)
                
    with open('./data/question.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(question_lines)

    with open('./data/answer.csv', 'r',  newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            answer_lines.append(row)
            if row[3] == question_id:
                answer_lines.remove(row)
                
    with open('./data/answer.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(answer_lines)


def edit_question_by_id():
    questions = []

    with open('./data/question.csv', 'r',  newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            pass
                
    '''with open('./data/question.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(question)'''
        