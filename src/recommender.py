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
    
user_profile = UserProfile(
    favorite_genre="lofi",
    favorite_mood="chill",
    target_energy=0.4,
    likes_acoustic=True
    )

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        scored_songs = []

        for song in self.songs:
            score = 0.0

            if song.genre == user.favorite_genre:
                score += 2.0

            if song.mood == user.favorite_mood:
                score += 1.0

            score += 1 - abs(song.energy - user.target_energy)

            if user.likes_acoustic:
                score += song.acousticness
            else:
                score += 1 - song.acousticness

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda x: x[1], reverse=True)

        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    songs = []

    print(f"Loading songs from {csv_path}...")

    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate score and reasons for a single song."""
    score = 0.0
    reasons = []

    # Genre match
    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match
    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy similarity
    energy_score = 1 - abs(song["energy"] - user_prefs["energy"])
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs and return top K recommendations."""    
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)

        scored_songs.append((song, score, explanation))

    # Sort highest score first
    scored_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)

    return scored_songs[:k]