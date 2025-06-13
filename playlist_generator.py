# Mood-Based Playlist Generator by Talar Jaya 🎵
# This program suggests songs based on your mood!

# Step 1: Create a dictionary of moods and songs
mood_songs = {
    "happy": " priya_mithunam",
    "sad": "padi_padi_lache",
    "energetic": "don't stop",
    "calm": "Clair de Lune by Claude Debussy",
    "angry": "Break Stuff by Limp Bizkit"
}
# Step 2: Welcome the user and show available moods
print("🎵 Welcome to the Mood-Based Playlist Generator! 🎵")
print("I’ll suggest a song based on your mood.")
print("Available moods:", ", ".join(mood_songs.keys()))

# Step 3: Loop to let the user keep trying different moods
while True:
    # Ask for the user's mood
    mood = input("\nWhat’s your mood today? (or type 'exit' to quit): ").lower()

    # Check if the user wants to exit
    if mood == "exit":
        print("Thanks for using the Playlist Generator! Bye! 👋")
        break

    # Step 4: Suggest a song based on the mood
    if mood in mood_songs:
        song = mood_songs[mood]
        print(f"Since you’re feeling {mood}, I suggest: {song} 🎶")
    else:
        print("Sorry, I don’t have a song for that mood. Try one of these:", ", ".join(mood_songs.keys()))