from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads songs.csv into a list of song dictionaries with numeric fields converted."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores one song against user preferences using the weighted genre/mood/energy/acoustic recipe."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs.get("genre"):
        score += 2.0
        reasons.append(f"genre matches ({song['genre']}): +2.0")

    if song["mood"] == user_prefs.get("mood"):
        score += 1.0
        reasons.append(f"mood matches ({song['mood']}): +1.0")

    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        energy_points = 1.0 - abs(song["energy"] - target_energy)
        score += energy_points
        reasons.append(f"energy closeness: +{energy_points:.2f}")

    likes_acoustic = user_prefs.get("likes_acoustic")
    if likes_acoustic is not None:
        song_is_acoustic = song["acousticness"] > 0.6
        if song_is_acoustic == likes_acoustic:
            score += 0.5
            reasons.append("acoustic preference matches: +0.5")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song against user preferences and returns the top k, sorted highest to lowest."""
    scored = [
        (song, score, "; ".join(reasons) if reasons else "no strong matches")
        for song, (score, reasons) in ((s, score_song(user_prefs, s)) for s in songs)
    ]
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
                                      # return the top results
