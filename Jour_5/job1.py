def factorielle(n):
    # doit etre positive

    if n < 0:
        return "Erreur le nombre doit etre positif"
    elif n == 0:
        return 1
    else:
        return n * factorielle(n-1)

def main():
    nombre = int(input("Entrez un nombre : "))
    print("La factorielle de", nombre, "est", factorielle(nombre))

if __name__ == "__main__":
    main()



