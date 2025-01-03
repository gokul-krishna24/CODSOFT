import java.util.Scanner;
import java.util.Random;

public class NumberGuessingGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Welcome to the Ultimate Number Guessing Game!");
        System.out.println("Guess the number and test your luck and intuition!");
        System.out.println("---------------------------------------------------");

        boolean keepPlaying = true;
        int totalScore = 0;
        int totalRounds = 0;

        while (keepPlaying) {
            totalRounds++;
            int secretNumber = random.nextInt(100) + 1; // Random number between 1 and 100
            int attempts = 5;
            boolean roundWon = false;

            System.out.println("\n Round " + totalRounds + " Begins!");
            System.out.println("I have picked a secret number between 1 and 100.");
            System.out.println("You have " + attempts + " attempts to guess it.");

            while (attempts > 0) {
                System.out.print("\nEnter your guess: ");
                int guess = scanner.nextInt();
                attempts--;

                if (guess == secretNumber) {
                    System.out.println(" Awesome! You've guessed the correct number!");
                    int roundScore = attempts * 20 + 50; // Score based on attempts left
                    System.out.println("You earned " + roundScore + " points this round.");
                    totalScore += roundScore;
                    roundWon = true;
                    break;
                } else if (guess < secretNumber) {
                    System.out.println(" Too low! Try again.");
                } else {
                    System.out.println(" Too high! Try again.");
                }

                if (attempts > 0) {
                    System.out.println(" Remaining attempts: " + attempts);
                } else {
                    System.out.println(" You're out of attempts. The number was: " + secretNumber);
                }
            }

            if (!roundWon) {
                System.out.println("Don't worry, better luck next time! ");
            }

            System.out.print("\nDo you want to play another round? (yes/no): ");
            String response = scanner.next().toLowerCase();
            keepPlaying = response.equals("yes");

            if (!keepPlaying) {
                System.out.println("\n Final Results ");
                System.out.println("Rounds Played: " + totalRounds);
                System.out.println("Total Score: " + totalScore);
                System.out.println("Thanks for playing! See you next time! ");
            }
        }
        scanner.close();
    }
}
