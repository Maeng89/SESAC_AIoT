class AiStore:

    def __init__(self, name, id, locate):
        self.name = name
        self.s_id = id
        self.locate = locate
        self.count = 0
        self.price = 0

    def set_product(self, count, price):
        self.count = count
        self.price = price

    def buy_item(self, b_count, input_amount):
        self.count -= b_count
        need_amount = self.price * b_count
        balance = need_amount - input_amount
        print(f'잔돈은 {balance}입니다.')
        if self.count < 0 :
            print(f'재고가 {self.count}만큼 부족합니다.')
        elif input_amount < need_amount :
            print(f'입력 금액이 {balance}만큼 부족합니다.')

    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_count(self):
        return self.count

    def get_price(self):
        return self.price


if __name__ == '__main__':

    s_name = input('스토어 지점이름 입력:')
    s_id = input('스토어 지점번호 입력:')
    locate = input('스토어 위치 입력:')

    store = AiStore(s_name, s_id, locate)
    print(store.get_name() + ' 스토어가 생성 되었습니다.')

    for i in range(10):

        print('스토어 조회는 1번, 구매는 2번, 상품 관리는 3번, 종료는 4번 을 눌러주세요')
        num = input()
        if num =='1':
           print('스토어 지점이름 :', store.get_name())
           print('스토어 지점번호 :', store.get_id())
           print('스토어 지점위치 :', store.get_locate())
           print('스토어 상품개수 :', store.get_count())
           print('스토어 상품가격 :', store.get_price())

        elif num == '2':
            count = int(input('구매할 상품 개수 입력'))
            print(f'구매 상품 개수는 {count}입니다.')
            need_price = store.get_price() * count
            print(f'구매 필요 금액은 {need_price}입니다.')
            amount = input(str(need_price) + ' 금액을 입금해 주세요')
            store.buy_item(count, need_price)

        elif num == '3':
            p_stock = int(input('상품 개수 입력'))
            p_price = int(input('상품 가격 입력'))
            store.set_product(p_stock, p_price)
            print(f'입력된 상품 개수는 {store.get_count()}이고 상품 가격은 {store.get_price()}입니다.')

        elif num == '4':
            print('종료합니다')
            break
        else:
            print('잘못된 입력입니다')