import os
import pickle
import numpy as np
from flask import Flask, render_template, request

# Base directory of this file (so paths work on Render too)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load pickle files safely from project root
popular_df = pickle.load(open(os.path.join(BASE_DIR, "popular.pkl"), "rb"))
pt = pickle.load(open(os.path.join(BASE_DIR, "pt.pkl"), "rb"))
books = pickle.load(open(os.path.join(BASE_DIR, "books.pkl"), "rb"))
similarity_scores = pickle.load(open(os.path.join(BASE_DIR, "similarity_scores.pkl"), "rb"))

# Initialize app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_rating'].values)
    )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Year-Of-Publication'].values))
        data.append(item)

    return render_template('recommend.html', data=data)


# ✅ Important: don't run app.run() when deploying with Gunicorn
if __name__ == "__main__":
    app.run(debug=True)
