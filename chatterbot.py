from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer # type: ignore

bot_name = "College Buddy"

# Create a new chat bot named College Buddy
chatbot = ChatBot(bot_name)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

knowledge_base = {
    "what are the best colleges in pune?": [
        "COEP",
        "PICT",
        "VIT",
        "CUMMINS",
        "PCCOE",
        "DY Patil"
    ],
    "what are the best engineering branches?": [
        "Computer Engineering",
        "IT Engineering",
        "ENTC Engineering",
        "Civil Engineering"
    ],
    "What are the top branch cut-offs for coep?": [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT Engineering",
        "ENTC Engineering : 99.2 percentile"
    ],
    "What are the top branch cut-offs for pict?": [
        "Computer Engineering : 99.4 percentile",
        "IT Engineering : 97.1 percentile",
        "ENTC Engineering : 96.2 percentile"
    ],
    "What are the top branch cut-offs for vit?": [
        "Computer Engineering : 99.8 percentile",
        "IT Engineering : 97.1 percentile",
        "ENTC Engineering : 96.2 percentile"
    ],
    "What are the top branch cut-offs for cummins?": [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT Engineering",
        "ENTC Engineering : 96.2 percentile"
    ],
    "What are the top branch cut-offs for pccoe?": [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT Engineering",
        "ENTC Engineering : 92.2 percentile"
    ],
    "When do college admission start?": [
        "Admission generally start around August",
    ],
}

# Add the knowledge base to the chatbot
for key, values in knowledge_base.items():
    for value in values:
        chatbot.set_trainer(ChatterBotCorpusTrainer)(key, value)

def respond(input_str):
    response = chatbot.get_response(input_str)
    st.write(response)

if __name__ == "__main__":
    st.write("Welcome to College Buddy!")
    input_str = st.text_input("Enter your query here.")
    col1, col2 = st.columns([1,0.1])
    with col1:
        ask = st.button("ASK")
    with col2:
        quit = st.button("QUIT")
    if(ask):
        respond(input_str)
    if(quit):
        st.write("Thank you for using the Chatbot")