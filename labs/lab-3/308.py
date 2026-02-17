class Account:
    def __init__(self , owner , balance, amount):
        self.owner = owner
        self.balance = balance
        self.amount = amount   
    def withdraw(self):
        if self.amount > self.balance:
            return "Insufficient Funds"
        else:
            return self.balance - self.amount 
        
b , w = map(int, input().split())
sek = Account("Yertay", b , w)
print(sek.withdraw())
