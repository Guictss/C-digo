#guisarabi@gmail.com

#Entrada
def count_inversions(arr):
    inversoes = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversoes += 1
    return inversoes

#Processamento
while True:
    entrada = input().split()
    N = int(entrada[0])
    if N == 0:
        break

    P = list(map(int, entrada[1:]))

    num_inversions = count_inversions(P)

#Saída
    print('Marcelo' if num_inversions % 2 == 0 else 'Carlos')