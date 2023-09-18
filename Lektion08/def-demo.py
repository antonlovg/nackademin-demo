# Övning

def minimun(lista):
    minsta_talet = lista[0]
    for i in lista:
        if(minsta_talet > i):

            minsta_talet = i
    return minsta_talet

my_list = [10, 2, 5, 50]
print(minimun(my_list))