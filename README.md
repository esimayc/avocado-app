# 🥑 Avocado Ripeness Prediction API

Welcome to the **Avocado App**!  
This is a FastAPI project where a deep learning model tries to answer one of the most important questions in life:  

👉 *“How many days until my avocado is ripe?”*  

---

## 🚀 What’s inside?
- A **FastAPI server** 
- A **trained deep learning model** (`avocado_model.keras`)  
- An endpoint where you can upload an avocado photo and get an estimate of how many days are left until it’s ripe


---

## 📂 Project Structure

avocado-app/
│── app/
│ ├── main.py # FastAPI app
│── avocado_model.keras # Trained model
│── requirements.txt # Dependencies
│── README.md # You’re reading this right now
│── .gitignore # Keeps the repo clean


---

## ⚙️ How to run it?
1. Clone the repo 🍴
   ```bash
   git clone https://github.com/esimayc/avocado-app.git
   cd avocado-app

2. Create a virtual environment 🛠️
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows

3. Install the requirements 📦
   pip install -r requirements.txt

4. Launch the API 🚀
   uvicorn app.main:app --reload

5. Open your browser 🌍
   API Root: http://127.0.0.1:8000
   Docs: http://127.0.0.1:8000/docs


---


The model was trained on:

Xavier, Pedro; Rodrigues, Pedro; L. M. Silva, Cristina (2024),
“Hass Avocado Ripening Photographic Dataset”,
Mendeley Data, V1, doi: 10.17632/3xd9n945v8.1

(Dataset is not included here — go grab it from the link if you want to play around!)


---

🤝 Contributing

This project is open to everyone who wants to improve it! 🎉

Whether you want to:

Add new features 💡

Improve the model 🧠

Fix bugs 🐛

Or just make the README look cooler ✨

We’d love your help! Feel free to fork, open issues, and send pull requests.



