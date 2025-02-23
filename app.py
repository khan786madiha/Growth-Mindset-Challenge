

import streamlit as st

# Setting up page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟", layout="wide")

# Title and Intro Section
st.title("🌟 Growth Mindset Challenge: Web App with Streamlit 🌟")
st.header("👋 Welcome to Your Growth Journey with Madiha Ali Khan (MAK)")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you on your path to growth.")

# Inspirational Image Section
# Removed as per your request

# Section for Challenges
st.header("🔍 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:", placeholder="E.g., Struggling with time management")

if user_input:
    st.success(f"💪 You're facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

 # Reflection Section
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:", placeholder="E.g., I learned that taking breaks helps me focus better.")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your thoughts.")

# Section to Celebrate Wins
st.header("🎉 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:", placeholder="E.g., Completed a difficult project on time.")

if achievement:
    st.success(f"🌟 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now.")

# Motivational Quotes Section
st.header("💬 Today's Growth Mindset Quotes")
quotes = [
    "“The only way to achieve the impossible is to believe it is possible.” - Charles Kingsleigh",
    "“Don't watch the clock; do what it does. Keep going.” - Sam Levenson",
    "“Hardships often prepare ordinary people for an extraordinary destiny.” - C.S. Lewis",
    "“Success is not how high you have climbed, but how you make a positive difference to the world.” - Roy T. Bennett",
    "“What lies behind us and what lies before us are tiny matters compared to what lies within us.” - Ralph Waldo Emerson"
]

for quote in quotes:
    st.write(f"- {quote}")

# Interactive Poll Section
st.header("📊 Quick Poll")
poll = st.radio("How do you feel about your progress?", ['Very Confident', 'Confident', 'Neutral', 'Unsure', 'Struggling'])

# Displaying Poll Results
if poll:
    st.write(f"Thank you for sharing! It's great to hear that you feel '{poll}' about your progress. Keep going! 💪")

# Footer with Personalized Message
st.write("-" * 40)
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**Created by Madiha Ali Khan (MAK)**")
