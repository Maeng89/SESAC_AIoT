# - 모듈 프로세스
#     - txt_to_store 함수 수정
#         - open()함수를 이용하여 stores.txt 파일 데이터 불러오기
#         - stores.txt 파일의 줄바꿈 기준으로 이름과 아이디를 가지는 스토어 리스트 생성
#         - readlines() 함수와 for 문을 이용할것
#         - store_list 리스트에 AiStore 인스턴스로 담길것
#     - store_to_json 함수 수정
#         - 딕셔너리 구조를 활용하여 모든 스토어 정보를 입력받은 path에 json으로 저장
#         - 변경한 재고 및 가격 정보도 포함되어야 함
#     - __main__ 구간 수정
#         - 6번 옵션구현
#         - 7번 옵션 구현

class AiStore:

    def __init__(self, name, s_id, locate):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products = {'커피':10}
        self.prices = ~

    def set_product(self, product, count, price):
        ~

    def buy_product(self, product, count, amount):
        ~


    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products(self):
        return self.products

    def get_prices(self):
        return self.prices

def create_store():
    s_name = input('스토어 이름 입력: ')
    s_id = input('스토어 아이디 입력: ')
    locate = input('스토어 위치 입력: ')
    ~
    print('{} 스토어가 생성 되었습니다.'.format(store.get_name()))
    return ~


def show_list():
    for store in store_list:
        print('스토어 이름:{} 스토어 아이디:{} 스토어 위치:{}'
              .format(~,
                      ~,
                      ~
                      ))

def search_store(s_id):
    ~

    print('스토어 아이디를 찾지 못했습니다.')
    return None


def show_store():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    print('{} 스토어 재고 현황: {}'
          .format(~,
                  ~
                  ))
    print('{} 스토어 가격 현황: {}'
          .format(~,
                  ~
                  ))

def buy():
    s_id = input('스토어 아이디 입력: ')
    ~
    product = input('상품 입력:')
    count = input('구매 개수 입력: ')
    # 옵션 '총 가격은 {} 입니다.' 출력
    price = input('가격 입력: ')
    ~

def manager_product():

    s_id = input('스토어 번호 입력: ')
    ~

    product = input('상품 입력: ')
    count = input('재고 개수 입력: ')
    price = input('상품 가격 입력: ')

    store.set_product(~)

def txt_to_store():
    pass


import json
def store_to_json():
    pass

if __name__ == '__main__':
    store_list = []

    print('1 - 스토어 생성')
    print('2 - 스토어 리스트 출력')
    print('3 - 스토어 정보 출력')
    print('4 - 상품 구매')
    print('5 - 상품 관리')
    print('6 - txt 파일로 스토어 생성')
    print('7 - json 파일로 스토어 정보 출력')


    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요: ')
        if input1 == '1':
            store = create_store()
            ~
        elif input1 == '2':
            ~
        elif input1 == '3':
            ~
        elif input1 == '4':
            ~
        elif input1 == '5':
            ~
        elif input1 == '6':
            pass
        elif input1 == '7':
            pass
        else:
            print('존재하지 않는 명령어 입니다.')