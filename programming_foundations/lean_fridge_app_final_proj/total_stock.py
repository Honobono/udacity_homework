import single_item_stock

class Total_Stock(object):
    def __init__(self):
        self.stock = {}

    def add_produce(self, produce_name, purchase_date, item_count, additional_note):
        if produce_name not in self.stock:
            self.stock[produce_name] = single_item_stock.Single_Item_Stock(produce_name)
        # should be out of the if statement bc existing produce_names need to be updated too
        self.stock[produce_name].add_stock(purchase_date, item_count, additional_note)

    def to_buy_list(self):
        # return a list of produce items that total_item_count falls dangerously down to 1 or less.   
        to_buy_list = []
        for produce_name in self.stock:
            if self.stock[produce_name].total_count() <= 1:
                to_buy_list.append(produce_name)

        return to_buy_list

    def __str__(self):
        string = ""
        for key, value in self.stock.items():
            string += str(value) + "\n"
        return string




if __name__== '__main__':
    fridge = Total_Stock()
    fridge.add_produce('apple', 20151216, 2, 'Fuji')
    fridge.add_produce('apple', 20151217, 3, 'Pinklady')
    fridge.add_produce('banana', 20151211, 4, 'none')
    fridge.add_produce('dragon fruit', 20151214, 1, 'sweet')
    print fridge
    print fridge.to_buy_list()
    
