#!/usr/bin/env python3
"""
Test script to verify the setup for Video RAG with Gemini
"""

import sys
import os
from dotenv import load_dotenv

def test_imports():
    """Test if all required packages are installed"""
    print("🔍 Testing imports...")
    
    try:
        import streamlit
        print(f"✅ Streamlit: {streamlit.__version__}")
    except ImportError:
        print("❌ Streamlit not installed. Run: pip install streamlit")
        return False
    
    try:
        # Modern import for Google Generative AI
        from google import genai
        print(f"✅ Google GenerativeAI (modern): {genai.__version__}")
    except ImportError:
        print("❌ Google GenerativeAI (modern) not installed. Run: pip install google-genai")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ Python-dotenv: Available")
    except ImportError:
        print("❌ Python-dotenv not installed. Run: pip install python-dotenv")
        return False
    
    return True

def test_api_key():
    """Test if API key is configured"""
    print("\n🔑 Testing API key configuration...")
    
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("⚠️  GEMINI_API_KEY not found in environment")
        print("   You can either:")
        print("   1. Create a .env file with GEMINI_API_KEY=your_key")
        print("   2. Enter the API key directly in the Streamlit app")
        print("   Get your key from: https://aistudio.google.com/app/apikey")
        return False
    
    if len(api_key) < 10:
        print("⚠️  API key seems too short, please verify")
        return False
    
    print("✅ API key found and looks valid")
    return True

def test_gemini_connection():
    """Test connection to Gemini API"""
    print("\n🌐 Testing Gemini API connection...")
    
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("⚠️  Skipping connection test - no API key")
        return False
    
    try:
        # Modern import for Google Generative AI
        from google import genai
        # Initialize the client
        client = genai.Client(api_key=api_key)
        
        # Try to list models to test connection
        models = list(client.models.list()) # Use client.models.list()
        print(f"✅ Connected to Gemini API - {len(models)} models available")
        
        # Check if the required model is available
        model_names = [m.name for m in models]
        if 'models/gemini-1.5-pro' in model_names:
            print("✅ Gemini 1.5 Pro model is available")
        else:
            print("⚠️  Gemini 1.5 Pro model not found in available models")
            print("   Available models:", [m.name for m in models[:3]])
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to connect to Gemini API: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Video RAG Setup Test")
    print("=" * 30)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test API key
    if not test_api_key():
        all_passed = False
    
    # Test connection
    if not test_gemini_connection():
        all_passed = False
    
    print("\n" + "=" * 30)
    if all_passed:
        print("🎉 All tests passed! You're ready to run the Video RAG app.")
        print("   Run: streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
