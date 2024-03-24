from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenerativeAI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    chat = model.start_chat(history=[])
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Recipe Generator")
st.title("🍽 Recipe Generator")

# Input for ingredients
input_text = st.text_input("Enter your ingredients: ", key="input")

# Input for meal type
meal_type = st.selectbox("Select Meal Type:", ["Breakfast", "Lunch", "Dinner"])

# Input for cuisine preference
cuisine_preference = st.selectbox("Select Cuisine Preference:", ["Italian", "Mexican", "Continental", "Other"])

# Input for cooking time
cooking_time = st.selectbox("Select Cooking Time:", ["Less than 30 minutes", "30-60 minutes", "More than 1 hour"])

# Input for complexity
complexity = st.selectbox("Select Complexity:", ["Beginner", "Intermediate", "Advanced"])

# Button to generate recipe
submit_button = st.button("Generate Recipe")

# Check if input_text is not empty and button is clicked
if input_text and submit_button:
    st.subheader("Here's the Recipe:")
    # Create prompt based on user inputs
    prompt = f"Generate a {meal_type.lower()} recipe with {cuisine_preference.lower()} cuisine, {cooking_time.lower()}, and {complexity.lower()} complexity using the following ingredients: {input_text}"
    response = get_gemini_response(prompt)
    for chunk in response:
        st.write(chunk.text)