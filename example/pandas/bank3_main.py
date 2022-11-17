import pandas as pd
import json

class Customer:

    def __init__(self, customer, accounts):
        self.customer = customer # series
        self.accounts = accounts # dataframe

    def add_account(self, a_id):# id = 계좌번호
        if a_id in self.accounts[self.accounts.index]:
            print('해당 계좌가 이미 존재합니다')
        else:
            #  새로운 계좌 데이터 할당
            # 데이터프레임에 딕셔너리를 추가하려면 dict to df 하거나 dict to series(name할당)로 가능
            new_account_dict = {'a_id': a_id,
                              'password': None,
                              'c_id': self.customer['c_id'],
                              'amount': 0
                              }
            new_account_df = pd.DataFrame([new_account_dict])
            new_account_df.set_index('a_id', inplace=True)
            self.accounts.append(new_account_df)

            # 고객 계좌 개수 추가
            self.customer['account_num'] += 1
            # 데이터베이스 업데이트
            self.update(c_df, a_df)

    def add_amount(self, a_id, amount):
        # 해당 계좌번호의 계좌금액에 입금금액 추가
        self.accounts['amount'].loc[a_id] += amount
        # self.accounts.loc[aid, 'amount']
        # 고객의 총합금액과 등급 업데이트
        self.customer['total_amount'] = self.get_total_amount()
        self.customer['rat'] = self.get_rat()

        # 데이터베이스 업데이트
        self.update(c_df, a_df)

    def sub_amount(self, a_id, amount):
        # 해당 계좌번호의 계좌금액에서 출금금액 차감
        self.accounts['amount'].loc[a_id] -= amount

        # 고객의 총합금액과 등급 업데이트
        self.customer['total_amount'] = self.get_total_amount()
        self.customer['rat'] = self.get_rat()

        # 데이터베이스 업데이트
        self.update(c_df, a_df)

    def get_total_amount(self):
        # 고객의 모든 계좌의 총합 금액을 반환
        total_amount = self.customer['total_amount']
        return total_amount

    def update(self, c_df, a_df):
        # 클래스 내 수정된  데이터를 데이터 프레임에 업데이트
        c_df.loc[c_df['c_id'] == self.customer['c_id']] = self.customer
        a_df.loc[a_df['a_id'] == self.accounts['a_id']] = self.accounts
        # ad_df.update(self.account) 인덱스 같으면 업데이트하고 다르면 추가

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
                'rat': 'normal'
                }
    c_df.loc[c_id] = customer
    # pd.concat([c_df, pd.DataFrame([customer])], ignore_index=False)
    print('{} 고객이 생성 되었습니다.'.format(c_name))
    return c_df

def show_list():
    for customer in customer_obj_list:
        print('고객이름:{} 고객번호:{}'
              .format(customer.get_name(),
                      customer.get_cid(),
                      ))

def search_customer(c_id): # 객체 목록이 아니라, 데이터 프레임으로 데이터를 가져올 수 있도록.
    # for customer in customer_obj_list:
    #     if customer.get_cid() == c_id:
    #         print('고객이름:{} 고객번호:{}'
    #               .format(customer.get_name(),
    #                       customer.get_id()
    #                       ))
    # customer =
    # account =
            return Customer(customer, account)

    print('고객 번호를 찾지 못했습니다.')
    return None


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

# def csv_to_customers():
#     input_path = input('고객 csv파일 불러오기 경로 입력') # bank3_customers.csv
#     try : # 오류 모니터링 영역
#         c_df = pd.read_csv(input_path)
#     except :
#         print(f'고객 csv파일 불러오기 실패')
#     else : # 코드 실행 영역
#         c_df.set_index('c_id', inplace=True)
#         print(c_df)
#         print(f'고객 csv파일 불러오기 성공')
# 
# def csv_to_accounts():
#     input_path = input('계좌 csv파일 불러오기 경로 입력') # bank3_customers.csv
#     try : # 오류 모니터링 영역
#         a_df = pd.read_csv(input_path)
#     except :
#         print(f'계좌 csv파일 불러오기 실패')
#     else : # 코드 실행 영역
#         a_df.set_index('a_id', inplace=True)
#         print(a_df)
#         print(f'계좌 csv파일 불러오기 성공')



#         for c_idx in c_df.index: # 고객 객체 생성 및 목록 추가
#             c_obj = Customer(c_df[c_idx])
#             customer_obj_list.append(c_obj)

if __name__ == '__main__':
    customer_obj_list = []
###### 고객/계좌 데이터 준비(csv to dataframe) ######
    c_df = pd.read_csv('bank3_customers.csv') # index_col은 인덱스로 활용된 칼럼이 삭제됨
    c_df.set_index('c_id', drop = False, inplace=True) # drop=false는 인덱스로 활용된 칼럼 유지
    print('고객 csv파일 불러오기 성공')
    print(f'고객 데이터({c_df.dtypes}) 준비 완료')
    print(c_df)
    print('='*50)

    a_df = pd.read_csv('bank3_accounts.csv')
    a_df.set_index('a_id', drop = False, inplace=True)
    print(f'계좌 데이터({c_df.dtypes}) 준비 완료')
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
            customer = create_customer()
            customer_obj_list.append(customer) # 고객 객체 리스트
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
            # csv_to_customers() # index false 처리
        elif input1 == '8': # csv 파일로 계좌 정보 출력
            # csv_to_accounts()
        elif input1 == '9': # csv 파일로 고객 - 계좌 정보 출력
            ca_merge()
        elif input1 == '10': # 등급별 고객의 명수 출력
            group_rat_count()

        else:
            print('존재하지 않는 명령어 입니다.')
