from dataclasses import dataclass

@dataclass(frozen=True)
class Dishes:
    amount: int
    name: str
    price: int
    weight: int

dish1 = Dishes(15, 'Salad', 8, 180)
dish2 = Dishes(25, 'Fries', 10, 250)
dish3 = Dishes(30, 'Steak', 15, 235)

class Order:


    def __init__(self):
        self.sum = 0
        self.weight = 0
        self.price = 0
        self.amount = 0
        self.lst = []
        self.cash = 0


    def characteristic(self,*args) -> int:
        #передаем в список оргументы dish
        self.lst = [args]
        
        for i in self.lst:
            for j in i:
                self.amount += j.amount
                self.price += j.price
                self.weight += j.weight
            return self.amount, self.price, self.weight


    def payment(self, cash):
        self.cash = int(cash)
        self.sum = self.price - self.cash
        # print(self.sum)


        if self.sum > 0:
            print(f'You need to pay {self.sum}$')
        elif self.sum == self.cash:
            print(f'Thanks for ur payment ')
        elif self.cash > self.price:
            # change = self.cash - self.sum
            print(f'Thanks for ur payment, that is ur change {abs(self.sum)}$')
        else:
            print(f'Your order, thanks for your payment {self.price}$')


first_order = Order()
first_order.characteristic(dish1,dish3)

print(first_order.amount)
print(first_order.price)
print(first_order.weight)

first_order.payment(0)
first_order.payment(20)
first_order.payment(25)

