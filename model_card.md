# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

'''
Model name: **VibeMatch**
Loaded songs: 18

==================================================
PROFILE: Conflicting Mood/Energy  {'genre': 'rock', 'mood': 'sad', 'energy': 0.9}
==================================================

1. Storm Runner — Voltline
   Score: 2.99
   Why:
     - genre matches (rock): +2.0
     - energy closeness: +0.99

2. Gym Hero — Max Pulse
   Score: 0.97
   Why:
     - energy closeness: +0.97

3. Neon Pulse Overdrive — Kilowatt
   Score: 0.95
   Why:
     - energy closeness: +0.95

4. Iron Fury — Deadbolt
   Score: 0.93
   Why:
     - energy closeness: +0.93

5. Sunrise City — Neon Echo
   Score: 0.92
   Why:
     - energy closeness: +0.92

==================================================

==================================================
PROFILE: Nonexistent Genre  {'genre': 'polka', 'mood': 'happy', 'energy': 0.5}
==================================================

1. Rooftop Lights — Indigo Parade
   Score: 1.74
   Why:
     - mood matches (happy): +1.0
     - energy closeness: +0.74

2. Sunrise City — Neon Echo
   Score: 1.68
   Why:
     - mood matches (happy): +1.0
     - energy closeness: +0.68

3. Velvet Hours — Simone Wray
   Score: 1.00
   Why:
     - energy closeness: +1.00

4. Dust and Diesel — Cole Harlan
   Score: 0.98
   Why:
     - energy closeness: +0.98

5. Broken Streetlights — Silver Fox
   Score: 0.95
   Why:
     - energy closeness: +0.95

==================================================

==================================================
PROFILE: Extreme Energy Out of Range  {'genre': 'pop', 'mood': 'happy', 'energy': 1.5}
==================================================

1. Sunrise City — Neon Echo
   Score: 3.32
   Why:
     - genre matches (pop): +2.0
     - mood matches (happy): +1.0
     - energy closeness: +0.32

2. Gym Hero — Max Pulse
   Score: 2.43
   Why:
     - genre matches (pop): +2.0
     - energy closeness: +0.43

3. Rooftop Lights — Indigo Parade
   Score: 1.26
   Why:
     - mood matches (happy): +1.0
     - energy closeness: +0.26

4. Iron Fury — Deadbolt
   Score: 0.47
   Why:
     - energy closeness: +0.47

5. Neon Pulse Overdrive — Kilowatt
   Score: 0.45
   Why:
     - energy closeness: +0.45

==================================================

==================================================
PROFILE: Negative Energy  {'genre': 'lofi', 'mood': 'chill', 'energy': -0.3}
==================================================

1. Library Rain — Paper Lanterns
   Score: 3.35
   Why:
     - genre matches (lofi): +2.0
     - mood matches (chill): +1.0
     - energy closeness: +0.35

2. Midnight Coding — LoRoom
   Score: 3.28
   Why:
     - genre matches (lofi): +2.0
     - mood matches (chill): +1.0
     - energy closeness: +0.28

3. Focus Flow — LoRoom
   Score: 2.30
   Why:
     - genre matches (lofi): +2.0
     - energy closeness: +0.30

4. Spacewalk Thoughts — Orbit Bloom
   Score: 1.42
   Why:
     - mood matches (chill): +1.0
     - energy closeness: +0.42

5. Cathedral Echoes — Aria Vane
   Score: 0.40
   Why:
     - energy closeness: +0.40

==================================================

==================================================
PROFILE: Empty Profile  {}
==================================================

1. Sunrise City — Neon Echo
   Score: 0.00
   Why:
     - no strong matches

2. Midnight Coding — LoRoom
   Score: 0.00
   Why:
     - no strong matches

3. Storm Runner — Voltline
   Score: 0.00
   Why:
     - no strong matches

4. Library Rain — Paper Lanterns
   Score: 0.00
   Why:
     - no strong matches

5. Gym Hero — Max Pulse
   Score: 0.00
   Why:
     - no strong matches

==================================================

==================================================
PROFILE: Typo'd Genre Casing  {'genre': 'Pop', 'mood': 'Happy', 'energy': 0.8}
==================================================

1. Sunrise City — Neon Echo
   Score: 0.98
   Why:
     - energy closeness: +0.98

2. Rooftop Lights — Indigo Parade
   Score: 0.96
   Why:
     - energy closeness: +0.96

3. Night Drive Loop — Neon Echo
   Score: 0.95
   Why:
     - energy closeness: +0.95

4. Storm Runner — Voltline
   Score: 0.89
   Why:
     - energy closeness: +0.89

5. Gym Hero — Max Pulse
   Score: 0.87
   Why:
     - energy closeness: +0.87

==================================================
'''

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

