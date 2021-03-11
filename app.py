from flask import Flask
from flask import render_template, redirect, request
from data_manager import data_handler_question
from data_manager import data_handler_answer

app = Flask(__name__)


@app.route("/")
@app.route('/list')
def question_list():
    if request.args:
        if request.args.get('order') == 'ascending':
            order = False
        else:
            order = True
        by = request.args.get('by')
        data = data_handler_question.get_all_quetions_by_latest(order, by)
    else:
        data = data_handler_question.get_all_quetions_by_latest()
    return render_template('list.html', data=data)


@app.route('/question/<question_id>')
def question(question_id):
    question = data_handler_question.get_question_by_id(question_id)
    data_handler_question.increment_view_number(question)
    answers = data_handler_answer.get_answer_by_question_id(question_id)

    if len(answers) > 0:
        return render_template('question.html', question=question, answers=answers)
    else:
        return render_template('question.html', question=question)


@app.route('/add-question', methods=['POST', 'GET'])
def add_question():

    if request.method == 'POST':
        data = data_handler_question.get_all_quetions_by_latest()
        if len(data) == 0:
            question_id = 1
        else:
            question_id = int(data[len(data)-1]['id'])+1
        question = {'id': question_id, 'message': request.form['message'], 'title': request.form['title']}
        data_handler_question.add_question(question)
        return redirect('/question/' + str(question['id']))

    return render_template('add-question.html')


@app.route('/question/<question_id>/delete-question', methods=['POST', 'GET'])
def delete_question(question_id):

    if request.method == 'GET':
        data_handler_question.delete_question_by_id(question_id)
        return redirect('/')


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def post_answer(question_id):
   
    if request.method == 'POST':
        answer = request.form['answer']
        data_handler_answer.add_answer(answer ,question_id)
        return redirect('/question/' + str(question_id))

    return render_template('post-answer.html', question_id=question_id)


@app.route('/question/<answer_id>/delete-answer', methods=['GET','POST'])
def delete_answer_by_id(answer_id):
        data_handler_answer.delete_answer_by_id(answer_id)
        return redirect('/')


@app.route('/question/<question_id>/edit', methods=['POST', 'GET'])
def edit_question(question_id):
    question = data_handler_question.get_question_by_id(question_id)

    if request.method == 'POST':
        data_handler_question.edit_question_by_id() 
        return redirect('/question/' + str(question_id))

    return render_template('edit-question.html', question=question, question_id=question_id)


if __name__ == "__main__":
    app.debug=True
    app.run()
