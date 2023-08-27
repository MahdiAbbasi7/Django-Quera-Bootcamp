"""َassert tutorial"""

Tshirt ={'name':'Mahdi', 'price':100}

def apply_discount(product, discount):
    price_after_discount = product['price'] - discount
    assert 0 <= price_after_discount <= product['price'] , " Sorry "#for error 
    return price_after_discount

print(apply_discount(Tshirt,1000))

# x = 4

# assert x==5
# print("x is equal 5")