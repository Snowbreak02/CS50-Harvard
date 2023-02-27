class Vault:
    def __init__(self, dollars=0, cents=0, penny=0):
        self.dollars = dollars
        self.cents = cents
        self.penny = penny

    def __str__(self):
        return f"{self.dollars} dollars, {self.cents} cents, {self.penny} penny"

    def __add__(self, other): #overloading the + sign below, combining both of them tgt
        dollars = self.dollars + other.dollars
        cents = self.cents + other.cents
        penny = self.penny +other.penny



jeremy = Vault(100, 50, 20)
print(jeremy)

shawn = Vault(1000, 500, 25)
print(shawn)

total = jeremy + shawn # as + is an add operator, it will call the __add__ overload operator above
print(total)