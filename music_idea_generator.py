import random

def generate_music_idea():
    ai_music_ideas = [
        "AI that composes background music based on your mood from webcam emotion detection.",
        "AI DJ that automatically mixes songs according to crowd energy.",
        "Neural network that generates melodies inspired by trending TikTok sounds.",
        "AI assistant that recommends chord progressions based on a singer's vocal range.",
        "AI app that creates personalized lullabies using your name and favorite sounds.",
        "AI tool that converts humming into full instrument tracks.",
        "AI that learns your playlist history and writes new songs in your favorite artist’s style.",
        "AI system that helps music producers generate drum patterns matching the lyrics’ mood.",
        "AI voice synthesizer that can sing any song in your voice tone.",
        "AI that recommends remix styles and BPMs for DJs automatically."
    ]

    print("🎧 Welcome to the AI Music Idea Generator!\n")
    num = int(input("How many ideas would you like? "))

    if num < 1:
        print("❌ Please enter a number greater than zero.")
        return

    ideas = random.sample(ai_music_ideas, min(num, len(ai_music_ideas)))

    print("\n✨ Your AI-powered music ideas ✨\n")
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea}")

if _name_ == "_main_":
    generate_music_idea()
