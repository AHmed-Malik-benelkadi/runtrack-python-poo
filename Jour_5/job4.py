# Écrire une fonction récursive permettant de retourner le plus grand chiffre d’une liste.

def max_liste(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return max(liste[0], max_liste(liste[1:]))

def main():
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(max_liste(liste))

if __name__ == "__main__":
    main()