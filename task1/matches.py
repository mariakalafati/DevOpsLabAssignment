from flask import Flask, render_template
import json
import random

app = Flask(__name__)

@app.route('/')
def show_all_matches(): 
    return render_template('homescreen.html', matches=matches)

@app.route('/match/<int:match_id>')
def show_match(match_id):
    match = matches[match_id]
    return render_template('match.html', match=match)

def create_matches(num_matches):
    matches = []
    with open('data.json', 'r') as f:
        data = json.load(f)
    for i in range(num_matches):
        id1 = random.randint(0, len(data["teams"]) - 1)
        id2 = random.randint(0, len(data["teams"]) - 1)
        while id1 == id2:
            id2 = random.randint(0, len(data["teams"]) - 1)
        team1 = data["teams"][id1]
        team2 = data["teams"][id2]
        score1 = random.randint(0, 5)
        score2 = random.randint(0, 5)
        scorers1 = random.choices(population=team1["players"], k=score1)
        scorers2 = random.choices(population=team2["players"], k=score2)
        minutes1 = random.sample(range(1, 94), score1)
        minutes2 = random.sample(range(1, 94), score2)
        minutes1.sort()
        minutes2.sort()
        match = {
            "match_id": i,
            "team1": team1["name"],
            "team2": team2["name"],
            "score": f"{score1}-{score2}",
            "scorers1": [(scorers1[j], minutes1[j]) for j in range(score1)],
            "scorers2": [(scorers2[j], minutes2[j]) for j in range(score2)],
        }
        matches.append(match)
    return matches

if __name__ == '__main__':
    global matches
    matches = create_matches(num_matches=10)
    app.run(debug=True)
