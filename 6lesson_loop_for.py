'''for user in range(0, 3):
    name = input("Jak masz na imię?")
    print("Cześć", name, user)
for i in range(0, 5):
    print("krok: ", i)
for i in range(2, 5):
    print("krok: ", i)
print("#")
print("##")
print("###")
print("####")
print("#####")
for i in range(1, 6):
    print(i * "#")
names = ["Ania", "Kasia", "Jan", "Piotr", "Paweł"]
for i in range(0, 5):
    print("Cześć", names[i])
names = ["Ania", "Kasia", "Jan", "Piotr", "Paweł"]
for n in names:
    print("Cześć", n)
    
for i in "ala ma kota":
    print("krok: ", i)
#albo stworzyć pętle w pętli:

for i in range(0, 3):
    for j in range(1, 6):
        print(j * "#")
wynik=0
for i in range (1,11):
    wynik =wynik+i
    print (wynik)


for i in range (1,11):
    print (i**3)
    
a=input('wpisz jakie chcesz imiona rozdzielając je spacją \n')
b=a.split(' ')
for i in b:
    print ('cześć ',i)

a=int(input('wpisz liczbę \n'))
for i in range (0,a+1):
    if (i%3==0):
        if(i%4!=0):
            print('liczba ',i,' jest wielokrotnością 3')
        if(i%4==0):
            print('„hurra”, liczba ',i,' dzieli się zarówno przez 3 jak i 4')
    elif(i%4==0):
        print('liczba ',i,' jest wielokrotnością 4')
    else:
        print(i, '*')

a=int(input('wpisz liczbę \n'))
wynik=1
for i in range(0, a):
    wynik=wynik+1
    for j in range(1, wynik):
        print(j * "#")

#albo tak:
a=int(input('wpisz liczbę \n'))
for i in range(1, a+1):
    for j in range(1, i+1):
        print(j * "#")'''

print('-'*67)
print('''| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} |'''
          .format(' ',1,2,3,4,5,6,7,8,9,10,))
print('-'*67)
for i in range(1,11):
    print('''| {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} | {:3} |'''
          .format(i*1,i*1,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,))
print('-'*67)






