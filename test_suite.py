"""
Comprehensive Test Suite for Tourist Guide Website
Verifies 100% syllabus compliance (CE0525) across all modules.
"""

import unittest
import os
import csv

from models import (
    TouristSpot, LocalGuide, AgencyGuide, Booking,
    ItineraryLinkedList, linear_search_destinations, binary_search_destinations,
    selection_sort_destinations, merge_sort_destinations
)
from utils import (
    load_destinations, load_guides, load_bookings, load_reviews,
    validate_email, validate_phone, validate_date, regex_search_reviews,
    filter_spots_by_category, calculate_discounted_prices,
    generate_analytics_data, generate_plots
)
from app import app

class TestSyllabusModules(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_01_file_handling(self):
        """UNIT I: Test File Reading & Parsing"""
        spots = load_destinations()
        self.assertGreater(len(spots), 0)
        self.assertIsInstance(spots[0], TouristSpot)
        print("[PASS] Unit I File Handling Test Passed")

    def test_02_oop_and_encapsulation(self):
        """UNIT II: Test OOP & Encapsulation Properties"""
        spot = TouristSpot(99, "Test Spot", "Test City", "Heritage", 1000, 4.5, "Desc", 2, "Gujarat")
        self.assertEqual(spot.price, 1000)
        spot.price = 1200
        self.assertEqual(spot.price, 1200)

        with self.assertRaises(ValueError):
            spot.price = -500
        print("[PASS] Unit II OOP & Encapsulation Test Passed")

    def test_03_inheritance_and_overriding(self):
        """UNIT II: Test Single Inheritance & Method Overriding"""
        local_guide = LocalGuide(101, "Local", 5, 500, 4.8, "English", "9876543210")
        agency_guide = AgencyGuide(102, "Agency", 5, 500, 4.8, "English", "9812345678")

        # Overridden 4-hour fee calculations
        self.assertEqual(local_guide.calculate_fee(4), 1800.0)    # 2000 * 0.90 (10% discount)
        self.assertEqual(agency_guide.calculate_fee(4), 2300.0)   # 2000 * 1.15 (15% surcharge)
        print("[PASS] Unit II Inheritance & Method Overriding Test Passed")

    def test_04_singly_linked_list(self):
        """UNIT II: Test Singly Linked List Data Structure"""
        itinerary = ItineraryLinkedList()
        itinerary.insert_step(1, "Day 1", "Arrival", 4)
        itinerary.insert_step(2, "Day 2", "Tour", 6)

        steps = itinerary.display()
        self.assertEqual(len(steps), 2)
        self.assertEqual(steps[0]["title"], "Day 1")
        self.assertEqual(steps[1]["title"], "Day 2")

        itinerary.delete_step(1)
        steps_after = itinerary.display()
        self.assertEqual(len(steps_after), 1)
        self.assertEqual(steps_after[0]["title"], "Day 2")
        print("[PASS] Unit II Singly Linked List Data Structure Test Passed")

    def test_05_searching_algorithms(self):
        """UNIT II: Test Linear & Binary Search"""
        spots = load_destinations()
        # Linear Search
        results = linear_search_destinations(spots, "Agra")
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0].name, "Taj Mahal")

        # Binary Search
        sorted_spots = sorted(spots, key=lambda s: s.spot_id)
        found = binary_search_destinations(sorted_spots, 1)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Taj Mahal")
        print("[PASS] Unit II Searching Algorithms Test Passed")

    def test_06_sorting_algorithms(self):
        """UNIT II: Test Selection Sort & Merge Sort"""
        spots = load_destinations()
        
        # Selection Sort by Price (Ascending)
        sel_sorted = selection_sort_destinations(spots, key="price", reverse=False)
        self.assertTrue(sel_sorted[0].price <= sel_sorted[-1].price)

        # Merge Sort by Rating (Descending)
        merge_sorted = merge_sort_destinations(spots, key="rating", reverse=True)
        self.assertTrue(merge_sorted[0].rating >= merge_sorted[-1].rating)
        print("[PASS] Unit II Sorting Algorithms Test Passed")

    def test_07_regular_expressions(self):
        """UNIT II: Test Regular Expressions (re)"""
        self.assertTrue(validate_email("student@indusuni.ac.in"))
        self.assertFalse(validate_email("invalid-email"))

        self.assertTrue(validate_phone("9876543210"))
        self.assertFalse(validate_phone("12345"))

        self.assertTrue(validate_date("2026-10-15"))
        self.assertFalse(validate_date("15-10-2026"))

        # Regex search reviews
        results = regex_search_reviews("guide")
        self.assertIsInstance(results, list)
        print("[PASS] Unit II Regular Expressions Test Passed")

    def test_08_higher_order_functions(self):
        """UNIT I: Test map, filter, lambda"""
        spots = load_destinations()
        heritage_spots = filter_spots_by_category(spots, "Heritage")
        self.assertTrue(all(s.category == "Heritage" for s in heritage_spots))

        discounted = calculate_discounted_prices(spots, 10)
        self.assertEqual(len(discounted), len(spots))
        self.assertEqual(discounted[0]["discounted_price"], round(spots[0].price * 0.90, 2))
        print("[PASS] Unit I Higher-Order Functions Test Passed")

    def test_09_pandas_numpy_matplotlib(self):
        """UNIT III & IV: Test Scientific Data Analysis & Plotting"""
        stats, df_spots, summary_stats = generate_analytics_data()
        self.assertIn("avg_price", stats)
        self.assertIn("price", summary_stats)

        chart1, chart2 = generate_plots()
        self.assertIsNotNone(chart1)
        self.assertIsNotNone(chart2)
        print("[PASS] Unit III & IV Scientific Computing Test Passed")

    def test_10_flask_web_routes(self):
        """UNIT IV: Test Flask Web Routes & Rendering"""
        client = self.client
        
        # Route /
        res_home = client.get('/')
        self.assertEqual(res_home.status_code, 200, f"Error body: {res_home.data.decode('utf-8')}")
        self.assertIn(b"Indus Tourist Guide", res_home.data)

        # Route /destinations
        res_dest = client.get('/destinations')
        self.assertEqual(res_dest.status_code, 200)

        # Route /destination/1
        res_detail = client.get('/destination/1')
        self.assertEqual(res_detail.status_code, 200)
        self.assertIn(b"Taj Mahal", res_detail.data)

        # Route /analytics
        res_analytics = client.get('/analytics')
        self.assertEqual(res_analytics.status_code, 200)
        self.assertIn(b"Scientific Data Analytics Dashboard", res_analytics.data)

        # Route /syllabus
        res_syl = client.get('/syllabus')
        self.assertEqual(res_syl.status_code, 200)
        self.assertIn(b"CE0525", res_syl.data)

        print("[PASS] Unit IV Flask Web Routes Test Passed")

if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
