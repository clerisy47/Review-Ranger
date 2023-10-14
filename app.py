import streamlit as st
from PIL import Image
from rasa.core.agent import Agent

rasa = Agent.load("models")


def generate_response(text, ratings):
    response = rasa.handle_text(text)
    return response


def generate_response(text, ratings):
    response = rasa.predict({"text": text})
    return response


st.title("Automatic Review Bot")

image = Image.open("image.jpeg")
st.image(image, use_column_width=True)

user_text = st.text_area("Enter your text:", "")

user_ratings = st.slider("Select ratings (out of 5):", 1, 5)

if st.button("Generate Review"):
    if user_text:
        response = generate_response(user_text, user_ratings)
        st.success(response)
    else:
        st.warning("Please enter some text.")

st.info("Enter some text and select the ratings to generate a review.")
