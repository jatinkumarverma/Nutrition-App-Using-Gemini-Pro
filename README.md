# Nutrition App Using Gemini Pro

## Overview
The Nutrition App is designed to provide personalized dietary advice and well-being tips by leveraging the advanced capabilities of the Gemini Pro pre-trained model. This application allows users to input their nutritional goals and preferences and receive tailored recommendations that promote healthy eating and lifestyle improvements.

## Project Flow
1. **User Interaction:**
   - Users interact with the UI to enter their dietary goals, preferences, or any other relevant information.
   
2. **Data Transmission:**
   - The user input is collected from the UI and transmitted to the backend using a Google API key.

3. **Model Processing:**
   - The input is forwarded to the Gemini Pro pre-trained model via an API call.
   - The model processes the input and generates personalized nutrition and well-being advice.

4. **Result Display:**
   - The results are returned to the frontend for formatting and display, providing the user with actionable insights.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/jatinkumarverma/nutrition-app.git
   cd nutrition-app
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   Install all required libraries listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### Google API Key Setup

1. **Generate Google API Key:**
   Obtain a Google API key from the Google Cloud Console. Make sure to restrict the API key to your application.

2. **Initialize Google API Key:**
   Set up the Google API key in your application by either:
   - Setting it as an environment variable:
     ```bash
     export GOOGLE_API_KEY='your-api-key'
     ```
   - Including it in your backend configuration.

## Contributing
If you'd like to contribute to the project, please fork the repository and submit a pull request with your proposed changes.
