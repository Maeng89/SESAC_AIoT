import pandas as pd

# 인스턴스를 어디서 생성하고, 어느 함수가 사용하는지 체크하자
# 점포 검색시 점포 인스턴스 생성


############ 클래스 정의 ############
class AiStore:

    def __init__(self, name, s_id, locate, products_num, inventory):
        self.name = name # value
        self.s_id = s_id # value
        self.locate = locate # value
        self.products_num = products_num # value
        self.inventory = inventory # dataframe

# 점포관리에서 객체
    def set_product(self, p_id, count, price):
        # if in 을 사용하기위해선 시리즈를 배열로 바꿔야할것 문서 참고
        # try문 사용 가능
        # 쿼리후 개수로 파악 가능
        ~
        # if product in self.products :
        #     self.products[product] += int(count)
        #     self.prices[product] = int(price)
        # else :
        #     self.products[product] = int(count)
        #     self.prices[product] = int(price)

    def buy_product(self, p_id, count, amount):
        ~

    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products_num(self):
        return self.products_num

    def show_products(self, p_df):
        ~

    def get_price(self, p_id):
        product =  self.inventory[self.inventory['p_id'] == p_id]
        if len(product) == 0:
            return None

        return product['price'].iloc[0]

    def update_data(self, s_df, iv_df):
        ~
        
############ 커머스 모듈 프로세스 ############
def create_store():
    s_name = input('스토어 이름 입력: ')
    s_id = input('스토어 번호 입력: ')
    locate = input('스토어 위치 입력: ')
    ~
    print('{} 스토어가 생성 되었습니다.'.format(store['name']))


def show_list():
    ~

def search_store(s_id):
    ~


def show_store():
    s_id = input('스토어 번호 입력: ')
    ~
def buy():
    s_id = input('스토어 번호 입력: ')
    ~
    p_id = input('상품 아이디 입력:')
    count = input('구매 개수 입력: ')
    count = int(count)
    ~
    price = input('가격 입력: ')
    ~
def manager_product():

    s_id = input('스토어 번호 입력: ')
    ~

    p_id = input('상품 아이디 입력: ')
    count = input('재고 개수 입력: ')
    price = input('상품 가격 입력: ')

    ~


import json
def products_counts():
    ~
    print(pc_df)


############ 실행 프로세스 ############
if __name__ == '__main__':
###### 데이터 준비 ######
    # 'stores.csv’ 를 불러와서 s_df에 데이터프레임으로 할당
    # set_index 함수를 활용해 ‘s_id’ 컬럼을 인덱스로(’s_id’ 컬럼유지)
    s_df = pd.read_csv('stores.csv')
    s_df.set_index('s_id', drop=False, inplace=True)  # drop=false는 인덱스로 활용된 칼럼 유지
    print(s_df.dtypes,'상점 데이터 불러오기 성공')

    # ‘products.csv’ 를 불러와서 p_df에 데이터프레임으로 할당
    # set_index 함수를 활용해 ‘p_id’ 컬럼을 인덱스로(’p_id’ 컬럼삭제)
    p_df = pd.read_csv('products.csv')
    p_df.set_index('p_id', inplace=True)
    print(p_df.dtypes, '상품 데이터 불러오기 성공')

    # ‘inventory.csv’ 를 불러와서 iv_df에 데이터프레임으로 할당
    # 순서 인덱스 유지
    iv_df = pd.read_csv('inventory.csv')
    print(iv_df.dtypes, '재고 데이터 불러오기 성공')

###### 스토어 메뉴 안내 ######

    print('1 - 스토어 생성')
    print('2 - 스토어 리스트 출력')
    print('3 - 스토어 정보 출력')
    print('4 - 상품 구매')
    print('5 - 상품 관리')
    print('6 - csv 파일로 스토어, 재고현황 파일 출력')
    print('7 - 상품명별 전체 재고 개수 출력')
    print('0 - 커머스 종료')

    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요: ')
        if input1 == '1': # 스토어 생성
            create_store()
        elif input1 == '2': # 스토어 리스트 출력
            show_list()
        elif input1 == '3': # 스토어 정보 출력
            show_store()
        elif input1 == '4': # 상품 구매
            buy()
        elif input1 == '5': # 상품 관리
            manager_product()
        elif input1 == '6': # csv 파일로 스토어, 재고현황 파일 출력
            ~
        elif input1 == '7': # 상품명별 전체 재고 개수 출력
            products_counts()
        elif input1 == '0':
            print('커머스 종료')
            break
        else:
            print('존재하지 않는 명령어 입니다.')