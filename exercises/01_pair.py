def pair(setence : str):

    splited_setence = setence.split(" ")
    
    dict = {}

    for product in splited_setence:
        dict[product] = dict.get(product , 0) + 1

    print(dict)

def remove_duplicates(lista : list):
    new_list = list(set(lista))

    print(new_list)


def frequency(n : list):
    dict = {}

    for i in n:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    mais_frequente = None
    maior_quantidade = 0

    for num, qtd, in dict.items():
        if qtd > maior_quantidade:
            maior_quantidade = qtd
            mais_frequente = num
     
    print(mais_frequente)

def palindrome(x : str):
    initial = 0
    end = len(x) - 1
    
   
    while initial < end:
        if x[initial] != x[end] : 
            return False
            
        initial += 1
        end -= 1

    return True
        
def even(x : list):
    even_list = []
    for i in x:
        if i % 2 == 0 : even_list.append(i)

    print(even_list)


def find_by_id(x : int):
    users = [ 
        {
        "id":1, 
        "nome": "Pedro"
         },
        {
        "id":2, 
        "nome": "Sergio"
         },
        {
        "id":3, 
        "nome": "Jorge"
         },
    ]
    isExist = False
    
    for i in users:

        if i["id"] == x:
            isExist = True
            print(i)

    if not isExist : 
        print("user not found")

if __name__ == "__main__":

    #pair("banana banana maca uva pera banana uva")

    #remove_duplicates([1,2,3,3,3,4,5,6,7,1,23])

    #frequency([1,1,1,2,2,2,42,1])

    #print(palindrome("arara"))

    #even([1,2,3,4,5,6,7,8,9])

    #find_by_id(4)
