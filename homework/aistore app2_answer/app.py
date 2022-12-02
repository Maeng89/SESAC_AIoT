from flask import Flask, request, render_template, redirect, url_for, session
import sys
from aistore import *
import datetime
from wtforms import Form, StringField, PasswordField, TextAreaField, validators

app = Flask(__name__)

app.config['SECRET_KEY'] = 'aiot'

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=5)
    session.modified = True

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route("/sregister", methods=['POST', 'GET'])
def sregister():
    if request.method == 'POST':
        s_id = request.form['sId']
        s_name = request.form['sName']
        locate = request.form['locate']
        create_store(s_id, s_name, locate)
        return redirect('/')

    return render_template('sregister.html')

@app.route("/stores", methods=['POST', 'GET'])
def stores():
    if request.method == 'POST':
        s_id = request.form['sId']

        return render_template('stores.html', stores = show_list(s_id))

    return render_template('stores.html', stores = show_list())

@app.route("/manage/<s_id>", methods=['POST', 'GET'])
def manage(s_id = 'nan'):
    if request.method == 'POST':
        if s_id == 'nan':
            s_id = request.form['sId']
            ai_store = search_store(s_id)

            return render_template('manage.html',
                                    s_id = s_id,
                                    inventory=ai_store.get_menu(),
                                    products=get_products()
                                    )
        else:
            p_id = request.form['pId']
            price = request.form['price']
            count = int(request.form['count'])
            ai_store = search_store(s_id)
            set_product(ai_store, p_id, price, count)
            update(ai_store)
            ai_store = search_store(s_id)

            return render_template('manage.html',
                                    s_id = s_id,
                                    inventory = ai_store.get_menu(),
                                    products = get_products())

    return render_template('manage.html', s_id = s_id, )

@app.route("/board/<s_id>", methods=['POST', 'GET'])
def board(s_id = 'nan'):
    if request.method == 'POST':
            s_id = request.form['sId']
            ai_store = search_store(s_id)
            redirect(url_for('board', s_id = s_id))
            # return render_template('board.html', s_id = s_id, menu = ai_store.get_menu())

    if s_id != 'nan':
        ai_store = search_store(s_id)
        return render_template('board.html',
                               s_id=s_id, menu = ai_store.get_menu())
    else:
        return render_template('board.html',
                               s_id=s_id,)

@app.route("/buy/<s_id>/<p_id>", methods=['POST', 'GET'])
def buy(s_id, p_id):
    ai_store = search_store(s_id)
    product = ai_store.get_product(p_id)
    if 'count' not in session:
        session['count'] = 1
    if request.method == 'POST':
        if request.form.get('plus') == '+':
            session['count'] +=1

        elif request.form.get('sub') == '-':
            if session['count'] > 1:
                session['count'] -=1

        else:
            ai_store.buy_product(p_id, session['count'])
            update(ai_store)
            del session['count']
            return redirect(url_for('board', s_id = s_id))

    return render_template('buy.html',
                           s_id=s_id, p_id = p_id,
                           product = product,
                           count = session['count']
                           )


if __name__ == '__main__':
    app.run('0.0.0.0',9999, debug=True)