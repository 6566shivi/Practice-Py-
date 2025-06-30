def chatbot():
    print("🤖 Hello! I am PyBot. Type 'exit' to quit.")
    
    while True:
        user = input("You: ").lower()
        
        if "hello" in user or "hi" in user:
            print("PyBot: Hello there! 👋")
        elif "how are you" in user:
            print("PyBot: I'm just a bunch of code, but I'm doing great! 😊")
        elif "your name" in user:
            print("PyBot: I'm PyBot, your Python friend!")
        elif "bye" in user or "exit" in user:
            print("PyBot: Bye! Have a great day 🚀")
            break
        else:
            print("PyBot: Sorry, I don't understand that yet. 😅")

chatbot()
