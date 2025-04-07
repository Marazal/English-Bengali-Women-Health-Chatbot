import openai
import os

# Setting up OpenAI API key 
openai.api_key = os.getenv("sk-")
client = openai.OpenAI()

def women_health_chatbot():
    print("Welcome to your personal Women's Health Assistant.")
    print("Please choose your preferred language / আপনার পছন্দের ভাষা নির্বাচন করুন:")
    print("1. English\n2. বাংলা (Bengali)")

    lang_choice = input("Enter 1 or 2: ")

    if lang_choice == '1':
        lang = "English"
        system_message = (
            "You are a compassionate AI assistant specialized in women's health. "
            "Provide helpful, accurate, and supportive information in English. "
            "Keep your tone professional yet warm. Do not give definitive diagnoses but offer guidance and suggest seeing a doctor when necessary."
        )
    elif lang_choice == '2':
        lang = "Bengali"
        system_message = (
            "তুমি একজন সহানুভূতিশীল AI সহকারী, যার বিশেষত্ব নারীদের স্বাস্থ্য। "
            "বাংলা ভাষায় সহায়ক, নির্ভুল ও আন্তরিক তথ্য দাও। "
            "চূড়ান্ত রোগ নির্ণয় দিও না, বরং পরামর্শ দাও এবং প্রয়োজনে ডাক্তারের সঙ্গে দেখা করার পরামর্শ দাও।"
        )
    else:
        print("Invalid choice. Defaulting to English.")
        lang = "English"
        system_message = (
            "You are a compassionate AI assistant specialized in women's health. "
            "Provide helpful, accurate, and supportive information in English. "
            "Keep your tone professional yet warm. Do not give definitive diagnoses but offer guidance and suggest seeing a doctor when necessary."
        )

    print(f"\n🤖 Starting chat in {lang}...")
    print("Type 'quit' to exit.\n")

    conversation_history = [
        {"role": "system", "content": system_message}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            goodbye = "বিদায়! সুস্থ থাকুন 💖" if lang == "Bengali" else "Take care! Wishing you good health 💖"
            print("Bot:", goodbye)
            break

        conversation_history.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation_history,
                temperature=0.7,
                max_tokens=500
            )

            bot_reply = response.choices[0].message.content.strip()
            print("Bot:", bot_reply)

            conversation_history.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            print("Bot: Sorry, I ran into an issue. Please try again later.")
            print("Error:", e)

# Running the chatbot
if __name__ == "__main__":
    women_health_chatbot()
