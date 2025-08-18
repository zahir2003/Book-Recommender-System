
# 📚 Book Recommender System

A **Machine Learning powered web application** that recommends books to users based on popularity and similarity.
This project is designed to demonstrate my skills in **Machine Learning, Data Science, Flask, and Web Development**, while showcasing how AI can be applied in real-world applications.

---

## 🚀 Features

* 🔍 **Search & Recommend**: Get personalized book recommendations based on user input.
* 📈 **Popularity Based**: Displays the **Top 50 Most Popular Books** with ratings, votes, and author details.
* 🎨 **Interactive UI**: Built with **Flask + HTML/CSS** for a clean and simple user experience.
* ⚡ **Fast & Lightweight**: Uses preprocessed `.pkl` files for efficient loading.
* 🖼️ **Book Images**: Recommendations include **book covers, authors, and ratings**.
* 🌐 **Deployable**: Can be hosted on **Heroku / Render / AWS** using a `Procfile`.

---

## 🛠️ Tech Stack

* **Programming Language:** Python 🐍
* **Frameworks:** Flask
* **Machine Learning:** Scikit-learn, NumPy, Pandas
* **Frontend:** HTML, CSS
* **Storage:** CSV dataset + Pickle (`.pkl`) models
* **Deployment Tools:** Gunicorn, Heroku

---


## ⚙️ How It Works

1. **Popularity-Based Filtering**: Recommends the most popular books (based on average rating & votes).
2. **Collaborative Filtering**: Suggests books similar to the one entered by the user.
3. **Web Application**: User interacts through a simple **Flask web interface**.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/zahir2003/Book-Recommender-System.git
cd Book-Recommender-System
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🌟 Demo Screenshots

### 🔹 Homepage (Popular Books)

Displays top 50 most popular books with images, authors, votes, and ratings.

### 🔹 Recommendation Page

Enter a book name and get **4 similar books** with cover images.

---

## 📊 Datasets

The datasets used in this project are:

* **Books.csv** → Metadata of books (title, author, publication year, image URLs)
* **Ratings.csv** → User ratings for books
* **Users.csv** → User demographic information

---

## 🎯 Future Improvements

* ✅ Add **Content-based filtering** using NLP (book descriptions).
* ✅ Build a **hybrid recommendation system** (Popularity + Collaborative + Content).
* ✅ Deploy on **cloud platforms** with CI/CD pipeline.
* ✅ Add **user authentication** for personalized profiles.

---

## 💡 Learning Outcomes

Through this project, I have practiced and demonstrated:

* Data preprocessing & feature engineering
* Machine learning model building for recommendations
* Flask web development
* Model serialization using **Pickle**
* Deploying ML apps on cloud platforms

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to **fork this repo** and improve the project.

---

## 📬 Contact  
👤 **Sk Mahiduzzaman**  
📧 Email: [Email](mailto:mohiduz03@gmail.com)  
💼 LinkedIn: [LinkedIn](https://www.linkedin.com/in/sk-mahiduzzaman)  

---

✨ *If you like this project, don’t forget to give it a ⭐ on GitHub!*
