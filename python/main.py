from python.domaine.Hero import Hero
from python.domaine.Villain import Villain

if __name__ == "__main__":
    # Vous permet de tester votre implémentation

    batman = Hero("Batman", -20, 40)
    joker = Villain("Joker", 50)

    print("Doit indiquer 0: " + str(batman.getPower()))
    print("Doit indiquer 40: " + str(batman.getPopularity()))
    print("Doit indiquer \"Super hero: Batman\": " + str(batman))
    print("Ne doit rien indiquer: ")
    batman.invoke()

    print()
    print("Doit indiquer 50: " + str(joker.getPower()))
    print("Doit indiquer \"Super villain: Joker\": " + str(joker))
    print("Doit indiquer \"Joker invoqué\": ")
    joker.invoke()

    print()
    batman = Hero("Batman", 40, 50)
    print("Doit indiquer 40: " + str(batman.getPower()))
    print("Doit indiquer 50: " + str(batman.getPopularity()))
    print("Doit indiquer \"Batman invoqué\": ")
    batman.invoke()

    print()

    print("Doit indiquer \"Batman défi Joker\": ")
    batman.challenge(joker)
    print("Doit indiquer \"Joker défi Batman\": ")
    joker.challenge([batman])
    print("Doit indiquer \"Joker défi Batman, WonderWoman\": ")
    wonderWoman = Hero("WonderWoman", 70, 70)
    joker.challenge([batman, wonderWoman])
