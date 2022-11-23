import pandas as pd
import json

class Customer:

    def __init__(self, customer, accounts):
        self.customer = customer # series
        self.accounts = accounts # dataframe

    def add_amount(self, a_id, amount):
        ~

    def sub_amount(self, a_id, amount):
        ~

    def add_account(self, a_id):
        ~

    def get_total_amount(self,):
        ~

    def get_rat(self):
        total_amount = self.get_total_amount()
        if total_amount > 100000:
            rat = 'vvip'
        elif total_amount > 10000:
            rat = 'vip'
        elif total_amount > 1000:
            rat = 'gold'
        elif total_amount > 100:
            rat = 'silver'
        else:
            rat = 'bronze'

        return rat

    def update(self, c_df, a_df):
        ~
    def get_name(self):
        return self.customer['name']

    def get_cid(self):
        return self.customer['c_id']

    def get_accounts(self):
        return self.accounts

    def get_customer(self):
        return self.customer


def create_customer():
    c_name = input('고객 이름 입력:')
    c_id = input('고객 번호 입력:')

    ~
    # c_df.loc[c_df['c_id'] == c_id] = customer
    # pd.concat([c_df, pd.DataFrame([customer])], ignore_index=False)
    print('{} 고객이 생성 되었습니다.'.format(c_name))


def show_list():
    for customer in ~:
        print('고객이름:{} 고객번호:{}'
              .format(customer['name'],
                      customer['c_id'],
                      ))


def search_customer(c_id):
    ~


def create_acount():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    acount_num = input('계좌번호 입력:')
    ~
    print('{} 고객의 {} 계좌가 등록되었습니다'
          .format(customer.get_name(),
                  acount_num,
                  ))


def show_customer():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    print('{} 고객님 등급:{} 총금액:{} 계좌정보:\n{}'
          .format(customer.get_name(),
                  customer.get_rat(),
                  customer.get_total_amount(),
                  customer.get_accounts()
                  ))


def deposit():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    acount_num = input('계좌번호 입력:')
    amount = input('입금할 금액 입력:')
    ~

def withdraw():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    acount_num = input('계좌번호 입력:')
    amount = input('출금할 금액 입력:')
    ~

def ca_merge():
    ~


def group_rat_count():
    ~



if __name__ == '__main__':

    ~
    print(c_df.dtypes)
    ~
    print(a_df.dtypes)

    print('1 - 고객 생성')
    print('2 - 계좌 생성')
    print('3 - 입금')
    print('4 - 출금')
    print('5 - 생성된 고객 리스트 출력')
    print('6 - 고객 정보 출력')
    print('7 - csv 파일로 고객 정보 출력')
    print('8 - csv 파일로 계좌 정보 출력')
    print('9 - csv 파일로 고객 - 계좌 정보 출력')
    print('10 - 등급별 고객의 명수 출력')

    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요')
        if input1 == '1':
            create_customer()
        elif input1 == '2':
            create_acount()
        elif input1 == '3':
            deposit()
        elif input1 == '4':
            withdraw()
        elif input1 == '5':
            show_list()
        elif input1 == '6':
            show_customer()
        elif input1 == '7':
            ~
        elif input1 == '8':
            ~
        elif input1 == '9':
            ca_merge()
        elif input1 == '10':
            group_rat_count()

        else:
            print('존재하지 않는 명령어 입니다.')
