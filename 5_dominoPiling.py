input = input()
lista = input.split(' ')
m = int(lista[0])
n = int(lista[1])
if (1<=m<=n<=16):
    print((m*n)//2)
else:
    exit()