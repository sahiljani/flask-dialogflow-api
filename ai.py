import random
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def generate_workout_plan(days, exercise_types):
    workout_plan = {}
    for day in days:
        workout_plan[day] = random.sample(exercise_types, k=random.randint(1, len(exercise_types)))
    return workout_plan

def main():
    default_days = ["Monday", "Wednesday", "Friday"]
    default_exercise_types = ["push-ups", "pull-ups", "squats", "lunges", "deadlifts", "planks", "burpees", "sit-ups"]

    print("Welcome to the Workout Plan Generator!")
    print("Default workout days are:", default_days)
    print("Default exercise types are:", default_exercise_types)
    print("Do you want to customize? (yes/no):")
    customize = input().lower()

    if customize == "yes":
        print("Choose the days you want to workout separated by commas (e.g., Monday,Wednesday,Friday):")
        selected_days = input().split(",")
        print("Choose the types of exercises you want to include separated by commas (e.g., push-ups,pull-ups,squats):")
        selected_exercises = input().split(",")
    else:
        selected_days = default_days
        selected_exercises = default_exercise_types

    # Generating synonyms for selected exercises
    synonyms_exercises = []
    for exercise in selected_exercises:
        synonyms_exercises.extend(get_synonyms(exercise))

    # Remove duplicates
    synonyms_exercises = list(set(synonyms_exercises))

    # Generating workout plan
    workout_plan = generate_workout_plan(selected_days, synonyms_exercises)

    # Printing workout plan
    print("\nYour Workout Plan:")
    for day, exercises in workout_plan.items():
        print(day + ": " + ", ".join(exercises))

if __name__ == "__main__":
    main()
