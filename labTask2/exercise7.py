products=[{"name":"Laptop","price":90000,"quantity":3},{"name":"PC","price":50000,"quantity":5},
         {"name":"Phone","price":80000,"quantity":2},{"name":"Drone","price":20000,"quantity":7}]
total=0
for i in products:
    total=total+i["price"]*i["quantity"]
def apply_discount(total):
    if total>=2000:
        discount=total*0.10
        final_price=total-discount
        print("final price:",final_price)
    else:
        print("no discount")
apply_discount(total)        
    

