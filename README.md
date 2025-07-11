# Hedgehog Strength Finder

A Streamlit web application for identifying your personal strengths based on Jim Collins' Hedgehog Concept. This tool helps you find your sweet spot at the intersection of three critical areas:

1. **Passion**: What you're deeply passionate about
2. **Strength**: What you can be the best at (natural talents and skills)
3. **Market Need**: What drives your economic engine (what the world needs)

## Features

- Interactive UI for inputting passions, strengths, and market needs
- Visual representation of the Hedgehog Concept
- AI-powered analysis using Google GenAI Flash 2.5 to provide personalized insights and improvement directions
- Easy to use interface with step-by-step guidance

## Screenshots

The application includes a visual representation of the Hedgehog Concept using the included `Hedgehog-Concept-Full.jpg` image.

## Requirements

- Python 3.8+
- Streamlit
- Gemini API key (for Gemini AI integration)
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/strength-finder-hedgehog.git
   cd strength-finder-hedgehog
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Get an API key from Google GenAI:
   - Sign up at [Google GenAI Console](https://aistudio.google.com/apikey)
   - Create an API key

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your browser and navigate to the provided URL (typically http://localhost:8501)

3. Enter your Gemini API key in the sidebar

4. Navigate through the three sections:
   - Home: Introduction to the Hedgehog Concept
   - Your Profile: Enter your passions, strengths, and market needs
   - Analysis & Visualization: View your Hedgehog analysis and get AI insights

## How to Use

1. Start by filling out all three sections in the "Your Profile" page:
   - List activities you're passionate about
   - List your natural strengths and talents
   - List market needs you can fulfill

2. Save each section using the respective "Save" buttons

3. Navigate to the "Analysis & Visualization" page

4. Click "Get Gemini Analysis" to receive personalized insights and recommendations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- Based on Jim Collins' Hedgehog Concept from his book "Good to Great"
- Uses Streamlit for the web interface
- Powered by Gemini AI from Google for personalized analysis
