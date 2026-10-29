
def display_question(question_data, question_number, total_questions):
    """Display a question and its options."""
    print(f"\nQuestion {question_number} of {total_questions}")
    print(question_data["question"])

    for option, text in question_data["options"].items():
        print(f"{option}. {text}")


def validate_answer(answer, options):
    """Check whether the answer is a valid option."""
    answer = answer.strip().upper()
    return answer in options


def check_answer(answer, correct_answer):
    """Check whether the answer is correct."""
    return answer.strip().upper() == correct_answer.upper()


def update_score(score, is_correct):
    """Update the score based on the answer."""
    if is_correct:
        score += 1

    return score


def get_result_category(percentage):
    """Return a category based on the final percentage."""
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Very Good"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 50:
        return "Pass"
    else:
        return "Needs Improvement"


def display_final_results(score, total_questions):
    """Display the final score and performance."""
    incorrect = total_questions - score

    if total_questions == 0:
        percentage = 0
    else:
        percentage = (score / total_questions) * 100

    category = get_result_category(percentage)

    print("\n" + "=" * 40)
    print("             QUIZ RESULTS")
    print("=" * 40)
    print(f"Total questions: {total_questions}")
    print(f"Correct answers: {score}")
    print(f"Incorrect answers: {incorrect}")
    print(f"Final score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Result category: {category}")
    print("=" * 40)


def get_questions():
    """Return the quiz questions."""
    questions = [
        {
            "question": "Which language is commonly used for web page structure?",
            "options": {
                "A": "Python",
                "B": "HTML",
                "C": "SQL",
                "D": "C++"
            },
            "correct_answer": "B"
        },
        {
            "question": "Which Python keyword defines a function?",
            "options": {
                "A": "function",
                "B": "define",
                "C": "def",
                "D": "fun"
            },
            "correct_answer": "C"
        },
        {
            "question": "Which data structure stores key-value pairs in Python?",
            "options": {
                "A": "List",
                "B": "Tuple",
                "C": "String",
                "D": "Dictionary"
            },
            "correct_answer": "D"
        },
        {
            "question": "What does len() return?",
            "options": {
                "A": "The length of an object",
                "B": "The largest number",
                "C": "The data type",
                "D": "The sum of numbers"
            },
            "correct_answer": "A"
        },
        {
            "question": "Which operator checks equality in Python?",
            "options": {
                "A": "=",
                "B": "==",
                "C": "!=",
                "D": ">="
            },
            "correct_answer": "B"
        },
        {
            "question": "Which loop is useful for iterating over a list?",
            "options": {
                "A": "repeat",
                "B": "loop",
                "C": "for",
                "D": "iterate"
            },
            "correct_answer": "C"
        }
    ]

    return questions


def play_quiz():
    """Run one complete quiz."""
    questions = get_questions()
    score = 0
    total_questions = len(questions)

    print("\nWELCOME TO THE PYTHON QUIZ!")
    print("-" * 40)

    for index, question_data in enumerate(questions, start=1):
        display_question(question_data, index, total_questions)

        while True:
            answer = input("Your answer (A, B, C, or D): ")

            if validate_answer(answer, question_data["options"]):
                break

            print("Invalid option. Please enter A, B, C, or D.")

        if check_answer(answer, question_data["correct_answer"]):
            print("Correct!")
            score = update_score(score, True)
        else:
            print(
                "Incorrect! The correct answer is",
                question_data["correct_answer"]
            )
            score = update_score(score, False)

    display_final_results(score, total_questions)


def main():
    """Allow the user to play the quiz multiple times."""
    while True:
        play_quiz()

        while True:
            play_again = input(
                "\nWould you like to play again? (yes/no): "
            ).strip().lower()

            if play_again in ("yes", "y", "no", "n"):
                break

            print("Please enter yes or no.")

        if play_again in ("no", "n"):
            print("Thank you for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
