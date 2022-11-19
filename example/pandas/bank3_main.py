import pandas as pd
import json

class Customer:

    def __init__(self, customer, accounts):
        self.customer = customer # series
        self.accounts = accounts # dataframe

    def add_account(self, a_id):# id = 계좌번호
        if a_id in self.accounts.index:
            print('해당 계좌가 이미 존재합니다')
        else:
            #  새로운 계좌 데이터 할당
            self.accounts.loc[a_id] = {'a_id': a_id, 'amount': 0, 'c_id': self.customer['c_id']}
            # 고객 계좌 개수 추가
            self.customer['account_num'] += 1
            # 데이터베이스 업데이트
            self.update(c_df, a_df)

    def add_amount(self, a_id, amount):
        if a_id in self.accounts.index:
            # 해당 계좌번호의 계좌금액에 입금금액 추가
            self.accounts.loc[a_id, 'amount'] += amount
            # 고객의 총합금액과 등급 업데이트
            self.customer['total_amount'] = self.get_total_amount()
            self.customer['rat'] = self.get_rat()
            # 데이터베이스 업데이트
            self.update(c_df, a_df)
        else:
            print('해당 계좌가 없습니다')

    def sub_amount(self, a_id, amount):
        if a_id in self.accounts.index:
            if self.accounts.loc[a_id, 'amount'] > amount:
                # 해당 계좌번호의 계좌금액에서 출금금액 차감
                self.accounts.loc[a_id, 'amount'] -= amount
                # 고객의 총합금액과 등급 업데이트
                self.customer['total_amount'] = self.get_total_amount()
                self.customer['rat'] = self.get_rat()
                # 데이터베이스 업데이트
                self.update(c_df, a_df)
            else:
                print('계좌의 금액이 부족합니다.')
        else:
            print('해당 계좌가 없습니다')

    def get_total_amount(self):
        # 고객의 모든 계좌의 총합 금액을 반환
        return self.accounts['amount'].sum()

    def update(self, c_df, a_df):
        # 클래스 내 수정된 고객시리즈 데이터를 고객 데이터 프레임에 업데이트
        # c_df.loc[c_df['c_id'] == self.customer['c_id']] = self.customer
        # a_df.loc[a_df['a_id'] == self.accounts['a_id']] = self.accounts
        # 쿼리를 쓰면 너무 복잡하니 최대한 쉬운 방법으로 접근하자
        c_df.loc[self.customer['c_id']] = self.customer
        a_df.update(self.accounts) # 인덱스 같으면 업데이트하고 다르면 추가
         # for a_id in self.accounts.index:
        #     a_df.loc[a_id] = self.accounts.loc[a_id]

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
    customer = {'c_id': c_id,
                'name': c_name,
                'account_num': 0,
                'total_amount': 0,
                'rat': 'normal'}
    c_df.loc[c_id] = customer
    # pd.concat([c_df, pd.DataFrame([customer])], ignore_index=False)
    print('{} 고객이 생성 되었습니다.'.format(c_name))

def show_list():
    for customer in c_df.iloc:
        print('고객이름:{} 고객번호:{}'
              .format(customer['name'],
                      customer['c_id'],
                      ))

def search_customer(c_id):
    # 객체 목록이 아니라, 데이터 프레임으로 데이터를 가져올 수 있도록.
    if c_id in c_df.index:
        customer = c_df.loc[c_id]
        accounts = a_df[a_df['c_id'] == c_id]
        return Customer(customer, accounts)
    else :
        print('고객 번호를 찾지 못했습니다.')
        return None

def create_acount():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    acount_num = input('계좌번호 입력:')
    customer.add_account(acount_num)
    customer.update(c_df, a_df)

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

    account_num = input('계좌번호 입력:')
    amount = int(input('입금할 금액 입력:'))
    customer.add_amount(account_num, amount)
    customer.update(c_df, a_df)

def withdraw():
    c_id = input('고객 번호 입력:')
    customer = search_customer(c_id)
    if customer is None:
        return

    account_num = input('계좌번호 입력:')
    amount = int(input('입금할 금액 입력:'))
    customer.sub_amount(account_num, amount)
    customer.update(c_df, a_df)

def ca_merge():
    # 병합을 위해 인덱스를 통일해야 함
    # merge_df = c_df.merge(a_df, on='c_id', how='left')
    merge_df = c_df.join(a_df.set_index('c_id'))
    merge_df.to_csv('ca_merge.csv', index=False)

def group_rat_count():
    group = c_df[['c_id', 'rat']].groupby(by='rat').count()
    group = group.rename(columns = {'c_id':'count'})
    print(group)



if __name__ == '__main__':
###### 고객/계좌 데이터 준비(csv to dataframe) ######
    c_df = pd.read_csv('bank3_customers.csv') # index_col은 인덱스로 활용된 칼럼이 삭제됨
    c_df.set_index('c_id', drop = False, inplace=True) # drop=false는 인덱스로 활용된 칼럼 유지
    print('고객 데이터 임포트 성공')
    print(c_df)
    print('='*50)

    a_df = pd.read_csv('bank3_accounts.csv')
    a_df.set_index('a_id', drop = False, inplace=True)
    print('계좌 데이터 임포트 성공')
    print(a_df)
    print('=' * 50)

###### 뱅킹 메뉴 안내 ######
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
        if input1 == '1': # 고객 생성
            create_customer()
        elif input1 == '2': # 계좌 생성
            create_acount()
        elif input1 == '3': # 입금
            deposit()
        elif input1 == '4': # 출금
            withdraw()
        elif input1 == '5': # 생성된 고객 리스트 출력
            show_list()
        elif input1 == '6': # 고객 정보 출력
            show_customer()
        elif input1 == '7': # csv 파일로 고객 정보 출력
            c_df.to_csv('customers_export.csv', index= False)
        elif input1 == '8': # csv 파일로 계좌 정보 출력
            a_df.to_csv('accounts_export.csv', index= False)
        elif input1 == '9': # csv 파일로 고객 - 계좌 정보 출력
            ca_merge()
        elif input1 == '10': # 등급별 고객의 명수 출력
            group_rat_count()

        else:
            print('존재하지 않는 명령어 입니다.')