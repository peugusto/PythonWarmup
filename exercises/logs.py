def process():
    log = [32,-141,"ERRO", None, 0, 8, 10, 11, 10, -20, 40000 , 6]
    final_balance = 0

    print('starting the log')

    for i in log:
        if i == "ERRO" : continue
        if i == None : continue

        if i > 10000 : break;

        final_balance += i
        

    print('\n The process was interruped')
    password = ""
    while password != "admin123":
        password = input("Enter your password: ");
    
    print(f"Final Balance: {final_balance:.2f}")


if __name__ == "__main__":
    process()
