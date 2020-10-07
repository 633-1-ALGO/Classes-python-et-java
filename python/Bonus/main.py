from python.Bonus.Number import Number

if __name__ == '__main__':
    nb1 = Number(10)
    nb2 = Number(20)

    print("Doit afficher 30: ")
    resultat = nb1 + nb2
    print(resultat)

    print("Doit afficher -10: ")
    resultat = nb1 - nb2
    print(resultat)

    print("Doit afficher 200: ")
    resultat = nb1 * nb2
    print(resultat)

    print("Doit afficher 0.5: ")
    resultat = nb1 / nb2
    print(resultat)
