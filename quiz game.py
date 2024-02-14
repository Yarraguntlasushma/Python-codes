from random import shuffle

QUESTIONS = {
    "What is the output of '2 + 2 * 3' in Python?": [
        "8", "10", "6", "12"
    ],
    "Which data structure in Python is mutable?": [
        "List", "Tuple", "String", "Set"
    ],
    "What is the result of the expression 'True and False' in Python?": [
        "False", "True", "None", "Error"
    ]
}

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, alternatives):
        correct_answer = alternatives[0]
        shuffled_alternatives = alternatives.copy()
        shuffle(shuffled_alternatives)

        print(question)
        for label, alternative in enumerate(shuffled_alternatives):
            print(f"  {label}) {alternative}")

        answer_label = int(input("Your answer (enter the number): "))
        answer = shuffled_alternatives[answer_label] if 0 <= answer_label < len(shuffled_alternatives) else None

        if answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer!r}.\n")

    def run_quiz(self):
        for question, alternatives in self.questions.items():
            self.ask_question(question, alternatives)
        print(f"Quiz completed! Your final score is {self.score}/{len(self.questions)}.")

# Example usage:
quiz_instance = Quiz(QUESTIONS)
quiz_instance.run_quiz()
