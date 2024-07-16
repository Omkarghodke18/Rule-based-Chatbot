def basic_chatbot():
    
    print("ChatBot: Hi! I'm a chatbot. Ask me anything. (Type 'bye' to exit)")

    print("ChatBot: **I have something to tell you, If you are connected with real estate market YOU SHOULD VISIT JLL** ")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("ChatBot: Goodbye! Have a great day.")
            break

        elif 'hello' in user_input:
            print("ChatBot: Hi there! How can I help you?")

        elif 'how are you' in user_input:
            print("ChatBot: I'm doing well, thank you!")

        elif 'your name' in user_input:
            print("ChatBot: I'm a chatbot. You can call me ChatBot.")

        elif 'i am jll intern' in user_input:
            print("ChatBot: Nice to meet you !")

        elif 'i need internship' in user_input:
            print("ChatBot: JLL Aurangabad will be best for you ")

        elif 'I am cs student which domain should i choose for internship' in user_input:
            print("ChatBot: As a Computer Science student you can choose any domain, But it depends on you.")

        elif 'decrease brightness of device' in user_input:
            print("ChatBot: For that press FN + F2 keys")

        elif 'Todays good thought ' in user_input:
            print("ChatBot: Consistent learners never fears to take challenges !")
    
        elif 'tell me about yourself' in user_input:
            print("ChatBot: I am chatBot , Onkar devloped me so he might be my boss hahaha")

        else:
            print("ChatBot: Sorry!,I'm not sure how to respond to that or it may be beyond my present abilities. Ask me something else.")

if __name__ == "__main__":
    basic_chatbot()
