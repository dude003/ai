import streamlit as st
bot_name = "College Buddy"

knowledge_base = {
    "what is your name?": [
        f"My name is {bot_name}! Happy to help you out with your College enquiries!"
    ],
    "hello": [
        f"Hello my name is {bot_name}! Happy to help you with your College enquiries!"
    ],
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

def respond(input_str: str):
    input_str = input_str.lower()
    if input_str in knowledge_base:
        values = knowledge_base[input_str]
        for value in values:
            st.write(value)
    else:
        print(input_str)
        key = input_str
        st.write("Question is not present in the knowledge base! \n Could you please enter the appropriate answer?")
        answer = st.text_input("Answer: ")
        add = st.button("Add Answer")

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
