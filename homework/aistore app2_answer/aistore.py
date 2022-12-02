import pandas as pd

s_df = pd.read_csv('./static/stores.csv')
s_df = s_df.set_index('s_id', drop=False)
p_df = pd.read_csv('./static/products.csv')
iv_df = pd.read_csv('./static/inventory.csv')

class AiStore:

    def __init__(self, name, s_id, locate, products_num, inventory):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products_num = products_num
        self.inventory = inventory

    def add_product(self, p_id, count, price, idx):
        n_product = {'p_id': p_id, 'count': count, 'price': price, 's_id': self.s_id}
        self.inventory.loc[idx] = n_product
        self.products_num = len(self.inventory)
        return n_product

    def set_product(self, p_id, count, price):
        product =  self.inventory[self.inventory['p_id'] == p_id]
        product['count'] += count
        product['price'] = price
        self.inventory.update(product)
        print(self.inventory)
    def is_product(self, p_id):
        product = self.inventory[self.inventory['p_id'] == p_id]
        if len(product) == 0:
            return False
        else:
            return True
    def buy_product(self, p_id, count):
        product =  self.inventory[self.inventory['p_id'] == p_id]
        product = product[product['count'] > count]
        if len(product) == 0:
            return

        product['count'] -= count
        self.inventory.update(product)

    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products_num(self):
        return self.products_num

    def get_inventory(self):
        return self.inventory
    def get_menu(self):
        menu = []
        for product in self.inventory.iloc:
            p_id = product['p_id']
            p_name = product['product']
            price = product['price']
            count = product['count']
            menu.append({'p_name': p_name, 'price': int(price), 'count': int(count), 'p_id':p_id})

        return menu

    def get_product(self, p_id):
        product = self.inventory[self.inventory['p_id'] == p_id]
        if len(product) == 0:
            return None
        product = product.iloc[0]
        p_id = product['p_id']
        p_name = product['product']
        price = product['price']
        count = product['count']
        return {'p_name': p_name, 'price': int(price), 'count': int(count), 'p_id':p_id}



def create_store(s_id, s_name, locate):

    store = {'s_id': s_id, 'name': s_name,
             'locate': locate,
             'products_num': 0,}

    s_df.loc[s_id] = store
    print('{} 스토어가 생성 되었습니다.'.format(store['name']))


def show_list(s_id = None):
    if s_id is None:
        return s_df.to_dict('records')
    else:
        return s_df[s_df['s_id'] == s_id].to_dict('records')

def search_store(s_id):
    print(iv_df)
    print(s_id)
    if s_id in s_df.index:
        store = s_df.loc[s_id]
        inventory = iv_df[iv_df['s_id'] == s_id]
        print(inventory)

        inventory = inventory.join(p_df.set_index('p_id'), on='p_id')
        return AiStore(store['name'],
                       store['s_id'],
                       store['locate'],
                       store['products_num'],
                       inventory)
    else:
        print('스토어를 찾지 못했습니다.')
        return None

def get_products():
    return p_df.to_dict('records')

def set_product(store, p_id, price, count):
    print(p_id)
    print(iv_df)
    if store.is_product(p_id):
        store.set_product(p_id, int(count), int(price))
    else:
        idx = len(iv_df)
        n_product = store.add_product(p_id, int(count), int(price), idx)
        iv_df.loc[idx] = n_product
        print('add',iv_df)

def update(store: AiStore):
    s_df[store.get_id()] = {'s_id': store.get_id(),
                       'name': store.get_name(),
                       'locate': store.get_locate(),
                       'products_num': store.get_products_num(), }
    iv_df.update(store.get_inventory())

