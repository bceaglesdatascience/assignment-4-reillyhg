purchases=int(input("Number of purchases: "))
sales_tax=float(input("Sales tax: "))
tax=sales_tax

customers=[]
cost=[]

for i in range(purchases):
    customer=input("Customer: ")
    price=float(input("Cost: "))
    customers.append(customer)
    cost.append(price)

def  add_tax(list_cost, tax):
    taxed_items=[]
    for price in list_cost:
        taxed_items.append(price*(1+tax))
    return taxed_items

taxed_prices= add_tax(cost, tax)

total_purchases={}

for i in range(purchases):
    if customers[i] not in total_purchases:
        total_purchases[customers[i]]=0
    total_purchases[customers[i]]+=round(taxed_prices[i], 2)
                    
print(total_purchases)

