from datetime import datetime,timedelta

class Article:
    def __init__(self, name,code,prix):
        self.name = name
        self.code = code
        self.price = prix

    def get_discount_price(self,discount=0):
           discount_price = (self.price /100) * discount
           new_price = self.price - discount_price
           return new_price
        


class Fruits(Article):
     def __init__(self,name,code,prix,fruit_category,end_date,origine):
          super().__init__(name,code,prix)
          self.fruit_category = fruit_category
          self.end_date = end_date
          self.origine = origine

     def alert(self):
          date_format = '%Y/%m/%d'
          formatted_end_date = datetime.strptime(self.end_date, date_format)
          current_date = datetime.now()
          seven_days_before = formatted_end_date - timedelta(weeks=1)
          if current_date.date() == seven_days_before.date():
               alert = print('Alert: The fruit is about to expire')
               return alert
     
          

    
fruits1 = Fruits("Apple", 12345, 2, "Fruits", "2024/08/29", "Spain")
fruits1.alert()
print(fruits1.get_discount_price(20))


class Feculenh(Article):
    def __init__(self, name, code, prix, prix_per_kilo, complet_cereal):
        super().__init__(name, code, prix)
        self.prix_per_kilo = prix_per_kilo
        self.complet_cereal = complet_cereal
    
    def price_per_bag(self,bag_weight):
        price_per_bag = self.prix_per_kilo * bag_weight
        return price_per_bag
    
feculenh1 = Feculenh("Potato", 52566245, 0.10, 1.3, False)
print(feculenh1.price_per_bag(10))
          