from flask import session

class shopping_cart:

    '''def __init__(self):

        #self.item_list = session['item_list']
        self.item_list = []'''
    def add_item(self,pro_code,pro_quantity):

        each_pro = {'pro_code': pro_code, 'pro_quantity': pro_quantity}

        if 'item_list' in session:
            item_list = session['item_list']
            item_list.append(each_pro)
            session['item_list'] = item_list
            return session['item_list']
        else:
            session['item_list'] = []
            session['item_list'].append(each_pro)
            return session['item_list']



    def remove_item(self,pro_code):
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





if __name__ == "__main__":
    a = shopping_cart()
    a.add_item('sdfsfsd',6)
    a.add_item('sfsfsdf',5)

