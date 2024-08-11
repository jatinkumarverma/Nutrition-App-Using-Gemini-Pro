from dotenv import load_dotenv
import streamlit as st 
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the Gemini API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        mime_type = uploaded_file.type
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": mime_type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Set up Streamlit page configuration
st.set_page_config(page_title="Gemini Health App")

# App Header
st.header("Gemini Health App")

# Input prompt from the user
input_text = st.text_input("Input Prompt: ", key="input")

# File uploader for images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Submit button
submit = st.button("Tell me the total calories")

# Input prompt template
input_prompt = """
You are an expert nutritionist where you need to see the food items from the image and calculate the total calories, 
also provide the details of every food item with calories intake in the following format:
1. Item 1 - number of calories
2. Item 2 - number of calories
----
----
"""

# Handle the submission
if submit:
    try:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_text, image_data, input_prompt)
        st.subheader("The Response is:")
        st.write(response)
    except FileNotFoundError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
