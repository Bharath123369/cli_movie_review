import json
import os

DATA_FILE = "reviews.json"

def load_reviews():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_reviews(reviews):
    with open(DATA_FILE, "w") as f:
        json.dump(reviews, f, indent=4)

def add_review():
    movie = input("Enter movie title: ").strip()
    reviewer = input("Enter your name: ").strip()
    try:
        rating = float(input("Enter rating (0 to 5): ").strip())
        if not (0 <= rating <= 5):
            raise ValueError
    except ValueError:
        print("Invalid rating. Please enter a number between 0 and 5.")
        return
    comment = input("Enter your comment: ").strip()

    reviews = load_reviews()
    reviews.append({
        "movie": movie,
        "reviewer": reviewer,
        "rating": rating,
        "comment": comment
    })
    save_reviews(reviews)
    print("Review added successfully!")

def average_rating():
    movie = input("Enter movie title to calculate average rating: ").strip()
    reviews = load_reviews()
    movie_reviews = [r for r in reviews if r["movie"].lower() == movie.lower()]

    if not movie_reviews:
        print(f"No reviews found for '{movie}'.")
        return

    avg = sum(r["rating"] for r in movie_reviews) / len(movie_reviews)
    print(f"Average rating for '{movie}': {avg:.2f} ({len(movie_reviews)} reviews)")

def menu():
    while True:
        print("\n=== Movie Review System ===")
        print("1. Add Movie Review")
        print("2. Show Average Rating")
        print("3. Exit")

        choice = input("Select an option (1–3): ").strip()

        if choice == "1":
            add_review()
        elif choice == "2":
            average_rating()
        elif choice == "3":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()