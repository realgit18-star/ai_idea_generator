walker main {
    can start entry {
        print("🎯 Welcome to the AI Idea Generator!")
        idea_type = input("What type of idea do you want to generate? (e.g. app, music, business): ")
        num_ideas = int(input("How many ideas would you like? "))

        ideas = [
            f"{idea_type.capitalize()} idea #{i+1}: A creative {idea_type} concept using AI to make life easier."
            for i in range(num_ideas)
        ]

        print("\n✨ Generated Ideas ✨")
        for idea in ideas:
            print(idea)

        print("\nNext step: You can upgrade this generator using AI (LLM).")
    }

    can ai_upgrade entry {
        user_prompt = input("Describe what kind of ideas you want AI to generate: ")
        llm_result = llm.chat("gpt-4", f"Generate 5 creative {user_prompt} ideas with explanations.")
        print("\n🤖 AI Generated Ideas:\n", llm_result)
    }
}
