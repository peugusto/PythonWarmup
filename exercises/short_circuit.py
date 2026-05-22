def calc(x,y,z):
    if x > 3000 and y > 600 : return True
    elif z == True : return True
    else: return False


if __name__ == "__main__":
    print(calc(400,100,True)) #true
    print(calc(3600,700,False)) #true
    print(calc(299,299,False)) #false

