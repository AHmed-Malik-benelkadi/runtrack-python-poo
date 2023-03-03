"""Écrire une fonction récursive qui calcule le n-ième nombre de la suite de Fibonacci.
La suite de Fibonacci est une suite de nombres où chaque nombre est la somme des
deux nombres précédents. Elle commence par 0 et 1, et les premiers termes sont donc :
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc."""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def main():
    n = int(input("Entrez un nombre : "))
    print(fibonacci(n))
if __name__ == "__main__":
    main()
