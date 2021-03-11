import utils
import datetime

questions_data = "question.csv"
answers_data = "answer.csv"
QUESTION_HEADER = ['id','submission_time','view_number','vote_number','title','message','image']
ANSWER_HEADER = ['id','submission_time','vote_number','question_id','message','image']

def get_all_quetions_by_latest(order=False, by='submission_time'):
    data = []
    questions = utils.open_file(questions_data, QUESTION_HEADER)
    for row in questions:
        data.append(row)
        data = sorted(data, key=lambda i: i[by],reverse=order)
    return data


def get_question_by_id(question_id):
    questions = utils.open_file(questions_data, QUESTION_HEADER)

    for row in questions:
        if row['id'] == question_id:
            return row


def add_question(question):
    data = {}
    data['id'] = question['id']
    data['submission_time'] = datetime.datetime.now()
    data['view_number'] = 0
    data['vote_number'] = 0 
    data['title'] = question['title']
    data['message'] = question['message'] 
    data['image'] = ''
    
    utils.append_to_file(questions_data, data, QUESTION_HEADER)


def increment_view_number(question):
    pass
         

def delete_question_by_id(question_id):
    
    question_lines = []
    questions = utils.open_file(questions_data, QUESTION_HEADER)
    for row in questions:
        if row['id'] != question_id:
             question_lines.append(row)
    utils.write_to_file(questions_data, question_lines, QUESTION_HEADER)          

    answer_lines = []
    answers = utils.open_file(answers_data, ANSWER_HEADER)
    for row in answers:
        if row['question_id'] != question_id:
            answer_lines.append(row)
    utils.write_to_file(answers_data, answer_lines, ANSWER_HEADER)           


def edit_question_by_id():
    questions = []

    utils.open_file(questions_data, QUESTION_HEADER)
    for row in reader:
        pass
                
    '''with open('./data/question.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(question)'''
        