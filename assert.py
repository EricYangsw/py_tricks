

# case1
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <=product['price'] #False for trigger error
    return price

shoes = {'name':'Fancy Shoes', 'price': 14900}

print(apply_discount(shoes, 0.25))
# print(apply_discount(shoes, 2))
print(__debug__)

# case 2
name = [
 'a',
 'b',
 'c',
 'd',




]
