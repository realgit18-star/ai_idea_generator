import random

def generate_ai_idea():
    categories = {
        "app": [
            "An AI fitness coach that adjusts your workout plan daily.",
            "A voice assistant that learns your emotions and mood.",
            "A study planner that generates personalized quizzes."
        ],
        "business": [
            "An AI tool that predicts small business trends.",
            "A chatbot for local restaurants that handles all orders.",
            "A marketing AI that writes ads based on local events."
        ],
        "music": [
            "AI that remixes your favorite songs based on your mood.",
            "A tool that writes original beats for rappers.",
            "AI that recommends chords and melodies for beginners."
        ]
    }

    print("🎯 Welcome to the AI Idea Generator!")
    idea_type = input("What type of idea do you want? (app, business, music): ").strip().lower()

    if idea_type not in categories:
        print("❌ Invalid type! Please choose from: app, business, music.")
        return

    num = int(input("How many ideas would you like? "))
    ideas = random.sample(categories[idea_type], min(num, len(categories[idea_type])))

    print("\n✨ Your AI-generated ideas:")
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea}")

if _name_ == "_main_":
    generate_ai_idea()
