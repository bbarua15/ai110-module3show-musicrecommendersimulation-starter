"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Prints ranked recommendations for a single user profile."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print("\n" + "=" * 50)
    print(f"PROFILE: {profile_name}  {user_prefs}")
    print("=" * 50)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} — {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Why:")
        for reason in explanation.split("; "):
            print(f"     - {reason}")

    print("\n" + "=" * 50)


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Three distinct stress-test profiles
    profiles = {
        "Conflicting Mood/Energy": {"genre": "rock", "mood": "sad", "energy": 0.9},
        "Nonexistent Genre": {"genre": "polka", "mood": "happy", "energy": 0.5},
        "Extreme Energy Out of Range": {"genre": "pop", "mood": "happy", "energy": 1.5},
        "Negative Energy": {"genre": "lofi", "mood": "chill", "energy": -0.3},
        "Empty Profile": {},
        "Typo'd Genre Casing": {"genre": "Pop", "mood": "Happy", "energy": 0.8},
    }

    for profile_name, user_prefs in profiles.items():
        print_recommendations(profile_name, user_prefs, songs, k=5)


if __name__ == "__main__":
    main()
