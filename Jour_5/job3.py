def longueur(chaine):
    if chaine == "":
        return 0
    else:
        return 1 + longueur(chaine[1:])

def main():
    chaine = input("Entrez une chaine de caractère : ")
    print("La longueur de la chaine est", longueur(chaine))

if __name__ == "__main__":
    main()