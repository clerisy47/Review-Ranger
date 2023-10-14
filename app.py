import streamlit as st
from PIL import Image
import rasa.shared.utils.io

rasa_model_path = "models"
rasa = rasa.shared.utils.io.load_model(rasa_model_path)

def generate_response(text):
    response = rasa.parse_text(text)
    return response

st.title("Automatic Review Bot")

image = Image.open("image.jpeg") 
st.image(image, use_column_width=True)

user_text = st.text_area("Enter your text:", "")

if st.button("Generate Review"):
    if user_text:
        response = generate_response(user_text)
        st.success(response)
    else:
        st.warning("Please enter some text.")

st.info("Enter some text to generate a review.")
