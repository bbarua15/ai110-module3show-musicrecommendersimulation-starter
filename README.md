# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

My song recommender looks at each song's genre, mood, energy, tempo, valence, danceability, and acousticness, and compares those to what the user says they like — their favorite genre, favorite mood, a target energy level, and whether they enjoy acoustic songs. To score a song, it gives the most points for a matching genre, a bit less for a matching mood, and for energy it rewards songs that are close to the user's target level rather than just favoring high or low energy, with a small bonus if the acoustic preference lines up too. Once every song in the catalog has a score, the system sorts them from highest to lowest and hands back the top few as the final recommendations, along with a short reason for each pick.

I finalized the exact math the recommender uses to score songs — genre match is worth 2 points, mood match is worth 1 point, energy gets up to 1 point based on how close it is to what the listener wants (not just high or low), and matching the acoustic preference adds a small half-point bonus, for a max possible score of 4.5. I also added a note admitting the system will probably lean too hard on genre — it might rank a just-okay genre match above a song that's actually a much better mood and energy fit, and it'll naturally recommend more of whatever genres and moods are most common in the small starter catalog, giving less variety to listeners with different taste.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

```
Loaded songs: 18

==================================================
TOP RECOMMENDATIONS
==================================================

1. Sunrise City — Neon Echo
   Score: 3.98
   Why:
     - genre matches (pop): +2.0
     - mood matches (happy): +1.0
     - energy closeness: +0.98

2. Gym Hero — Max Pulse
   Score: 2.87
   Why:
     - genre matches (pop): +2.0
     - energy closeness: +0.87

3. Rooftop Lights — Indigo Parade
   Score: 1.96
   Why:
     - mood matches (happy): +1.0
     - energy closeness: +0.96

4. Night Drive Loop — Neon Echo
   Score: 0.95
   Why:
     - energy closeness: +0.95

5. Storm Runner — Voltline
   Score: 0.89
   Why:
     - energy closeness: +0.89

==================================================

```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



