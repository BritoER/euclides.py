#O Algoritmo de Euclides em teoria dos números é o sistema que demonstra que dados inteiros a e b, -sem perder generalidade-
# sendo a < b, então mdc(a,b) = mdc(a-bk, b), tal que k é inteiro positivo.
a,b = input().split()
a = int(a)
b = int(b)
#Perceba que esta é a definição de módulo. Estamos olhando (b) módulo (a).
#Usaremos a função para poder repetir o comando enquanto for necessário.
def algt(a,b):
    while a!=b and a!=1 and b!=1:
        if b>a:
            b = b - a
        elif b<a:
            a = a - b
        print(a,b)

algt(a,b)