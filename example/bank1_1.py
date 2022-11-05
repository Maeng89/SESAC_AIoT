class Customer:

    def __init__(self, name, id):
       self.name = name
       self.id = id
       self.amount = 0

    def add_amount(self, add):
        self.add = add
        self.amount += add

    def sub_amount(self, sub):
        self.sub = sub
        self.amount -= sub

    def get_name(self):
       return self.name

    def get_id(self):
       return self.id

    def get_amount(self):
       return self.amount


if __name__ == '__main__': # 메인함수의 선언, 시작을 의미

    c_name = input('고객 이름 입력:')
    c_id = input('고객 번호 입력:')
    customer = Customer(c_name, c_id)
    print(customer.get_name() + ' 고객이 생성 되었습니다.') # '{고객이름} 고객이 생성 되었습니다' 출력

    amount = int(input('입금 금액 입력'))
    customer.add_amount(amount)

    amount = int(input('출금 금액 입력'))
    customer.sub_amount(amount)

    print(f"고객 이름 {customer.get_name()}, 고객 번호 {customer.get_id()}, 계좌 금액 {customer.get_amount()}") # '고객이름, 고객아이디, 계좌금액' 출력
