"""
Models & Data Structures Module
Implements OOP Classes, Encapsulation, Inheritance, Method Overriding,
Singly Linked List Data Structure, Searching & Sorting Algorithms.
All topics strictly map to CE0525 (Unit II: OOP, Data Structures, Algorithms).
"""

# ==========================================
# 1. OOP & ENCAPSULATION (Unit II)
# ==========================================

class TouristSpot:
    """Represents a Tourist Destination with Encapsulation & Properties."""
    def __init__(self, spot_id, name, location, category, price, rating, description, duration_days, state):
        self.spot_id = int(spot_id)
        self.name = str(name)
        self.location = str(location)
        self.category = str(category)
        self._price = float(price)      # Encapsulated (protected attribute)
        self._rating = float(rating)    # Encapsulated (protected attribute)
        self.description = str(description)
        self.duration_days = int(duration_days)
        self.state = str(state)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = float(value)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if 0 <= value <= 5.0:
            self._rating = float(value)
        else:
            raise ValueError("Rating must be between 0 and 5")

    def to_dict(self):
        """Convert object attributes to dictionary (Structured Objects - Unit I)."""
        return {
            "id": self.spot_id,
            "name": self.name,
            "location": self.location,
            "category": self.category,
            "price": self._price,
            "rating": self._rating,
            "description": self.description,
            "duration_days": self.duration_days,
            "state": self.state
        }


# ==========================================
# 2. INHERITANCE & METHOD OVERRIDING (Unit II)
# ==========================================

class BaseGuide:
    """Base Class demonstrating Abstract Data Types and Encapsulation."""
    def __init__(self, guide_id, name, experience_yrs, hourly_rate, rating, languages, phone):
        self.guide_id = int(guide_id)
        self.name = str(name)
        self.experience_yrs = int(experience_yrs)
        self.hourly_rate = float(hourly_rate)
        self.rating = float(rating)
        self.languages = str(languages)
        self.phone = str(phone)

    def calculate_fee(self, hours):
        """Base method to be overridden by child classes (Method Overriding)."""
        return self.hourly_rate * hours


class LocalGuide(BaseGuide):
    """Single Inheritance: Local Guide with special local discount overriding fee calculation."""
    def __init__(self, guide_id, name, experience_yrs, hourly_rate, rating, languages, phone, local_area="City Center"):
        super().__init__(guide_id, name, experience_yrs, hourly_rate, rating, languages, phone)
        self.local_area = local_area
        self.guide_type = "Local Guide"

    # Method Overriding
    def calculate_fee(self, hours):
        base = super().calculate_fee(hours)
        # Local guides offer 10% discount for community tours
        return round(base * 0.90, 2)


class AgencyGuide(BaseGuide):
    """Single Inheritance: Certified Agency Guide with service charge overriding fee calculation."""
    def __init__(self, guide_id, name, experience_yrs, hourly_rate, rating, languages, phone, agency_name="Royal Travel Co"):
        super().__init__(guide_id, name, experience_yrs, hourly_rate, rating, languages, phone)
        self.agency_name = agency_name
        self.guide_type = "Agency Certified"

    # Method Overriding
    def calculate_fee(self, hours):
        base = super().calculate_fee(hours)
        # Agency adds 15% booking and insurance surcharge
        return round(base * 1.15, 2)


class Booking:
    """Represents a user tour booking with calculation methods."""
    def __init__(self, booking_id, spot_id, spot_name, user_name, user_email, user_phone, travel_date, num_travelers, total_cost):
        self.booking_id = int(booking_id)
        self.spot_id = int(spot_id)
        self.spot_name = str(spot_name)
        self.user_name = str(user_name)
        self.user_email = str(user_email)
        self.user_phone = str(user_phone)
        self.travel_date = str(travel_date)
        self.num_travelers = int(num_travelers)
        self.total_cost = float(total_cost)

    def to_dict(self):
        return {
            "id": self.booking_id,
            "spot_id": self.spot_id,
            "spot_name": self.spot_name,
            "user_name": self.user_name,
            "user_email": self.user_email,
            "user_phone": self.user_phone,
            "travel_date": self.travel_date,
            "num_travelers": self.num_travelers,
            "total_cost": self.total_cost
        }


