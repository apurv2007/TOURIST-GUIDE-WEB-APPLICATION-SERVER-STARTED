"""
Data Initializer Module for Tourist Guide Website
Populates initial sample CSV and TXT data files using Python File Handling.
All concepts strictly map to CE0525 (Files, Structured Objects, Mutability).
"""
import os
import csv

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

def init_data_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # 1. Destinations CSV
    destinations_file = os.path.join(DATA_DIR, "destinations.csv")
    if not os.path.exists(destinations_file):
        destinations = [
            ["id", "name", "location", "category", "price", "rating", "description", "duration_days", "state"],
            [1, "Taj Mahal", "Agra", "Heritage", 1500, 4.9, "Iconic marble mausoleum built by Shah Jahan in memory of Mumtaz Mahal.", 1, "Uttar Pradesh"],
            [2, "Jaipur City Palace & Forts", "Jaipur", "Heritage", 2200, 4.8, "Explore Amber Fort, Hawa Mahal, and royal Rajasthani heritage.", 2, "Rajasthan"],
            [3, "Kerala Backwaters Cruise", "Alleppey", "Nature", 3500, 4.7, "Serene houseboat cruising along emerald backwaters and palm groves.", 3, "Kerala"],
            [4, "Varanasi Ghats & Ganga Aarti", "Varanasi", "Spiritual", 1200, 4.6, "Spiritual experience along ancient ghats and sacred evening Aarti.", 2, "Uttar Pradesh"],
            [5, "Goa Sun & Beaches", "Panaji", "Beach", 2800, 4.5, "Golden beaches, water sports, vibrant local markets and seafood.", 3, "Goa"],
            [6, "Manali Mountain Trek", "Manali", "Adventure", 4000, 4.8, "Snowy Himalayan trails, Solang Valley sports, and pine forests.", 4, "Himachal Pradesh"],
            [7, "Statue of Unity & Dam", "Kevadia", "Modern", 1800, 4.7, "World's tallest statue dedicated to Sardar Vallabhbhai Patel.", 1, "Gujarat"],
            [8, "Gir National Park Safari", "Junagadh", "Wildlife", 3200, 4.6, "Home to the endangered Asiatic Lions in their natural habitat.", 2, "Gujarat"],
            [9, "Rann of Kutch Desert Festival", "Bhuj", "Culture", 3000, 4.9, "White salt desert under moonlight with vibrant Gujarati folk culture.", 3, "Gujarat"],
            [10, "Darjeeling Tea Gardens", "Darjeeling", "Nature", 2500, 4.7, "Panoramic views of Kanchenjunga peak and lush green tea estates.", 3, "West Bengal"]
        ]
        with open(destinations_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(destinations)
        print("Created destinations.csv")

    # 2. Guides CSV
    guides_file = os.path.join(DATA_DIR, "guides.csv")
    if not os.path.exists(guides_file):
        guides = [
            ["id", "name", "guide_type", "experience_yrs", "hourly_rate", "rating", "languages", "phone"],
            [101, "Rajesh Sharma", "LocalGuide", 8, 500, 4.9, "Hindi, English", "9876543210"],
            [102, "Ananya Sen", "AgencyGuide", 5, 800, 4.8, "English, Bengali, Hindi", "9812345678"],
            [103, "Vikram Rathore", "LocalGuide", 12, 600, 4.9, "Hindi, Rajasthani, English", "9988776655"],
            [104, "Priya Nair", "AgencyGuide", 6, 750, 4.7, "Malayalam, English, Tamil", "9744556677"],
            [105, "Bhavesh Patel", "LocalGuide", 10, 550, 4.8, "Gujarati, Hindi, English", "9825012345"]
        ]
        with open(guides_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(guides)
        print("Created guides.csv")

    # 3. Bookings CSV
    bookings_file = os.path.join(DATA_DIR, "bookings.csv")
    if not os.path.exists(bookings_file):
        bookings = [
            ["id", "spot_id", "spot_name", "user_name", "user_email", "user_phone", "travel_date", "num_travelers", "total_cost"],
            [1001, 1, "Taj Mahal", "Aarav Mehta", "aarav@example.com", "9898012345", "2026-10-15", 2, 3000],
            [1002, 3, "Kerala Backwaters Cruise", "Riya Patel", "riya@example.com", "9727011223", "2026-11-01", 3, 10500],
            [1003, 7, "Statue of Unity & Dam", "Amit Shah", "amit@example.com", "9909012345", "2026-10-20", 4, 7200],
            [1004, 9, "Rann of Kutch Desert Festival", "Neha Joshi", "neha@example.com", "9879011122", "2026-12-05", 2, 6000]
        ]
        with open(bookings_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(bookings)
        print("Created bookings.csv")

    # 4. Reviews Text File
    reviews_file = os.path.join(DATA_DIR, "reviews.txt")
    if not os.path.exists(reviews_file):
        reviews = [
            "Taj Mahal | Aarav Mehta | 5 | Unforgettable sunrise view of Taj Mahal! Guide was super knowledgeable.",
            "Kerala Backwaters Cruise | Riya Patel | 5 | So peaceful and delicious Kerala traditional food served on houseboat.",
            "Statue of Unity & Dam | Amit Shah | 4 | Great architecture and light show in the evening!",
            "Jaipur City Palace | Dev Patel | 5 | Stunning royal history and brilliant photo spots."
        ]
        with open(reviews_file, "w", encoding="utf-8") as f:
            for r in reviews:
                f.write(r + "\n")
        print("Created reviews.txt")

if __name__ == "__main__":
    init_data_files()
