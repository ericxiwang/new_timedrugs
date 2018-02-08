from flask import session
from models import product_info, pro_discount


class shopping_cart:
    '''def __init__(self):

        #self.item_list = session['item_list']
        self.item_list = []'''

    def add_item(self, pro_code, pro_quantity):

        each_pro = {'pro_code': pro_code, 'pro_quantity': pro_quantity}

        if 'item_list' in session:
            item_list = session['item_list']
            item_list.append(each_pro)
            session['item_list'] = item_list
            return session['item_list']
        else:
            session['item_list'] = []
            session['item_list'].append(dict(each_pro))
            return session['item_list']

    def remove_item(self, pro_code):
        all_items = session['item_list']
        for each_item in all_items:
            if each_item['pro_code'] == pro_code:
                all_items.remove(each_item)
        session['item_list'] = all_items
        return session['item_list']

    def checkout(self):
        pass

    def clear_item(self):
        self.item_list = []
        return self.item_list

    def session_merge(self):

        if session['user_email']:
            session['item_list'] = self.item_list

    def item_list_all(self):
        new_item = {}
        if session['item_list']:
            list_all = []

            for each_line in session['item_list']:
                each_item = product_info.query.filter_by(pro_code=each_line['pro_code']).first()

                #put data from query to a new dict 'new_item'
                new_item['pro_code'] = each_item.pro_code
                new_item['pro_img'] = each_item.pro_img
                new_item['pro_name'] = each_item.pro_name
                new_item['pro_o_price'] = each_item.pro_o_price
                new_item['pro_quantity'] = each_line['pro_quantity']

                # if current item has promotion, put related data into 'new_item'
                if each_item.promotion_id != 0:

                    new_item['pro_promotion'] = self.get_promotion(each_item.promotion_id,
                                                                   pro_o_price=each_item.pro_o_price,
                                                                   pro_quantity=each_line['pro_quantity'],
                                                                   pro_weight=each_item.pro_weight)
                # if current item has no promotion, just insert a empty dict into 'new_item
                else:
                    new_item['pro_promotion'] = dict()

                list_all.append(dict(new_item))



        else:
            all_item_list = 'no item'
            list_all = 'no item'

        return list_all

    def get_promotion(self, promotion_id, **kwargs):
        for k, v in kwargs.items():
            print k, v
            exec (k + '=v')

        promotion_suit = dict()
        current_discount = pro_discount.query.filter_by(promotion_id=promotion_id).first()

        # =========== discount =========
        if current_discount.pro_type == 1:
            discount_precentage = current_discount.discount_value
            final_price = pro_o_price * discount_precentage * 0.01

            total_price = float(final_price) * int(pro_quantity)
            total_weight = float(pro_weight) * int(pro_quantity)

            promotion_suit = {'pro_type': '1',
                              'final_price': final_price,
                              'total_price': total_price,
                              'total_weight': total_weight}

        # =========== buy and get
        elif current_discount.pro_type == 2:
            pro_buy = current_discount.pro_buy
            pro_get = current_discount.pro_get
            real_get = int(float(pro_quantity) / float(pro_buy)) * int(pro_get)
            final_quantity = int(pro_quantity) + int(real_get)

            total_weight = pro_weight * final_quantity
            total_price = pro_o_price * int(pro_quantity)

            promotion_suit = {'pro_type': '2',
                              'pro_quantity': int(pro_quantity),
                              'real_get': int(real_get),
                              'total_price': total_price,
                              'total_weight': total_weight}

        # ============ special price ======
        elif current_discount.pro_type == 3:
            pro_price = current_discount.pro_price
            total_price = pro_price * pro_quantity
            total_weight = pro_weight * pro_quantity
            promotion_suit = {'pro_type': '3',
                              'pro_o_price': pro_o_price,
                              'pro_price': pro_price,
                              'total_price': total_price,
                              'total_weight': total_weight}

        # ============ free shipping ======
        elif current_discount.pro_type == 4:
            total_weight = 0
            total_price = pro_o_price * pro_quantity
            promotion_suit = {'pro_type': '4',
                              'total_price': total_price,
                              'total_weight': total_weight}

        else:
            print "no promotion"
        return promotion_suit


if __name__ == "__main__":
    a = shopping_cart()
    a.add_item('sdfsfsd', 6)
    a.add_item('sfsfsdf', 5)
