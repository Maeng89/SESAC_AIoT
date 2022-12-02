from flask import Flask, request, render_template, redirect, url_for, session
import sys
from aistore import *
import datetime
from wtforms import Form, StringField, PasswordField, TextAreaField, validators

# Flask 인스턴스 생성
app = Flask(__name__)
# Flask 세션관리 및 암호화, git ignore 필수
# 세션ID에 접근하기 위해 암호화키 필요
app.config['SECRET_KEY'] = 'aiot'

#세션 시간 옵션설정
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

# 파라미터를 선언해두지 않았는데 가변인자처럼 추가가 가능하네?
@app.route("/manage/<s_id>", methods=['POST', 'GET'])
def manage(s_id = 'nan'): # 근데 왜 None이 아니라 스트링으로?
    if request.method == 'POST': # s_id로그인 화면(상품 등록 전)
        #폼이 두개로 나누어짐 s_id가 'nan'이냐 아니냐 로 판별가능

        if s_id == 'nan': # 'nan'일 때 스토어 로그인 폼
            # s_id를 통해 store 인스턴스를 받아옴 aistore 모듈의 함수 사용
            s_id = request.form['sId']
            store = search_store(s_id)
            # aistore 모듈의 p_df 목록을 가져오는 함수사용
            # 렌더링시 필요한 변수 할당해야 할것
            return render_template('manage.html',
                                   s_id = s_id,
                                   inventory = store.get_menu(),
                                   products = get_products_whole())

        else: # 아닐 때 상품 등록 폼 (manage안에서 상품 등록시)
            # s_id를 통해 ai_store 인스턴스를 받아옴
            store = search_store(s_id)
            # 폼에서 데이터 가져와 상품 업데이트 aistore모듈의 함수중 2개를 사용해야함
            p_id = request.form['pId']
            price = request.form['price']
            count = request.form['count']
            set_product(store, p_id, price, count)
            # 업데이트 불필요해 보이늰데 왜 2개일까? aistore인스턴스를 2번 받아오는 이유가 있나?
            # 상품 없을땐 인스턴스 set_product에서 update하고, 있을 땐 iv_df.loc으로 직접 입력함
            return render_template('manage.html',
                                   s_id=s_id,
                                   inventory = store.get_menu(),
                                   products = get_products_whole())

    # 최초 진입시
    return render_template('manage.html', s_id = s_id, )

@app.route("/board/<s_id>", methods=['POST', 'GET'])
def board(s_id = 'nan'):
    pass
#     if s_id != 'nan':
#         # 스토어 아이디가 있을땐 스토어 메뉴를 변수로 전달
#         # 스토어 인스턴스 받아온후 스토어클래스의 함수를 사용해 menu 전달
#         ~
#         return render_template('board.html',
#                                s_id=s_id, ~)
#     else:
#         #'nan' 일땐 폼을 통해서 페이지 렌더링
#         if request.method == 'POST':
#             ~
#             return render_template('board.html', s_id=s_id, ~)
#
#         return render_template('board.html',
#                                s_id=s_id,)

#물품 구매 페이지
@app.route("/buy/<s_id>/<p_id>", methods=['POST', 'GET'])
def buy(s_id, p_id):
    pass
    # # 스토어 인스턴스 찾아옴
    # # 스토어 함수 활용하여 상품 정보 찾아옴
    # ai_store = ~
    # product = ~
    # # 세션에 count 키가 없으면 'count'키의 값을 1로 할당 (아이템 구매 개수)
    # # 세션은 딕셔너리처럼 사용 가능하며 페이지접속자에 독립적으로 할당
    # if 'count' not in session:
    #     session['count'] = 1
    #
    # if request.method == 'POST':
    #
    #     if request.form.get('plus') == '+':
    #         # + 버튼일 경우만 true
    #         # 세션의 count를 +1 하고 페이지 렌더링
    #         ~
    #     elif request.form.get('sub') == '-':
    #         # - 버튼일 경우만 true
    #         # 세션의 count가 1보다 크면 -1 하고 페이지 렌더링
    #         ~
    #
    #     else:
    #         # 전부 아니므로 구매 버튼일 경우가 됨
    #         # 스토어에서 구매 함수 실행후 업데이트
    #         ~
    #         del session['count']
    #         return redirect(url_for('board', s_id = s_id))

    # return render_template('buy.html',
    #                        s_id=s_id, p_id = p_id,
    #                        product = product,
    #                        count = session['count']
    #                        )


if __name__ == '__main__':
    app.run('0.0.0.0',9999, debug=True)