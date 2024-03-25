from flask import Flask, jsonify, request
import random
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def get_student_number():
    return jsonify({"student_number": "200537749"})

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    query_result = req.get('queryResult')
    if query_result.get('action') == 'input.workout':
        # Default values for workout days and exercise types
        default_days = ["Monday", "Wednesday", "Friday"]
        default_exercise_types = ["push-ups", "pull-ups", "squats", "lunges", "deadlifts", "planks", "burpees", "sit-ups"]

        # Generating workout plan
        workout_plan = generate_workout_plan(default_days, default_exercise_types)

        # Formatting workout plan
        fulfillmentText = "Your Workout Plan:\n"
        for day, exercises in workout_plan.items():
            fulfillmentText += f"{day}: {', '.join(exercises)}\n"

    return {
            "fulfillmentText": fulfillmentText,
            "source": "webhookdata"
        }

if __name__ == '__main__':
    app.run(debug=True)
