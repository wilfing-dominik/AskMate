import datetime
import utils

questions_data = "question.csv"
answers_data = "answer.csv"
ANSWER_HEADER = {'id','submission_time','vote_number','question_id','message','image'}

def get_all_answers_by_latest():
    data = []
    answers = utils.open_file(questions_data, ANSWER_HEADER)

    for row in answers:
        data.append(row)
        data = sorted(data, key=lambda i: i['submission_time'])
    return data


def get_answer_by_question_id(question_id):
    data = []
    answers = utils.open_file(answers_data, ANSWER_HEADER)

    for row in answers:
        if row['question_id'] == question_id:
            data.append(row)
    return data


def add_answer(answer, question_id):
    data = {} 
    answers = utils.open_file(answers_data, ANSWER_HEADER)
    
    if len(answers) == 0:
        iddd = 1
    else:
        idd = answers[len(answers)-1]['id']
        id_int = int(idd) 
        iddd= id_int+1

    data['id'] =  iddd
    data['submission_time'] = datetime.datetime.now()
    data['vote_number'] = 0
    data['question_id'] = question_id
    data['message'] = answer
    data['image'] =  ""

    utils.append_to_file(answers_data, data, ANSWER_HEADER)


def delete_answer_by_id(answer_id):
    data = []
    answers = utils.open_file(answers_data, ANSWER_HEADER)

    for row in answers:
        if row['id'] != answer_id:
            data.append(row)

    utils.write_to_file(answers_data, data, ANSWER_HEADER)
