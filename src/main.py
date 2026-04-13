"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Multiple user profiles
    profiles = [
        {"name": "High-Energy Pop", "prefs": {"genre": "pop", "mood": "happy", "energy": 0.9}},
        {"name": "Chill Lofi", "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.3}},
        {"name": "Deep Rock", "prefs": {"genre": "rock", "mood": "intense", "energy": 0.9}},
        {"name": "Confusing User", "prefs": {"genre": "rock", "mood": "sad", "energy": 0.9}},
    ]

    # Loop through each profile
    for profile in profiles:
        print(f"\n=== 🎧 {profile['name']} ===\n")

        recommendations = recommend_songs(profile["prefs"], songs, k=5)

        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec

            print(f"{i}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Why: {explanation}")
            print()


if __name__ == "__main__":
    main()