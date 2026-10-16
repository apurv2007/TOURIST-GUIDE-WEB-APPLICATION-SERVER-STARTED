"""
Utilities & Analytics Module
Implements File Handling, Regular Expressions (re), Higher-Order Functions (map, filter, lambda),
Multithreading, NumPy, Pandas, and Matplotlib chart generation.
All concepts strictly map to CE0525 course syllabus.
"""

import os
import csv
import re
import threading
import time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for web rendering
import matplotlib.pyplot as plt

from models import (
    TouristSpot, LocalGuide, AgencyGuide, Booking,
    ItineraryLinkedList, linear_search_destinations, selection_sort_destinations, merge_sort_destinations
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
STATIC_DIR = os.path.join(BASE_DIR, "static")

if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)


# ==========================================
# 1. FILE HANDLING & DATA READING (Unit I)
# ==========================================

def load_destinations():
    """Reads destinations from CSV file using Python csv module."""
    dest_path = os.path.join(DATA_DIR, "destinations.csv")
    spots = []
    if not os.path.exists(dest_path):
        return spots

    with open(dest_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            spot = TouristSpot(
                spot_id=row["id"],
                name=row["name"],
                location=row["location"],
                category=row["category"],
                price=row["price"],
                rating=row["rating"],
                description=row["description"],
                duration_days=row["duration_days"],
                state=row["state"]
            )
            spots.append(spot)
    return spots


def load_guides():
    """Reads tour guides from CSV file, instantiating LocalGuide or AgencyGuide objects."""
    guides_path = os.path.join(DATA_DIR, "guides.csv")
    guides = []
    if not os.path.exists(guides_path):
        return guides

    with open(guides_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            g_type = row.get("guide_type", "LocalGuide")
            if g_type == "LocalGuide":
                guide = LocalGuide(
                    guide_id=row["id"],
                    name=row["name"],
                    experience_yrs=row["experience_yrs"],
                    hourly_rate=row["hourly_rate"],
                    rating=row["rating"],
                    languages=row["languages"],
                    phone=row["phone"]
                )
            else:
                guide = AgencyGuide(
                    guide_id=row["id"],
                    name=row["name"],
                    experience_yrs=row["experience_yrs"],
                    hourly_rate=row["hourly_rate"],
                    rating=row["rating"],
                    languages=row["languages"],
                    phone=row["phone"]
                )
            guides.append(guide)
    return guides


def load_bookings():
    """Reads user tour bookings from CSV file."""
    bookings_path = os.path.join(DATA_DIR, "bookings.csv")
    bookings = []
    if not os.path.exists(bookings_path):
        return bookings

    with open(bookings_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            b = Booking(
                booking_id=row["id"],
                spot_id=row["spot_id"],
                spot_name=row["spot_name"],
                user_name=row["user_name"],
                user_email=row["user_email"],
                user_phone=row["user_phone"],
                travel_date=row["travel_date"],
                num_travelers=row["num_travelers"],
                total_cost=row["total_cost"]
            )
            bookings.append(b)
    return bookings


def save_booking(spot_id, spot_name, user_name, user_email, user_phone, travel_date, num_travelers, total_cost):
    """Appends a new booking record into CSV file using Python file append ('a')."""
    bookings_path = os.path.join(DATA_DIR, "bookings.csv")
    new_id = 1001
    existing_bookings = load_bookings()
    if existing_bookings:
        new_id = max(b.booking_id for b in existing_bookings) + 1

    with open(bookings_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([new_id, spot_id, spot_name, user_name, user_email, user_phone, travel_date, num_travelers, total_cost])

    # Trigger background multithreaded logging
    log_thread = threading.Thread(target=async_log_activity, args=(f"New booking #{new_id} for {user_name} on {spot_name}",))
    log_thread.start()

    return new_id


def load_reviews():
    """Reads reviews from text file using Python open() and split()."""
    reviews_path = os.path.join(DATA_DIR, "reviews.txt")
    reviews = []
    if not os.path.exists(reviews_path):
        return reviews

    with open(reviews_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) >= 4:
                reviews.append({
                    "spot": parts[0],
                    "user": parts[1],
                    "rating": parts[2],
                    "comment": parts[3]
                })
    return reviews


def save_review(spot_name, user_name, rating, comment):
    """Appends a review string to reviews.txt file."""
    reviews_path = os.path.join(DATA_DIR, "reviews.txt")
    review_line = f"{spot_name} | {user_name} | {rating} | {comment}\n"
    with open(reviews_path, "a", encoding="utf-8") as f:
        f.write(review_line)


# ==========================================
# 2. REGULAR EXPRESSIONS (Unit II: re)
# ==========================================

def validate_email(email):
    """Validates email format using Regular Expression pattern."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, str(email).strip()))


def validate_phone(phone):
    """Validates 10-digit phone number starting with 6-9 using Regex."""
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, str(phone).strip()))


def validate_date(date_str):
    """Validates YYYY-MM-DD date pattern using Regex."""
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    return bool(re.match(pattern, str(date_str).strip()))


def regex_search_reviews(query):
    """Retrieves reviews containing a specific word or pattern using re.search."""
    reviews = load_reviews()
    matching = []
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    for r in reviews:
        if pattern.search(r["comment"]) or pattern.search(r["spot"]):
            matching.append(r)
    return matching


# ==========================================
# 3. HIGHER-ORDER FUNCTIONS (Unit I: lambda, map, filter)
# ==========================================

def filter_spots_by_category(spots, category):
    """Uses filter() and lambda to filter spots by category."""
    if not category or category.lower() == "all":
        return spots
    return list(filter(lambda s: s.category.lower() == category.lower(), spots))


def filter_spots_by_budget(spots, max_price):
    """Uses filter() and lambda to extract spots under max_price."""
    return list(filter(lambda s: s.price <= max_price, spots))


def calculate_discounted_prices(spots, discount_percentage=10):
    """Uses map() and lambda to calculate promotional discounted prices for all spots."""
    factor = (100 - discount_percentage) / 100.0
    discounted_list = list(map(lambda s: {
        "id": s.spot_id,
        "name": s.name,
        "original_price": s.price,
        "discounted_price": round(s.price * factor, 2)
    }, spots))
    return discounted_list


# ==========================================
# 4. MULTITHREADING IN PYTHON (Unit II)
# ==========================================

def async_log_activity(message):
    """Simulates background task logging using threading.Thread."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [BACKGROUND THREAD] {message}\n"
    log_file = os.path.join(DATA_DIR, "system_audit.log")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_line)


# ==========================================
# 5. PANDAS, NUMPY & MATPLOTLIB ANALYTICS (Unit III & IV)
# ==========================================

def generate_analytics_data():
    """
    Computes statistical analysis using Pandas and NumPy (Unit IV & III).
    """
    spots = load_destinations()
    bookings = load_bookings()

    if not spots:
        return {}, None, None

    # Convert spots list to Pandas DataFrame
    spots_data = [s.to_dict() for s in spots]
    df_spots = pd.DataFrame(spots_data)

    # Statistical Data Summarization with Pandas describe()
    summary_stats = df_spots[["price", "rating", "duration_days"]].describe().to_dict()

    # NumPy Array Computing & Calculations
    prices_array = np.array(df_spots["price"])
    ratings_array = np.array(df_spots["rating"])

    stats_dict = {
        "total_spots": int(len(df_spots)),
        "avg_price": round(float(np.mean(prices_array)), 2),
        "std_price": round(float(np.std(prices_array)), 2),
        "max_price": float(np.max(prices_array)),
        "min_price": float(np.min(prices_array)),
        "avg_rating": round(float(np.mean(ratings_array)), 2),
        "category_counts": df_spots["category"].value_counts().to_dict(),
        "state_counts": df_spots["state"].value_counts().to_dict()
    }

    # Bookings Analysis using Pandas Aggregation
    if bookings:
        bookings_data = [b.to_dict() for b in bookings]
        df_bookings = pd.DataFrame(bookings_data)
        stats_dict["total_bookings"] = int(len(df_bookings))
        stats_dict["total_revenue"] = float(df_bookings["total_cost"].sum())
        stats_dict["avg_travelers"] = round(float(df_bookings["num_travelers"].mean()), 1)
    else:
        stats_dict["total_bookings"] = 0
        stats_dict["total_revenue"] = 0.0
        stats_dict["avg_travelers"] = 0

    return stats_dict, df_spots, summary_stats


def generate_plots():
    """
    Generates Matplotlib bar chart and pie chart plots (Unit III).
    Saves plots as PNG images in static directory.
    """
    stats_dict, df_spots, _ = generate_analytics_data()
    if df_spots is None or df_spots.empty:
        return None, None

    # 1. Bar Chart: Rating by Destination Category (Pandas + Matplotlib)
    fig, ax = plt.subplots(figsize=(7, 4))
    cat_ratings = df_spots.groupby("category")["rating"].mean()
    categories = cat_ratings.index
    ratings = cat_ratings.values

    colors = ['#2b5c8f', '#d97736', '#2e8b57', '#8b2b5c', '#d9a736', '#5c2b8f']
    ax.bar(categories, ratings, color=colors[:len(categories)], width=0.5)
    ax.set_title("Average Tourist Rating by Category", fontsize=12, fontweight='bold', pad=12)
    ax.set_xlabel("Destination Category", fontsize=10)
    ax.set_ylabel("Average Rating (Out of 5.0)", fontsize=10)
    ax.set_ylim(0, 5.5)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    chart1_path = os.path.join(STATIC_DIR, "category_ratings.png")
    plt.savefig(chart1_path, dpi=120)
    plt.close()

    # 2. Pie Chart: Destination Distribution by Category
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    cat_counts = df_spots["category"].value_counts()
    ax2.pie(cat_counts.values, labels=cat_counts.index, autopct='%1.1f%%', startangle=140, colors=colors[:len(cat_counts)])
    ax2.set_title("Tourist Spot Share by Category", fontsize=12, fontweight='bold')
    plt.tight_layout()

    chart2_path = os.path.join(STATIC_DIR, "category_distribution.png")
    plt.savefig(chart2_path, dpi=120)
    plt.close()

    return "category_ratings.png", "category_distribution.png"


def build_sample_itinerary(duration_days):
    """Builds a Singly Linked List itinerary based on duration."""
    itinerary = ItineraryLinkedList()
    activities = [
        (1, "Day 1: Arrival & Welcome", "Hotel check-in, orientation session, and evening heritage walk.", 4),
        (2, "Day 2: Guided Sightseeing Tour", "Full day visit to primary landmarks, monuments & photo spots.", 7),
        (3, "Day 3: Culture & Local Cuisine", "Explore local artisan markets, traditional lunch, and cultural show.", 6),
        (4, "Day 4: Nature & Departure", "Early morning scenic viewpoint, souvenir shopping, and departure transfer.", 4)
    ]
    for i in range(min(duration_days, len(activities))):
        day, title, act, dur = activities[i]
        itinerary.insert_step(day, title, act, dur)
    return itinerary.display()
