import java.util.Scanner;
import java.util.concurrent.atomic.AtomicBoolean;

class Question {
    String questionText;
    String[] options;
    int correctOption;

    public Question(String questionText, String[] options, int correctOption) {
        this.questionText = questionText;
        this.options = options;
        this.correctOption = correctOption;
    }

    public boolean isCorrect(int selectedOption) {
        return selectedOption == correctOption;
    }
}

public class QuizApplication {
    private static final int TIME_LIMIT = 10;
    private Question[] questions;
    private int score;
    private String[] resultSummary;

    public QuizApplication() {
        questions = new Question[]{
                new Question("What is the capital of France?", new String[]{"1. Berlin", "2. Madrid", "3. Paris", "4. Rome"}, 3),
                new Question("Who developed Java?", new String[]{"1. James Gosling", "2. Dennis Ritchie", "3. Bjarne Stroustrup", "4. Guido van Rossum"}, 1),
                new Question("What is 5 + 3?", new String[]{"1. 6", "2. 7", "3. 8", "4. 9"}, 3),
                new Question("Which is the largest planet?", new String[]{"1. Earth", "2. Jupiter", "3. Saturn", "4. Venus"}, 2),
                new Question("What is the boiling point of water?", new String[]{"1. 50°C", "2. 75°C", "3. 90°C", "4. 100°C"}, 4)
        };
        score = 0;
        resultSummary = new String[questions.length];
    }

    public void start() {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < questions.length; i++) {
            System.out.println("\nQuestion " + (i + 1) + ": " + questions[i].questionText);
            for (String option : questions[i].options) {
                System.out.println(option);
            }
            System.out.println("You have " + TIME_LIMIT + " seconds to answer.");

            AtomicBoolean answered = new AtomicBoolean(false);
            int[] selectedOption = {-1};

            Thread inputThread = new Thread(() -> {
                if (scanner.hasNextInt()) {
                    selectedOption[0] = scanner.nextInt();
                    answered.set(true);
                }
            });

            inputThread.start();
            try {
                inputThread.join(TIME_LIMIT * 1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            if (!answered.get()) {
                System.out.println("Time's up! Moving to the next question.");
                resultSummary[i] = "Unanswered";
            } else if (questions[i].isCorrect(selectedOption[0])) {
                System.out.println("Correct!");
                score++;
                resultSummary[i] = "Correct";
            } else {
                System.out.println("Incorrect. The correct answer was: " + questions[i].correctOption);
                resultSummary[i] = "Incorrect";
            }
        }

        displayResults();
        scanner.close();
    }

    private void displayResults() {
        System.out.println("\nQuiz Over!");
        System.out.println("Your Score: " + score + "/" + questions.length);
        System.out.println("Summary:");
        for (int i = 0; i < resultSummary.length; i++) {
            System.out.println("Question " + (i + 1) + ": " + resultSummary[i]);
        }
    }

    public static void main(String[] args) {
        QuizApplication quizApp = new QuizApplication();
        quizApp.start();
    }
}
