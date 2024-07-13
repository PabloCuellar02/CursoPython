""""
resp='S'

while resp=='S':
    num=input('Introduce un numero: ')
    num=int(num)

    if (num %2 == 0):
        print('El numero es par')
    else:
        print('El numero es impar')
    
    resp=input('Quieres continuar? S/N: ').upper()
"""

def bubble_short(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                print(list)
    return list

list=[3,45,9,23,4]
bubble_short(list)

print(3 <= 4)
    