# ==========================================
# 3. SINGLY LINKED LIST DATA STRUCTURE (Unit II)
# ==========================================

class ItineraryNode:
    """Node of Singly Linked List storing itinerary step."""
    def __init__(self, day_num, title, activity, duration_hrs):
        self.day_num = day_num
        self.title = title
        self.activity = activity
        self.duration_hrs = duration_hrs
        self.next = None


class ItineraryLinkedList:
    """Singly Linked List for managing tour day-by-day itinerary."""
    def __init__(self):
        self.head = None

    def insert_step(self, day_num, title, activity, duration_hrs):
        """Insert node at the end of Singly Linked List."""
        new_node = ItineraryNode(day_num, title, activity, duration_hrs)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Traverse Singly Linked List and return list of step dicts."""
        steps = []
        current = self.head
        while current:
            steps.append({
                "day": current.day_num,
                "title": current.title,
                "activity": current.activity,
                "duration": current.duration_hrs
            })
            current = current.next
        return steps

    def delete_step(self, day_num):
        """Delete node by day number from Singly Linked List."""
        if not self.head:
            return False
        if self.head.day_num == day_num:
            self.head = self.head.next
            return True
        current = self.head
        while current.next and current.next.day_num != day_num:
            current = current.next
        if current.next:
            current.next = current.next.next
            return True
        return False


# ==========================================
# 4. SEARCHING & SORTING ALGORITHMS (Unit II)
# ==========================================

def linear_search_destinations(spots_list, query_str):
    """
    Linear Search Technique (Unit II).
    Searches for query string across name, location, state, or category.
    """
    query = query_str.lower().strip()
    results = []
    for spot in spots_list:
        if (query in spot.name.lower() or 
            query in spot.location.lower() or 
            query in spot.category.lower() or 
            query in spot.state.lower() or 
            query in spot.description.lower()):
            results.append(spot)
    return results


def binary_search_destinations(sorted_spots_list, target_id):
    """
    Binary Search Technique (Unit II).
    Assumes list is sorted by spot_id. Returns matching TouristSpot or None.
    """
    low = 0
    high = len(sorted_spots_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_id = sorted_spots_list[mid].spot_id
        if mid_id == target_id:
            return sorted_spots_list[mid]
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


def selection_sort_destinations(spots_list, key="price", reverse=False):
    """
    Selection Sort Algorithm (Unit II).
    Sorts TouristSpot objects by specified key ('price' or 'rating').
    """
    arr = list(spots_list) # copy list
    n = len(arr)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            val_j = getattr(arr[j], key)
            val_target = getattr(arr[target_idx], key)
            if reverse:
                if val_j > val_target:
                    target_idx = j
            else:
                if val_j < val_target:
                    target_idx = j
        arr[i], arr[target_idx] = arr[target_idx], arr[i]
    return arr


def merge_sort_destinations(spots_list, key="rating", reverse=True):
    """
    Merge Sort Algorithm (Unit II).
    Divide-and-conquer sorting algorithm.
    """
    if len(spots_list) <= 1:
        return spots_list

    mid = len(spots_list) // 2
    left = merge_sort_destinations(spots_list[:mid], key=key, reverse=reverse)
    right = merge_sort_destinations(spots_list[mid:], key=key, reverse=reverse)

    return _merge(left, right, key, reverse)


def _merge(left, right, key, reverse):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        val_left = getattr(left[i], key)
        val_right = getattr(right[j], key)
        if reverse:
            condition = (val_left >= val_right)
        else:
            condition = (val_left <= val_right)

        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
