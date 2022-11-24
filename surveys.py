class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions


satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

survey_ladies_survey = Survey(
    "Survey Ladies Survey",
    "Would you like to take a survey?",
    [
        Question("Do you eat beans?"),
        Question("Would you like to see a new movie starring George Wendt?"),
        Question("Do you eat beans with George Wendt?"),
        Question("Would you like to see George Wendt eating beans in a movie?"),
        Question("Do you eat beans at George Wendt movies?"),
        Question("Would you like to see George Wendt in a bean-eating movie?"),
        Question("How many beans do you eat in a George Wendt bean-eating movie?",
                 ["none", "0-10", "10-20", "20-30", "30-40", "over 40"]),
        Question("How many bean-eating movies have you seen with George Wendt?",
                 ["0", "1", "more than 1"])
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
    "beans": survey_ladies_survey
}