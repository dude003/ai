import streamlit as st

knowledge_base = {
    "weight_loss": [
        "1: Cardio exercises like running, cycling, or swimming",
        "2: High-intensity interval training (HIIT)",
        "3: Calorie deficit diet - focus on whole foods",
        "4: Regular hydration and adequate sleep"
    ],
    "muscle_gain": [
        "1: Strength training with weights",
        "2: Bodyweight exercises like push-ups, pull-ups",
        "3: Protein-rich diet with balanced carbs and fats",
        "4: Consistent workout schedule with rest days for recovery"
    ],
    "improve_flexibility": [
        "1: Daily stretching routines",
        "2: Yoga sessions multiple times a week",
        "3: Incorporate pilates for core strength",
        "4: Stay hydrated and practice mindfulness"
    ],
    "general_fitness": [
        "1: Combination of cardio and strength training",
        "2: Regular outdoor activities like hiking or team sports",
        "3: Balanced diet with plenty of vegetables and fruits",
        "4: Regular sleep schedule and stress management techniques"
    ]
}

st.header("Fitness and Wellness Plan Recommendation System")

def respond(input):
    fitness_goals, current_fitness, diet_preference, time_availability = input

    if ("lose weight" in fitness_goals and "beginner" in current_fitness and "no restrictions" in diet_preference and "limited time" in time_availability):
        st.write("Based on your inputs, here is a recommended fitness and wellness plan for weight loss:")
        for item in knowledge_base["weight_loss"]:
            st.write(item)
    elif ("gain muscle" in fitness_goals and "intermediate" in current_fitness and "high protein" in diet_preference and "ample time" in time_availability):
        st.write("Based on your inputs, here is a recommended plan for muscle gain:")
        for item in knowledge_base["muscle_gain"]:
            st.write(item)
    elif ("increase flexibility" in fitness_goals and "beginner" in current_fitness and "vegetarian" in diet_preference and "moderate time" in time_availability):
        st.write("Based on your inputs, here is a recommended plan to improve flexibility:")
        for item in knowledge_base["improve_flexibility"]:
            st.write(item)
    elif ("stay active" in fitness_goals and "advanced" in current_fitness and "no restrictions" in diet_preference and "limited time" in time_availability):
        st.write("Based on your inputs, here is a recommended plan for general fitness:")
        for item in knowledge_base["general_fitness"]:
            st.write(item)
    else:
        st.write("Please adjust your selections to get a tailored fitness plan.")

if __name__ == "__main__":
    fitness_goals = st.selectbox("Select your fitness goal:", ["lose weight", "gain muscle", "increase flexibility", "stay active"])
    current_fitness = st.selectbox("What is your current fitness level?", ["beginner", "intermediate", "advanced"])
    diet_preference = st.selectbox("What is your dietary preference?", ["no restrictions", "vegetarian", "high protein"])
    time_availability = st.selectbox("How much time can you dedicate?", ["limited time", "moderate time", "ample time"])

    if st.button("Get Fitness Plan Recommendations"):
        respond([fitness_goals, current_fitness, diet_preference, time_availability])