VibeMatch picks the top 5 songs for a user from a small catalog. It looks at what genre, mood, and energy the user says they like. It assumes the user knows their own taste and can describe it simply. This is a class project. It is not built for real users.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

VibeMatch checks each song's genre, mood, energy, and acousticness. It compares these to what the user wants. A genre match gives the most points. A mood match gives fewer points. Energy is scored by how close it is to the user's target, not just "high" or "low." Acousticness gives a small bonus if it matches. All the points add up to one score per song. Then the songs are sorted from highest score to lowest. None of this logic was in the starter code. I wrote all of it myself.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog started with 10 songs. I added 8 more songs, so now there are 18. The new songs cover genres the old ones didn't, like hip-hop, classical, metal, folk, R&B, country, EDM, and reggae. Even with the new songs, some genres only have 1 song. Lofi has 3. There are no lyrics in the data. There is no "sad" mood anywhere in the catalog, which caused problems during testing.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

VibeMatch works well when a user has one clear genre and mood, and that combo is well-covered by the catalog. For example, a "pop/happy/high-energy" user gets "Sunrise City" as the top pick, and that feels right. The energy scoring also works correctly — it always picks songs closer to the target energy over songs that are just high or low.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

Here's a 3-5 sentence version, grounded in your actual experiment results, ready to paste into `model_card.md`:

The genre match only works with exact spelling. "Pop" and "pop" are treated as different genres, so a simple typo breaks the whole genre match. "Indie pop" also never counts as a match for "pop," even though they're similar. I tested a "sad" mood request and got almost the same result as an "intense" mood request, because no song in the data is tagged "sad." I also tried an empty profile — one with no preferences at all. Every song scored 0, and the "top 5" was just the first 5 rows of the file, not a real ranking. When I changed the weights (less genre, more energy), a metal song jumped into the top 5 for a rock request, just because its energy number was close. None of these problems are fixed. They're just documented here.

During testing, I found that the exact-string genre match creates a real filter bubble: a user who prefers "pop" never gets a boost for "indie pop" songs, even though a human listener would likely consider them closely related. This also showed up as a case-sensitivity bug — when I tested a profile with `genre: "Pop"` instead of `"pop"`, the system lost the entire +2.0 genre bonus and fell back to ranking songs by energy alone, even though "Sunrise City" was a genuinely strong pop/happy match. Separately, my weight-shift experiment (doubling energy's weight, halving genre's) pulled "Iron Fury," a metal/angry song, into the top 5 for a rock/sad profile purely because its energy number was close, despite sharing no genre or mood overlap at all — showing the system can be tuned into surfacing songs that match on only one dimension. Together, these reveal that the scoring logic has no fuzzy matching and no way to weigh "how many dimensions matched" against "how strongly," so a single typo or a single weight change can swap a well-rounded recommendation for a much weaker one.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested three normal profiles (High-Energy Pop, Chill Lofi, Deep Intense Rock) plus six edge cases designed to try to break the system, then compared them in pairs to check whether the differences in output actually made sense. Profiles that differed in genre or energy correctly produced very different top songs, which is valid. But a few comparisons exposed real bugs: a profile asking for "sad" mood got almost the same result as one asking for "intense" mood, because no song in the catalog is tagged "sad" at all, and a profile typed as "Pop" instead of "pop" lost its entire genre match and scored far lower than it should have for the same actual request. An empty profile was the starkest case — every song tied at a score of 0, so the "top 5" was just meaningless CSV row order rather than a real recommendation.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I'd want to fix the genre matching so it's not case-sensitive, and so close genres like "pop" and "indie pop" count as a partial match. I'd also want the system to say "not enough info" instead of faking a ranking when the profile is empty. Adding more songs per genre would help too, so smaller genres aren't stuck with just 1-2 options. If I had more time, I'd add a way to check if mood and energy make sense together, so contradictory requests get flagged instead of silently answered.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this taught me that a recommender isn't really "smart" — it's just doing math on the data you give it. Most of the weird results weren't really bugs in my code, they were gaps in the data or in how I compared things. What surprised me most was the empty profile problem. I expected it to either break or say something like "no preferences given," but instead it gave a totally fake, confident-looking answer. That made me think about how real apps like Spotify might do the same thing — showing you a list that looks personal, even when the system doesn't actually have a strong reason for picking it.
