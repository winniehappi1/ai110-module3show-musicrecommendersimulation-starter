# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
**VibeMatch 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 



This recommender suggests songs based on a user’s preferred genre, mood, and energy level. It assumes that users have clear preferences and that songs with similar features will match their taste. This system is designed for classroom exploration, not for real-world users.


---

## 3. How the Model Works  

Explain your scoring approach in simple language.  


The model looks at features of each song such as genre, mood, energy, and acousticness. It also uses the user’s preferences, including favorite genre, favorite mood, target energy, and whether they like acoustic music.

Each song is given a score. The system adds points if the genre matches and if the mood matches. It also gives points based on how close the song’s energy is to the user’s target. Finally, it adjusts the score depending on whether the user prefers acoustic songs.

After scoring all songs, the system sorts them from highest to lowest score and returns the top recommendations.


---

## 4. Data  

Describe the dataset the model uses.  

The dataset contains a small catalog of songs with features like genre, mood, energy, tempo, valence, danceability, and acousticness. There are around 15–20 songs in total.

The dataset includes a mix of genres such as pop, rock, lofi, and others, along with different moods like happy, chill, and intense. However, some genres and moods are underrepresented.

No major data was added or removed, but the dataset is limited and does not represent all types of musical taste.

---

## 5. Strengths  

Where does your system seem to work well  

The system works well for users with clear and simple preferences. For example, it gives good results for users who want chill lofi music or high-energy pop songs.

It correctly matches songs based on genre and mood, and the energy similarity helps refine the recommendations. In many cases, the results felt accurate and matched expected music styles.


---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 


One limitation of this system is that it over-prioritizes genre. Since genre gives more points than other features, songs from the favorite genre often appear at the top even if they do not match mood or energy well.

Another issue is that energy similarity has a strong influence on the results. Songs with energy close to the user’s target are ranked higher, which can reduce variety and make recommendations too similar.

The system also struggles with users who have conflicting preferences. For example, if a user wants a “chill” mood but high energy, the system does not handle this well and may give confusing results.

In addition, the dataset is very small, which limits diversity. Some genres or moods only have one or two songs, so the recommendations can feel repetitive.

Finally, the acoustic preference can indirectly bias the system toward certain types of music, such as chill or relaxed songs, instead of giving a balanced mix.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 


I tested my recommender system using several different user profiles, including "High-Energy Pop," "Chill Lofi," "Deep Rock," and a "Confusing User" with mixed preferences.

For each profile, I looked at whether the recommended songs matched the user’s genre, mood, and energy preferences. In general, the system behaved as expected. For example, the "Chill Lofi" profile mostly returned calm, low-energy songs, while the "Deep Rock" profile returned intense, high-energy songs.

One surprising result was that some songs appeared in multiple profiles. For example, "Gym Hero" showed up even when it did not fully match the genre or mood. This happens because the system gives strong weight to energy similarity, so songs with similar energy levels can rank high even if other features do not match.

I also noticed that the "Confusing User" profile produced results mostly based on energy, ignoring mood differences. This showed that the system struggles when user preferences conflict.

Overall, the system works well for clear and simple preferences, but it becomes less accurate when preferences are mixed or when different features compete with each other.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

PIn the future, I would improve the model by adding more features such as lyrics or artist similarity. I would also improve the scoring system to better balance genre, mood, and energy.

Another improvement would be increasing the dataset size to provide more variety. Finally, I would add a way to diversify recommendations so users do not always see very similar songs.
 

---

## 9. Personal Reflection  

A few sentences about your experience.  

During this project, I learned how recommender systems turn simple data into meaningful suggestions. I was surprised that even a basic scoring system could produce results that feel realistic.

Using AI tools helped me write code faster and understand the structure of the system, but I still had to check the logic and fix errors myself.

This project showed me that even simple algorithms can feel powerful, but they also have clear limitations. It changed how I think about music apps like Spotify, and how they might be using similar ideas at a larger scale. 
