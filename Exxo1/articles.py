class Article:
    def __init__(self, name,code,prix):
        self.name = name
        self.code = code
        self.price = prix

    def get_discount_price(self,discount=0):
           discount_price = (self.price /100) * discount
           new_price = self.price - discount_price
           return new_price
        

article1 = Article('Tasse', 12345, 100)
print(article1.get_discount_price(20))

    
