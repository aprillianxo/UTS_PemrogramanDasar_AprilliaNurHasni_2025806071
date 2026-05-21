import json
import os
from colorama import Fore

FILE_NAME = "scores.json"

def load_scores():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_score(name, score):
    scores = load_scores()

    scores.append({
        "name": name,
        "score": score
    })

    with open(FILE_NAME, "w") as file:
        json.dump(scores, file, indent=4)

def show_top_scores():
    scores = load_scores()

    sorted_scores = sorted(
        scores,
        key=lambda x: x["score"],
        reverse=True
    )

    print(Fore.CYAN + "\n=== TOP 5 SCORE ===")

    for i, player in enumerate(sorted_scores[:5], start=1):
        print(
            Fore.GREEN +
            f"{i}. {player['name']} - {player['score']} pts"
        )