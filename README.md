# Disesase-prediction-system

A web-based application that predicts diseases based on user-selected symptoms using a simple but effective matching algorithm.

## 📋 Quick Start Guide

1. **Open Command Prompt**
   - Press `Windows + R`
   - Type `cmd`
   - Press `Enter`

2. **Go to Project Directory**
   ```bash
   cd D:\a project
   ```

3. **Activate Virtual Environment**
   ```bash
   venv\Scripts\activate
   ```
   - If you see `(venv)` at the start of the line, it worked!

4. **Run the Website**
   ```bash
   python app.py
   ```
   - Keep this window open while using the website

5. **Open the Website**
   - Open your web browser
   - Go to: `http://localhost:5000`

6. **Stop the Website**
   - When you're done, go back to Command Prompt
   - Press `Ctrl + C` to stop

## 🔍 How to Use

1. **Select Symptoms**
   - Click on any symptoms you have
   - Use the search box to find specific symptoms
   - Selected symptoms will turn blue

2. **Get Prediction**
   - Click "Predict Disease"
   - View the predicted disease and confidence score

## 💡 Features

- 15+ diseases in database
- 40+ symptoms to choose from
- Real-time search
- Confidence score
- Modern UI design

## ⚠️ Important Note

This is a demonstration project and should not be used as a substitute for professional medical advice. Always consult with a healthcare provider for proper medical diagnosis.

## 🔧 Troubleshooting

If you get errors:

1. **"venv is not recognized"**
   - Make sure you're in the correct directory
   - Try creating a new virtual environment:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     pip install -r requirements.txt
     ```

2. **"Module not found"**
   - Make sure you've installed requirements:
     ```bash
     pip install -r requirements.txt
     ```

3. **"Port already in use"**
   - Close any other running Python applications
   - Or try using a different port:
     ```python
     # In app.py, change the last line to:
     app.run(debug=True, port=5001)
     ```


```

## 💻 Requirements

- Python 3.8 or higher
- Web browser (Chrome, Firefox, Edge, etc.)
- Internet connection (for loading CSS and icons)
