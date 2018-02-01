
class shopping_cart:

    def __init__(self):

        self.item_list = []

    def add_item(self,pro_code,pro_quantity):
        each_pro = {'pro_code':pro_code,'pro_quantity':pro_quantity}
        self.item_list.append(each_pro)

        return self.item_list

    def remove_item(self,pro_code):
        for each_pro in self.item_list:
            if each_pro['pro_code'] == pro_code:
                self.item_list.remove(each_pro)
            return self.item_list
    def checkout(self):
        pass
    def clear_item(self):
        self.item_list = []
        return self.item_list
    def session_merge(self):

        if session['user_email']:
            session['item_list'] = self.item_list



if __name__ == "__main__":
    a = shopping_cart_1()
    a.add_item('sdfsfsd',6)
    a.add_item('sfsfsdf',5)
    print a.item_list
