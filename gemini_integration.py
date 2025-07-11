import os
from google import genai
import streamlit as st

def get_gemini_analysis(passions, strengths, market_needs):
    """
    Get Gemini AI analysis of the user's hedgehog profile.
    
    Args:
        passions (list): List of user's passions
        strengths (list): List of user's strengths
        market_needs (list): List of user's market needs
    
    Returns:
        str: HTML formatted analysis from Gemini
    """
    try:
        # Get API key from streamlit secrets
        try:
            api_key = st.secrets["GOOGLE_API_KEY"]
        except KeyError:
            return "<p>Error: Google API key not found in .streamlit/secrets.toml file.</p>"
            
        # Initialize Gemini API
        client = genai.Client(api_key=api_key)
        
        # Format the inputs for the prompt
        passions_str = "\n".join([f"- {p}" for p in passions])
        strengths_str = "\n".join([f"- {s}" for s in strengths])
        market_needs_str = "\n".join([f"- {m}" for m in market_needs])
        
        # Create prompt for Gemini
        prompt = f"""
        You are an expert career coach and personal development advisor. I'm going to share information about 
        a person's passions, strengths, and identified market needs based on Jim Collins' Hedgehog Concept.
        
        Please analyze this information and provide:
        1. A summary of how these three areas might intersect to form their "Hedgehog Concept" - their optimal 
           career path or life focus
        2. Specific, actionable directions for improving and developing their strengths
        3. Suggestions for how they might better align their passions and strengths with market needs
        4. Potential career paths or business opportunities that leverage all three areas
        
        Format your response with clear headings and bullet points where appropriate. Be specific, practical, 
        and encouraging.
        
        ## USER'S PASSIONS (Activities they love doing and could do all night):
        {passions_str}
        
        ## USER'S STRENGTHS (What they're naturally good at):
        {strengths_str}
        
        ## MARKET NEEDS (What they can provide that the world needs):
        {market_needs_str}
        """
        
        # Create a Gemini model instance
        model = 'gemini-2.5-flash'
        
        # Get response from Gemini
        response = client.models.generate_content(
            contents=prompt,
            model=model
        )
        
        # Extract and return the response content
        return response.text
        
    except Exception as e:
        return f"<p>Error connecting to Gemini API: {str(e)}</p>"
