size = int(input("Taille de votre sapin: "))

for i in range(0, size):
    print(' ' * (size - i) + '^' * (1 + 2*i))
