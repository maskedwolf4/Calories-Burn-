
**# Calorie Burn Prediction App**

**## Overview**

This application utilizes a machine learning model to estimate the number of calories burned during physical activity based on various factors. It's built with Python and Streamlit, providing a user-friendly interface for exploration.

**## Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/maskedwolf4/Calories-Burn-.git
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # (Linux/macOS)
   venv\Scripts\activate.bat  # (Windows)
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

**## Usage**

1. **Run the app:**

   ```bash
   streamlit run cbapp.py
   ```

2. **Enter your information:**
   - Age
   - Height (cm)
   - Weight (kg)
   - Duration of activity (minutes)
   - Heart rate (BPM)
   - Body temperature (°C)

3. **Click "Predict Calories Burned" to generate the prediction.**

**## Model Details**

- **Model type:** Decision Trees
- **Features:**
-  - Age
   - Height (cm)
   - Weight (kg)
   - Duration of activity (minutes)
   - Heart rate (BPM)
   - Body temperature (°C)
- **Performance metrics:**
  - mae= 0.0,
     mse= 0.0,
     r2_score= 1.0,
     rmse= 0.0

**## Disclaimer**

- **Limitations:** Acknowledge that the app provides estimates and shouldn't replace professional advice.
- **Health guidance:** Encourage users to consult healthcare professionals for personalized recommendations.

**## Contribute**

- Feel free to contribute to this project by submitting issues or pull requests.

**## License**

- This app is licensed under  Apache-2.0 license.
