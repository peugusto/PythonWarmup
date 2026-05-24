try:
    name = input("enter your name: ")
except ValueError as e:
    print("numbers are not allowed" + e)
else: 
    print("name: "+ name)
finally:
    print("end")