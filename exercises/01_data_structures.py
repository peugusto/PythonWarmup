def func():
    storage = {"apple" : {"price": 2 , "qtd": 10},
               "cake" : {"price": 10 , "qtd": 3},
               "banana" : {"price":  1, "qtd": 20},
               "water" : {"price": 2.5 , "qtd": 10},}
    
    daily = [("apple", 2),("water",4)]

    for produto, qtd in daily:
        if produto in storage:
            price = storage[produto][price]
            


if __name__ == "__main__":
    func()