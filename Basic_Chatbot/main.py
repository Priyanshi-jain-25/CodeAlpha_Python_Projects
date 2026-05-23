from datetime import datetime
def show_greeting():
    current_hour=datetime.now().hour
    if current_hour <12:
        print("Bot:Good Morning!")
    elif current_hour<18:
        print("Bot:Good Afternoon!")
    else:
        print("Bot:Good Evening!")

def chatbot_response(user_input):
    if user_input=="hello":
        return"Hello! Nice to meet you."
    
    elif user_input=="how are you":
        return"I am good.Thank you!"
    
    elif user_input=="your name":
        return " I am Python Chatbot"
    
    elif user_input=="time":
        current_time= datetime.now().strftime("%H:%M:%S")
        return f"Current Time is {current_time}"
    
    elif user_input=="date":
        current_date=datetime.now().strftime("%d-%m-%Y")
        return f"Today Date is {current_date}"
    
    elif user_input == "good morning":
        return "Good Morning! Have a wonderful day ahead."
    
    elif user_input == "good night":
        return "Good Night! Sweet dreams and take care."
    
    elif user_input=="jai jinendra":
        return"Jai Jinendra! Whishing you peace and happiness"
    
    elif user_input == "namaste":
        return "Namaste! Hope you are having a great day."

    elif user_input == "motivate me":
        return "Success comes from consistency and hard work. Keep learning!"

    elif user_input == "study tip":
        return "Focus on one concept at a time and practice daily."

    elif user_input == "quote":
        return "Believe in yourself and keep moving forward."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "help":
        return "You can ask me about time, date, greetings, motivate me, or study tips."

    elif user_input == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."


# Main program
print("===SMART PYTHON CHATBOT===")

show_greeting()

print("\nCommands: hello, time, date, good morning, good night, jai jinendra, namaste, motivate me, study tip, quote, thank you, help, bye")

print("\nType 'bye' to exit.")

# Main chatbot 
while True:

    user_message = input("\nYou: ").lower()
    response = chatbot_response(user_message)
    print("Bot:", response)

    if user_message == "bye":
        break