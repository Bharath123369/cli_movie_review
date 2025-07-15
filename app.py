from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "reviews.json"

# Load reviews from file
def load_reviews():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save reviews to file
def save_reviews(reviews):
    with open(DATA_FILE, "w") as f:
        json.dump(reviews, f, indent=4)

# Route to get all reviews
@app.route("/reviews", methods=["GET"])
def get_reviews():
    return jsonify(load_reviews())

# Route to add a review
@app.route("/reviews", methods=["POST"])
def add_review():
    data = request.get_json()
    required_fields = {"movie", "reviewer", "rating", "comment"}

    if not data or not required_fields.issubset(data):
        return jsonify({"error": "Missing fields"}), 400

    try:
        rating = float(data["rating"])
        if not (0 <= rating <= 5):
            raise ValueError
    except ValueError:
        return jsonify({"error": "Rating must be a number between 0 and 5"}), 400

    review = {
        "movie": data["movie"].strip(),
        "reviewer": data["reviewer"].strip(),
        "rating": rating,
        "comment": data["comment"].strip()
    }

    reviews = load_reviews()
    reviews.append(review)
    save_reviews(reviews)

    return jsonify({"message": "Review added successfully!"}), 201

# Route to get average rating of a movie
@app.route("/reviews/<string:movie>/average", methods=["GET"])
def average_rating(movie):
    reviews = load_reviews()
    movie_reviews = [r for r in reviews if r["movie"].lower() == movie.lower()]

    if not movie_reviews:
        return jsonify({"message": f"No reviews found for '{movie}'"}), 404

    avg = sum(r["rating"] for r in movie_reviews) / len(movie_reviews)
    return jsonify({
        "movie": movie,
        "average_rating": round(avg, 2),
        "review_count": len(movie_reviews)
    })

if __name__ == "__main__":
    app.run(debug=True)
