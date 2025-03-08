def compute_taxes(func):
    def inner(amount , tax):
        if amount>0 and amount<10000:
            tax = 0.18
        elif amount > 10000:
            tax = 0.25
        else:
            print("ivalid amount")
        return func( amount , tax)
    return inner
    
@compute_taxes
def pay(amount , tax):
    return amount + (amount*tax)

amount_to_pay = pay(90 ,0 )
print("amount_to_pay " , amount_to_pay)
