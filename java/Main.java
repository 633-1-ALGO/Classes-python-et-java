import domaine.Hero;
import domaine.Villain;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

//        Vous permet de tester votre implémentation

        Hero batman = new Hero("Batman", -20, 40);
        Villain joker = new Villain("Joker", 50);

        System.out.println("Doit indiquer 0: " + batman.getPower());
        System.out.println("Doit indiquer 40: " + batman.getPopularity());
        System.out.println("Doit indiquer \"Super hero: Batman\": " + batman);
        System.out.println("Ne doit rien indiquer: ");
        batman.invoke();

        System.out.println("\n");
        System.out.println("Doit indiquer 50: " + joker.getPower());
        System.out.println("Doit indiquer \"Super villain: Joker\": " + joker);
        System.out.print("Doit indiquer \"Joker invoqué\": ");
        joker.invoke();

        System.out.println("\n");
        batman = new Hero("Batman", 40, 50);
        System.out.println("Doit indiquer 40: " + batman.getPower());
        System.out.println("Doit indiquer 50: " + batman.getPopularity());
        System.out.print("Doit indiquer \"Batman invoqué\": ");
        batman.invoke();

        System.out.println("\n");
        System.out.print("Doit indiquer \"Batman défi Joker\": ");
        batman.challenge(joker);
        System.out.print("Doit indiquer \"Joker défi Batman\": ");
        joker.challenge(Arrays.asList(batman));
        System.out.print("Doit indiquer \"Joker défi Batman, WonderWoman\": ");
        Hero wonderWoman = new Hero("WonderWoman", 70, 70);
        joker.challenge(Arrays.asList(batman, wonderWoman));

    }
}
