~

class AiStore:

    def __init__(self, name, s_id, locate, products_num, inventory):
        ~
    def set_product(self, p_id, count, price):
        # if in 을 사용하기위해선 시리즈를 배열로 바꿔야할것 문서 참고
        # try 문사용 가능
        # 쿼리후 개수로 파악 가능
        ~

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

if __name__ == '__main__':

    s_df = pd.read_csv('./stores.csv')
    ~
    p_df = pd.read_csv('./products.csv')
    ~
    iv_df = pd.read_csv('./inventory.csv')


    print('1 - 스토어 생성')
    print('2 - 스토어 리스트 출력')
    print('3 - 스토어 정보 출력')
    print('4 - 상품 구매')
    print('5 - 상품 관리')
    print('6 - csv 파일로 스토어, 재고현황 파일 출력')
    print('7 - 상품명별 전체 재고 개수 출력')


    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요: ')
        if input1 == '1':
            create_store()
        elif input1 == '2':
            show_list()
        elif input1 == '3':
            show_store()
        elif input1 == '4':
            buy()
        elif input1 == '5':
            manager_product()
        elif input1 == '6':
            ~
        elif input1 == '7':
            products_counts()
        else:
            print('존재하지 않는 명령어 입니다.')