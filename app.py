import streamlit as st
import os
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from gemini_integration import get_gemini_analysis

# Page configuration
st.set_page_config(
    page_title="Hedgehog Strength Finder",
    page_icon="🦔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS for custom styling
st.markdown("""
<style>
    .header-text {
        font-size: 40px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 24px;
        font-weight: bold;
        color: #1E3A8A;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .footer {
        text-align: center;
        color: #6B7280;
        margin-top: 30px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Function to load and display the hedgehog image
def display_hedgehog_image():
    try:
        image = Image.open("Hedgehog-Concept-Full.jpg")
        st.image(image, use_container_width=True)
    except FileNotFoundError:
        st.error("Hedgehog image not found. Make sure 'Hedgehog-Concept-Full.jpg' is in the project directory.")

# Session state initialization
if 'passion' not in st.session_state:
    st.session_state.passion = []
if 'strength' not in st.session_state:
    st.session_state.strength = []
if 'market_need' not in st.session_state:
    st.session_state.market_need = []
if 'gemini_analysis' not in st.session_state:
    st.session_state.gemini_analysis = None
if 'api_key_set' not in st.session_state:
    st.session_state.api_key_set = False
if 'show_venn' not in st.session_state:
    st.session_state.show_venn = False

# Initialize page in session state if not exists
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Sidebar for navigation
st.sidebar.markdown("<div class='section-header'>Navigation</div>", unsafe_allow_html=True)

# Functions to change page
def set_page(page_name):
    st.session_state.page = page_name

# Create sidebar navigation
st.sidebar.button("🏠 Home", on_click=set_page, kwargs={"page_name": "Home"}, use_container_width=True)
st.sidebar.button("👤 Your Profile", on_click=set_page, kwargs={"page_name": "Your Profile"}, use_container_width=True)
st.sidebar.button("📊 Analysis & Visualization", on_click=set_page, kwargs={"page_name": "Analysis & Visualization"}, use_container_width=True)

# Get current page
page = st.session_state.page

# Set API key from secrets.toml
st.session_state.api_key_set = True

# Home page
if page == "Home":
    st.markdown("<div class='header-text'>Hedgehog Strength Finder</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
    <p>Welcome to the Hedgehog Strength Finder! Based on Jim Collins' Hedgehog Concept, this tool helps you 
    identify your sweet spot at the intersection of:</p>
    
    <ol>
        <li><strong>Passion:</strong> What you're deeply passionate about</li>
        <li><strong>Strength:</strong> What you can be the best in the world at</li>
        <li><strong>Market Need:</strong> What drives your economic engine (or what the world needs)</li>
    </ol>
    
    <p>At the intersection of these three circles lies your "Hedgehog Concept" - your optimal career path or life focus.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display hedgehog image
    display_hedgehog_image()
    
    st.markdown("""
    <div class='card'>
    <h3>How to use this tool:</h3>
    <ol>
        <li>Navigate to "Your Profile" and fill out the three sections</li>
        <li>Go to "Analysis & Visualization" to see your Hedgehog visualization</li>
        <li>Get personalized insights from Gemini AI on how to improve and develop your strengths</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Add a spacer
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Next button to navigate to Profile page
    st.button("Next: Your Profile", on_click=set_page, kwargs={"page_name": "Your Profile"})

# Profile Page
elif page == "Your Profile":
    st.markdown("<div class='header-text'>Your Hedgehog Profile</div>", unsafe_allow_html=True)
    
    # Passion Section
    st.markdown("<div class='section-header'>1. What are you deeply passionate about?</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
    <p>List activities you love so much you could do them all night without being forced. 
    These are things you're naturally drawn to and want to improve at.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input for passions
    passion_input = st.text_area("Enter what you're passionate about (one item per line):", 
                        height=150, 
                        help="What activities do you love doing? What could you talk about for hours?")
    
    # Save passion function with page preservation
    def save_passions():
        if passion_input:
            # Save the data
            st.session_state.passion = [item.strip() for item in passion_input.split('\n') if item.strip()]
            # Set the page to stay on profile
            st.session_state.page = "Your Profile"
            return True
        return False
    
    # Save passions button
    if st.button("Save Passions"):
        if save_passions():
            st.success(f"Saved {len(st.session_state.passion)} passions!")
        else:
            st.warning("Please enter at least one passion.")
    
    # Strength Section
    st.markdown("<div class='section-header'>2. What are you naturally good at?</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
    <p>List skills and abilities you excel at naturally - these could be from talent, experience, 
    education, or your background. What do others recognize you as being good at?</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input for strengths
    strength_input = st.text_area("Enter what you're naturally good at (one item per line):", 
                         height=150,
                         help="What comes easily to you? What do people compliment you on?")
    
    # Save strengths function with page preservation
    def save_strengths():
        if strength_input:
            # Save the data
            st.session_state.strength = [item.strip() for item in strength_input.split('\n') if item.strip()]
            # Set the page to stay on profile
            st.session_state.page = "Your Profile"
            return True
        return False
    
    # Save strengths button
    if st.button("Save Strengths"):
        if save_strengths():
            st.success(f"Saved {len(st.session_state.strength)} strengths!")
        else:
            st.warning("Please enter at least one strength.")
    
    # Market Need Section
    st.markdown("<div class='section-header'>3. What does the world need that you can provide?</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='card'>
    <p>List services or products you can provide that people would pay for or value. 
    What skills or knowledge do you have that solves real-world problems?</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input for market needs
    market_need_input = st.text_area("Enter what the world needs that you can provide (one item per line):", 
                            height=150,
                            help="What problems can you solve? What would people pay you to do?")
    
    # Save market needs function with page preservation
    def save_market_needs():
        if market_need_input:
            # Save the data
            st.session_state.market_need = [item.strip() for item in market_need_input.split('\n') if item.strip()]
            # Set the page to stay on profile
            st.session_state.page = "Your Profile"
            return True
        return False
    
    # Save market needs button
    if st.button("Save Market Needs"):
        if save_market_needs():
            st.success(f"Saved {len(st.session_state.market_need)} market needs!")
        else:
            st.warning("Please enter at least one market need.")
    
    # Add a spacer
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Next button to navigate to Analysis page
    st.button("Next: Analysis & Visualization", on_click=set_page, kwargs={"page_name": "Analysis & Visualization"})

# Analysis & Visualization Page
elif page == "Analysis & Visualization":
    st.markdown("<div class='header-text'>Your Hedgehog Analysis</div>", unsafe_allow_html=True)
    
    # Check if all sections have data
    all_sections_filled = (len(st.session_state.passion) > 0 and 
                         len(st.session_state.strength) > 0 and 
                         len(st.session_state.market_need) > 0)
    
    if not all_sections_filled:
        st.warning("Please fill out all three sections in Your Profile first.")
    else:
        # Display the data
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='section-header'>Your Passions</div>", unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.passion, 1):
                st.write(f"{i}. {item}")
        
        with col2:
            st.markdown("<div class='section-header'>Your Strengths</div>", unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.strength, 1):
                st.write(f"{i}. {item}")
        
        with col3:
            st.markdown("<div class='section-header'>Market Needs</div>", unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.market_need, 1):
                st.write(f"{i}. {item}")
        
        # Display the hedgehog visualization
        st.markdown("<div class='section-header'>Hedgehog Concept Visualization</div>", unsafe_allow_html=True)
        display_hedgehog_image()
        
        # Gemini Analysis Section
        st.markdown("<div class='section-header'>Gemini AI Analysis</div>", unsafe_allow_html=True)
        
        if st.button("Get Gemini Analysis"):
            with st.spinner("Analyzing your profile with Gemini AI..."):
                analysis = get_gemini_analysis(
                    st.session_state.passion,
                    st.session_state.strength,
                    st.session_state.market_need
                )
                st.session_state.gemini_analysis = analysis
        
        if st.session_state.gemini_analysis:
            st.markdown(f"""
            <div class='card'>
            {st.session_state.gemini_analysis}
            </div>
            """, unsafe_allow_html=True)
            
            # Add export functionality
            col1, col2 = st.columns([1, 2])
            with col1:
                # Create a plain text version for text file export
                analysis_text = st.session_state.gemini_analysis
                st.download_button(
                    label="📄 Download as TXT",
                    data=analysis_text,
                    file_name="hedgehog_analysis.txt",
                    mime="text/plain"
                )
            
            with col2:
                # Create an HTML version for HTML file export
                current_date = pd.Timestamp.now().strftime("%Y-%m-%d")
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Hedgehog Analysis - {current_date}</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
                        h1 {{ color: #1E3A8A; }}
                        h2 {{ color: #2563EB; margin-top: 30px; }}
                        .container {{ max-width: 800px; margin: 0 auto; }}
                        .header {{ text-align: center; margin-bottom: 40px; }}
                        .footer {{ text-align: center; margin-top: 50px; font-size: 0.8em; color: #6B7280; }}
                        .analysis {{ background-color: #f8fafc; padding: 20px; border-radius: 5px; }}
                        .section {{ margin-bottom: 30px; }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h1>Hedgehog Concept Analysis</h1>
                            <p>Generated on {current_date}</p>
                        </div>
                        
                        <div class="section">
                            <h2>Your Passions</h2>
                            <ul>
                                {''.join([f'<li>{item}</li>' for item in st.session_state.passion])}
                            </ul>
                        </div>
                        
                        <div class="section">
                            <h2>Your Strengths</h2>
                            <ul>
                                {''.join([f'<li>{item}</li>' for item in st.session_state.strength])}
                            </ul>
                        </div>
                        
                        <div class="section">
                            <h2>Market Needs</h2>
                            <ul>
                                {''.join([f'<li>{item}</li>' for item in st.session_state.market_need])}
                            </ul>
                        </div>
                        
                        <div class="section">
                            <h2>AI Analysis</h2>
                            <div class="analysis">
                                {st.session_state.gemini_analysis}
                            </div>
                        </div>
                        
                        <div class="footer">
                            <p>Based on Jim Collins' Hedgehog Concept from "Good to Great"</p>
                        </div>
                    </div>
                </body>
                </html>
                """
                
                st.download_button(
                    label="📊 Download as HTML Report",
                    data=html_content,
                    file_name="hedgehog_analysis.html",
                    mime="text/html"
                )

# Footer
st.markdown("""
<div class='footer'>
Hedgehog Strength Finder - Based on Jim Collins' Hedgehog Concept
</div>
""", unsafe_allow_html=True)
