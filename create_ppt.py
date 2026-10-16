"""
PowerPoint Presentation Generator (14 Slides)
Generates Indus_Tourist_Guide_Presentation.pptx using python-pptx.
Adheres strictly to CE0525 Course Syllabus & Project Architecture.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # Set slide dimensions to widescreen 16:9
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette Constants
    NAVY = RGBColor(30, 58, 138)       # #1E3A8A - Primary Header
    BLUE_ACCENT = RGBColor(37, 99, 235) # #2563EB - Secondary Blue
    AMBER = RGBColor(217, 119, 6)      # #D97706 - Accent Orange
    DARK_TEXT = RGBColor(15, 23, 42)    # #0F172A - Body Text
    GRAY_TEXT = RGBColor(100, 116, 139) # #64748B - Subtitles
    WHITE = RGBColor(255, 255, 255)
    LIGHT_BG = RGBColor(248, 250, 252)  # #F8FAFC
    CARD_BG = RGBColor(241, 245, 249)   # #F1F5F9

    def add_header(slide, title_text, category_text="CE0525: PROGRAMMING FOR SCIENTIFIC COMPUTING"):
        # Header Background Banner
        header_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
        header_shape.fill.solid()
        header_shape.fill.fore_color.rgb = NAVY
        header_shape.line.fill.background()

        # Category Pill / Top Text
        txBox_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.3))
        tf_cat = txBox_cat.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = AMBER

        # Main Slide Title
        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.6))
        tf = txBox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = WHITE

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.fill.background()

    # Title Card Inner Shape
    card1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5))
    card1.fill.solid()
    card1.fill.fore_color.rgb = WHITE
    card1.line.color.rgb = AMBER
    card1.line.width = Pt(3)

    tf1 = card1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.6)
    tf1.margin_top = Inches(0.5)

    p = tf1.paragraphs[0]
    p.text = "INDUS INSTITUTE OF TECHNOLOGY & ENGINEERING"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = AMBER
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "Department of Computer Science & Engineering"
    p.font.size = Pt(13)
    p.font.color.rgb = GRAY_TEXT
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "\nINDUS TOURIST GUIDE SYSTEM"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "Scientific Computing & Data Structures Python Web Application\n"
    p.font.size = Pt(18)
    p.font.italic = True
    p.font.color.rgb = BLUE_ACCENT
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "Course Code: CE0525 | Credit Points: 4 | Semester V"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = DARK_TEXT
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "\nCourse Coordinator: Ass. Prof. Sweta Rathod"
    p.font.size = Pt(13)
    p.font.color.rgb = DARK_TEXT
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "Course Lecturers: Ass. Prof. Madhvi Bera | Ass. Prof. Babita Patel | Ass. Prof. Anjali Chopra | Ass. Prof. Namrata Bhrambhatt | Ass. Prof. Devyangini Vasava"
    p.font.size = Pt(11)
    p.font.color.rgb = GRAY_TEXT
    p.alignment = PP_ALIGN.CENTER

    # ==========================================
    # SLIDE 2: EXECUTIVE SUMMARY & OBJECTIVES
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Executive Summary & Project Objectives")

    # Left Box - Problem Statement & Overview
    box_l = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.5))
    box_l.fill.solid()
    box_l.fill.fore_color.rgb = CARD_BG
    box_l.line.color.rgb = BLUE_ACCENT

    tf_l = box_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = Inches(0.3)
    tf_l.margin_top = Inches(0.3)

    p = tf_l.paragraphs[0]
    p.text = "🎯 Project Vision & Problem Statement"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = NAVY

    items_l = [
        "Develop an end-to-end Tourist Guide system built 100% in Python.",
        "Demonstrate practical application of Scientific Computing & Data Structures.",
        "Provide both a Web Application interface (Flask) and a Desktop Management tool (Tkinter).",
        "Implement real-world dataset analytics, route planning, booking management, and certified guide directory.",
        "Strict compliance with CE0525 University Course Syllabus."
    ]
    for item in items_l:
        p = tf_l.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    # Right Box - Key Objectives
    box_r = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.5))
    box_r.fill.solid()
    box_r.fill.fore_color.rgb = CARD_BG
    box_r.line.color.rgb = AMBER

    tf_r = box_r.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = Inches(0.3)
    tf_r.margin_top = Inches(0.3)

    p = tf_r.paragraphs[0]
    p.text = "🚀 Key Engineering Objectives"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = AMBER

    items_r = [
        "1. Web & Desktop Dual Interface: Flask microframework + Tkinter desktop GUI.",
        "2. Custom Data Structures: Singly Linked List for day-by-day tour itineraries.",
        "3. Algorithmic Processing: Selection Sort, Merge Sort, Linear Search, Binary Search.",
        "4. Scientific Analytics: Pandas statistical summarization & Matplotlib plotting.",
        "5. Object-Oriented Design: Encapsulation, Single/Multiple Inheritance, Method Overriding."
    ]
    for item in items_r:
        p = tf_r.add_paragraph()
        p.text = item
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(10)

    # ==========================================
    # SLIDE 3: SYLLABUS ALIGNMENT TABLE
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "University Course Syllabus Alignment (CE0525)")

    table_shape = slide3.shapes.add_table(5, 3, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.5))
    table = table_shape.table
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(4.5)
    table.columns[2].width = Inches(5.0)

    headers = ["Syllabus Unit", "Core Course Concepts Covered", "Project Implementation & Modules"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        for p in cell.text_frame.paragraphs:
            p.font.bold = True
            p.font.color.rgb = WHITE
            p.font.size = Pt(13)

    rows_data = [
        ("UNIT I\n(Basic Elements)", "Branching, Looping, Functions, Recursion, Files (CSV/TXT), Lists, Tuples, Dicts, Sets, lambda, map(), filter().", "data_initializer.py, utils.py\nFile I/O persistence, Higher-Order category filtering and promotional discount mapping."),
        ("UNIT II\n(OOP & Data Structures)", "Classes, Encapsulation, Single/Multiple Inheritance, Method Overriding, Singly Linked List, Searching/Sorting, re, threading.", "models.py, utils.py\nTouristSpot & Booking classes, Local/Agency Guide inheritance, Itinerary LinkedList, Linear/Binary search, Selection/Merge sort."),
        ("UNIT III\n(GUI & Plotting)", "Tkinter GUI (Widgets, Dropdowns, Treeview, Forms, Canvas), NumPy arrays, Matplotlib / PyLab bar & pie charts.", "admin_gui.py, utils.py\nTkinter Multi-tab Desktop Admin Tool, NumPy array calculations, Matplotlib bar chart of ratings & pie chart of category distribution."),
        ("UNIT IV\n(Pandas & Web)", "Python Pandas (Data Alignment, Aggregation, Summarization describe()), Basics of Web development (Flask Framework).", "app.py, utils.py\nFlask web server with dynamic routing, Jinja2 rendering, Pandas df.describe() statistical analytics table.")
    ]

    for row_idx, r in enumerate(rows_data, start=1):
        for col_idx, text in enumerate(r):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG if row_idx % 2 == 1 else WHITE
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11)
                p.font.color.rgb = DARK_TEXT

    # ==========================================
    # SLIDE 4: SYSTEM ARCHITECTURE & TECH STACK
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "System Architecture & Technology Stack")

    # Architecture Cards (3 Horizontal Columns)
    col_w = Inches(3.64)
    gap = Inches(0.4)

    cols = [
        ("🌐 Presentation Layer", NAVY, [
            "Flask Web Application (app.py)",
            "Bootstrap 5 Responsive Layout",
            "Dynamic Jinja2 Template Views",
            "Tkinter Desktop Admin Tool (admin_gui.py)",
            "Interactive Treeview & OptionMenu"
        ]),
        ("⚙️ Business & Logic Layer", BLUE_ACCENT, [
            "OOP Domain Models (models.py)",
            "Singly Linked List Itinerary Engine",
            "Linear & Binary Search Modules",
            "Selection & Merge Sort Engines",
            "Regex Input Validation (utils.py)"
        ]),
        ("📊 Analytics & Data Layer", AMBER, [
            "Pandas DataFrame & Aggregation",
            "NumPy Vectorized Calculations",
            "Matplotlib Chart Generator",
            "CSV File Persistence Engine",
            "TXT File Reviews & Audit Logs"
        ])
    ]

    for idx, (col_title, color, bullet_list) in enumerate(cols):
        left_pos = Inches(0.8) + idx * (col_w + gap)
        box = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, Inches(1.5), col_w, Inches(5.4))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = color
        box.line.width = Pt(2)

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = col_title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = color

        for bullet in bullet_list:
            p = tf.add_paragraph()
            p.text = "• " + bullet
            p.font.size = Pt(12)
            p.font.color.rgb = DARK_TEXT
            p.space_before = Pt(10)

    # ==========================================
    # SLIDE 5: UNIT I - DATA PERSISTENCE & HIGHER-ORDER FUNCTIONS
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Unit I: Data Persistence & Higher-Order Functions")

    box_l5 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.5))
    box_l5.fill.solid()
    box_l5.fill.fore_color.rgb = CARD_BG
    box_l5.line.color.rgb = NAVY

    tf_l5 = box_l5.text_frame
    tf_l5.word_wrap = True
    tf_l5.margin_left = Inches(0.3)
    tf_l5.margin_top = Inches(0.3)

    p = tf_l5.paragraphs[0]
    p.text = "📁 File Handling (CSV & Text Files)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY

    items_l5 = [
        "Structured CSV Files: destinations.csv, guides.csv, bookings.csv.",
        "Unstructured TXT Files: reviews.txt for user feedback.",
        "File Operations: open(), read(), write(), append ('a'), and DictReader.",
        "Audit Logging: Asynchronous file writes for security tracking."
    ]
    for item in items_l5:
        p = tf_l5.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    box_r5 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.5))
    box_r5.fill.solid()
    box_r5.fill.fore_color.rgb = CARD_BG
    box_r5.line.color.rgb = AMBER

    tf_r5 = box_r5.text_frame
    tf_r5.word_wrap = True
    tf_r5.margin_left = Inches(0.3)
    tf_r5.margin_top = Inches(0.3)

    p = tf_r5.paragraphs[0]
    p.text = "⚡ Higher-Order Functions (lambda, map, filter)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = AMBER

    p = tf_r5.add_paragraph()
    p.text = "1. Category Filtering with filter() & lambda:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(8)

    p = tf_r5.add_paragraph()
    p.text = "   filter_spots_by_category = lambda spots, cat:\n   list(filter(lambda s: s.category.lower() == cat.lower(), spots))"
    p.font.size = Pt(11)
    p.font.name = "Consolas"
    p.font.color.rgb = DARK_TEXT

    p = tf_r5.add_paragraph()
    p.text = "2. Price Discount Calculation with map() & lambda:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.space_before = Pt(12)

    p = tf_r5.add_paragraph()
    p.text = "   calculate_discounted_prices = lambda spots:\n   list(map(lambda s: s.price * 0.90, spots))"
    p.font.size = Pt(11)
    p.font.name = "Consolas"
    p.font.color.rgb = DARK_TEXT

    # ==========================================
    # SLIDE 6: UNIT II - OOP & ENCAPSULATION
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Unit II: Object-Oriented Programming & Encapsulation")

    box_l6 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.5))
    box_l6.fill.solid()
    box_l6.fill.fore_color.rgb = CARD_BG
    box_l6.line.color.rgb = BLUE_ACCENT

    tf_l6 = box_l6.text_frame
    tf_l6.word_wrap = True
    tf_l6.margin_left = Inches(0.3)
    tf_l6.margin_top = Inches(0.3)

    p = tf_l6.paragraphs[0]
    p.text = "🔒 Encapsulation & Protected Attributes"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    items_l6 = [
        "Encapsulated State: Price (_price) and Rating (_rating) are protected attributes.",
        "Property Decorators: Getter and Setter methods control access.",
        "Data Validation: Setters enforce rules (e.g., price >= 0, rating between 0.0 and 5.0).",
        "Information Hiding: Internal representation hidden from client caller."
    ]
    for item in items_l6:
        p = tf_l6.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    box_r6 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.5))
    box_r6.fill.solid()
    box_r6.fill.fore_color.rgb = CARD_BG
    box_r6.line.color.rgb = NAVY

    tf_r6 = box_r6.text_frame
    tf_r6.word_wrap = True
    tf_r6.margin_left = Inches(0.3)
    tf_r6.margin_top = Inches(0.3)

    p = tf_r6.paragraphs[0]
    p.text = "💻 Code Implementation (TouristSpot Class)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY

    code_text6 = """class TouristSpot:
    def __init__(self, spot_id, name, price, rating):
        self.spot_id = spot_id
        self.name = name
        self._price = float(price)   # Protected
        self._rating = float(rating) # Protected

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = float(value)"""

    p = tf_r6.add_paragraph()
    p.text = code_text6
    p.font.size = Pt(11)
    p.font.name = "Consolas"
    p.font.color.rgb = DARK_TEXT

    # ==========================================
    # SLIDE 7: UNIT II - INHERITANCE & METHOD OVERRIDING
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Unit II: Inheritance & Method Overriding")

    # Diagram Boxes
    b_base = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.5), Inches(1.4), Inches(4.3), Inches(1.3))
    b_base.fill.solid()
    b_base.fill.fore_color.rgb = NAVY

    tf = b_base.text_frame
    p = tf.paragraphs[0]
    p.text = "Base Class: BaseGuide"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    p = tf.add_paragraph()
    p.text = "calculate_fee(hours) = hourly_rate * hours"
    p.font.size = Pt(11)
    p.font.color.rgb = AMBER
    p.alignment = PP_ALIGN.CENTER

    b_local = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(3.5), Inches(5.0), Inches(3.2))
    b_local.fill.solid()
    b_local.fill.fore_color.rgb = CARD_BG
    b_local.line.color.rgb = BLUE_ACCENT
    b_local.line.width = Pt(2)

    tf_loc = b_local.text_frame
    tf_loc.margin_left = Inches(0.2)
    p = tf_loc.paragraphs[0]
    p.text = "Single Inheritance: LocalGuide"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    items_loc = [
        "Inherits from BaseGuide.",
        "Overridden Method: calculate_fee(hours)",
        "Applies 10% community tourist discount:",
        "return base_fee * 0.90"
    ]
    for item in items_loc:
        p = tf_loc.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT

    b_agency = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(3.5), Inches(5.0), Inches(3.2))
    b_agency.fill.solid()
    b_agency.fill.fore_color.rgb = CARD_BG
    b_agency.line.color.rgb = AMBER
    b_agency.line.width = Pt(2)

    tf_ag = b_agency.text_frame
    tf_ag.margin_left = Inches(0.2)
    p = tf_ag.paragraphs[0]
    p.text = "Single Inheritance: AgencyGuide"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = AMBER

    items_ag = [
        "Inherits from BaseGuide.",
        "Overridden Method: calculate_fee(hours)",
        "Applies 15% agency insurance surcharge:",
        "return base_fee * 1.15"
    ]
    for item in items_ag:
        p = tf_ag.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT

    # ==========================================
    # SLIDE 8: UNIT II - SINGLY LINKED LIST DATA STRUCTURE
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Unit II: Custom Data Structure — Singly Linked List")

    # Linked List Node Visualization
    nodes = [
        ("Head Node\nDay 1: Welcome & Arrival", "Duration: 4 hrs"),
        ("Node 2\nDay 2: Guided Sightseeing", "Duration: 7 hrs"),
        ("Node 3\nDay 3: Culture & Market", "Duration: 6 hrs"),
        ("Tail Node\nDay 4: Departure Walk", "Next: None")
    ]

    n_w = Inches(2.6)
    n_gap = Inches(0.4)
    for idx, (title, sub) in enumerate(nodes):
        l_pos = Inches(0.8) + idx * (n_w + n_gap)
        n_box = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l_pos, Inches(1.6), n_w, Inches(1.8))
        n_box.fill.solid()
        n_box.fill.fore_color.rgb = NAVY if idx == 0 else (BLUE_ACCENT if idx < 3 else AMBER)

        tf_n = n_box.text_frame
        p = tf_n.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        p = tf_n.add_paragraph()
        p.text = sub
        p.font.size = Pt(11)
        p.font.color.rgb = CARD_BG
        p.alignment = PP_ALIGN.CENTER

    # Bottom Explanation Card
    box_b8 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.8), Inches(11.733), Inches(3.1))
    box_b8.fill.solid()
    box_b8.fill.fore_color.rgb = CARD_BG
    box_b8.line.color.rgb = BLUE_ACCENT

    tf_b8 = box_b8.text_frame
    tf_b8.word_wrap = True
    tf_b8.margin_left = Inches(0.3)
    tf_b8.margin_top = Inches(0.25)

    p = tf_b8.paragraphs[0]
    p.text = "⛓️ ItineraryLinkedList Data Structure Implementation"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY

    items_b8 = [
        "ItineraryNode: Stores day_num, title, activity, duration_hrs, and next pointer.",
        "Sequential Route Traversal: Navigates day-by-day tour stops linearly.",
        "Operations Implemented: insert_step() at end, display() list conversion, delete_step() by day number.",
        "Use Case: Dynamically formats tour itineraries for destinations in destination_detail view."
    ]
    for item in items_b8:
        p = tf_b8.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(6)

    # ==========================================
    # SLIDE 9: UNIT II - SEARCHING & SORTING ALGORITHMS
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Unit II: Searching & Sorting Algorithms")

    box_l9 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.5))
    box_l9.fill.solid()
    box_l9.fill.fore_color.rgb = CARD_BG
    box_l9.line.color.rgb = NAVY

    tf_l9 = box_l9.text_frame
    tf_l9.word_wrap = True
    tf_l9.margin_left = Inches(0.3)
    tf_l9.margin_top = Inches(0.3)

    p = tf_l9.paragraphs[0]
    p.text = "🔍 Searching Techniques"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY

    items_l9 = [
        "1. Linear Search (linear_search_destinations):",
        "   - Scans name, location, state, category, and description.",
        "   - Case-insensitive string matching.",
        "2. Binary Search (binary_search_destinations):",
        "   - Operates on spot_id sorted array in O(log n) time.",
        "   - Divide-and-conquer search strategy."
    ]
    for item in items_l9:
        p = tf_l9.add_paragraph()
        p.text = item
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    box_r9 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.5))
    box_r9.fill.solid()
    box_r9.fill.fore_color.rgb = CARD_BG
    box_r9.line.color.rgb = AMBER

    tf_r9 = box_r9.text_frame
    tf_r9.word_wrap = True
    tf_r9.margin_left = Inches(0.3)
    tf_r9.margin_top = Inches(0.3)

    p = tf_r9.paragraphs[0]
    p.text = "📊 Sorting Algorithms"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = AMBER

    items_r9 = [
        "1. Selection Sort (selection_sort_destinations):",
        "   - Sorts destinations by price (Low to High or High to Low).",
        "   - In-place comparative sorting algorithm.",
        "2. Merge Sort (merge_sort_destinations):",
        "   - Recursive divide-and-conquer sorting algorithm.",
        "   - Sorts tourist spots by rating to display Top-Rated destinations on Home page."
    ]
    for item in items_r9:
        p = tf_r9.add_paragraph()
        p.text = item
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 10: UNIT II - REGULAR EXPRESSIONS & MULTITHREADING
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Unit II: Regular Expressions & Multithreading")

    box_l10 = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.5))
    box_l10.fill.solid()
    box_l10.fill.fore_color.rgb = CARD_BG
    box_l10.line.color.rgb = BLUE_ACCENT

    tf_l10 = box_l10.text_frame
    tf_l10.word_wrap = True
    tf_l10.margin_left = Inches(0.3)
    tf_l10.margin_top = Inches(0.3)

    p = tf_l10.paragraphs[0]
    p.text = "🔤 Regular Expressions (re Module)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    items_l10 = [
        "Email Pattern: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
        "Phone Pattern: ^[6-9]\\d{9}$ (10-digit Indian phone validation).",
        "Date Pattern: ^\\d{4}-\\d{2}-\\d{2}$ (YYYY-MM-DD format).",
        "Regex Review Search: re.search() matches query patterns across user feedback text."
    ]
    for item in items_l10:
        p = tf_l10.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    box_r10 = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.5))
    box_r10.fill.solid()
    box_r10.fill.fore_color.rgb = CARD_BG
    box_r10.line.color.rgb = NAVY

    tf_r10 = box_r10.text_frame
    tf_r10.word_wrap = True
    tf_r10.margin_left = Inches(0.3)
    tf_r10.margin_top = Inches(0.3)

    p = tf_r10.paragraphs[0]
    p.text = "🧵 Multithreading (threading.Thread)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY

    items_r10 = [
        "Asynchronous Logging: Launches background thread upon new booking creation.",
        "Non-blocking Execution: Web server returns instant response to user while thread logs to file.",
        "Audit Log File: system_audit.log records timestamps and booking activities.",
        "Thread Safety: Independent log file appends without main thread blocking."
    ]
    for item in items_r10:
        p = tf_r10.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================
    # SLIDE 11: UNIT III - TKINTER DESKTOP MANAGEMENT GUI
    # ==========================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Unit III: Tkinter Desktop Management GUI")

    box_main11 = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(11.733), Inches(5.5))
    box_main11.fill.solid()
    box_main11.fill.fore_color.rgb = CARD_BG
    box_main11.line.color.rgb = AMBER
    box_main11.line.width = Pt(2)

    tf_11 = box_main11.text_frame
    tf_11.word_wrap = True
    tf_11.margin_left = Inches(0.4)
    tf_11.margin_top = Inches(0.3)

    p = tf_11.paragraphs[0]
    p.text = "🖥️ Desktop Admin Interface (admin_gui.py)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = AMBER

    gui_features = [
        "Multi-Tab Layout (ttk.Notebook): Organized into Destinations Catalog, Add Spot Form, Fare Calculator, and Syllabus Mapping tabs.",
        "Interactive Data Table (ttk.Treeview): Displays destinations with columns (ID, Name, Location, Category, Price, Rating, State).",
        "Category Dropdown Filter (ttk.OptionMenu): Dynamically filters treeview records by tourist spot category.",
        "Destination Entry Form: Inputs new tourist spot records, performs float/int validation, and appends to destinations.csv.",
        "Tour Fare Calculator: Computes base cost, guide fees, and 5% GST tax estimate with instant output display."
    ]
    for feat in gui_features:
        p = tf_11.add_paragraph()
        p.text = "• " + feat
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    # ==========================================
    # SLIDE 12: UNIT III & IV - SCIENTIFIC COMPUTING & DATA ANALYTICS
    # ==========================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Unit III & IV: Scientific Computing & Data Analytics")

    col12_w = Inches(3.64)
    cols12 = [
        ("📈 Pandas Data Analysis", NAVY, [
            "df.describe() statistical table",
            "Mean price & duration",
            "Standard deviation",
            "Group-by category counts",
            "Total booking revenue sum"
        ]),
        ("🔢 NumPy Array Computing", BLUE_ACCENT, [
            "Vectorized prices array",
            "np.mean() average price",
            "np.std() price standard dev",
            "np.max() & np.min() range",
            "Array matrix math"
        ]),
        ("📊 Matplotlib Chart Generation", AMBER, [
            "Bar Chart: Category Ratings",
            "Pie Chart: Spot Distribution",
            "Saved as PNG static assets",
            "Agg non-interactive backend",
            "Embedded in Web Dashboard"
        ])
    ]

    for idx, (col_title, color, bullet_list) in enumerate(cols12):
        left_pos = Inches(0.8) + idx * (col12_w + gap)
        box = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, Inches(1.5), col12_w, Inches(5.4))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = color
        box.line.width = Pt(2)

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = col_title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = color

        for bullet in bullet_list:
            p = tf.add_paragraph()
            p.text = "• " + bullet
            p.font.size = Pt(12)
            p.font.color.rgb = DARK_TEXT
            p.space_before = Pt(12)

    # ==========================================
    # SLIDE 13: UNIT IV - FLASK WEB APPLICATION ARCHITECTURE
    # ==========================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Unit IV: Flask Web Application Architecture")

    box_m13 = slide13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(11.733), Inches(5.5))
    box_m13.fill.solid()
    box_m13.fill.fore_color.rgb = CARD_BG
    box_m13.line.color.rgb = NAVY
    box_m13.line.width = Pt(2)

    tf_13 = box_m13.text_frame
    tf_13.word_wrap = True
    tf_13.margin_left = Inches(0.4)
    tf_13.margin_top = Inches(0.3)

    p = tf_13.paragraphs[0]
    p.text = "🌐 Flask Microframework & Web Routes Architecture"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = NAVY

    routes_info = [
        "/ (Home): Featured top-rated destinations (Merge Sort) and quick statistics counters.",
        "/destinations: Catalog with category filter (lambda), budget filter, and price/rating sorting.",
        "/destination/<id>: Detailed view with Singly Linked List itinerary, guide rates, and booking form.",
        "/book: POST route receiving booking data, validating email/phone with Regex, and appending to CSV.",
        "/bookings: View all confirmed user tour bookings persisted in CSV.",
        "/guides: Certified tour guide directory demonstrating OOP inheritance and overridden fee calculations.",
        "/reviews: Submit traveler reviews and regex search pattern matching across feedback.",
        "/analytics: Scientific Analytics dashboard displaying Pandas describe() table & Matplotlib PNG charts."
    ]
    for r_item in routes_info:
        p = tf_13.add_paragraph()
        p.text = "• " + r_item
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 14: TESTING, VERIFICATION & CONCLUSION
    # ==========================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "Testing, Verification & Project Conclusion")

    box_l14 = slide14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.5))
    box_l14.fill.solid()
    box_l14.fill.fore_color.rgb = CARD_BG
    box_l14.line.color.rgb = BLUE_ACCENT

    tf_l14 = box_l14.text_frame
    tf_l14.word_wrap = True
    tf_l14.margin_left = Inches(0.3)
    tf_l14.margin_top = Inches(0.3)

    p = tf_l14.paragraphs[0]
    p.text = "✅ Unit Test Verification (test_suite.py)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    test_results = [
        "Test Suite Status: 10 / 10 Tests PASSED (OK).",
        "File I/O Test: Successfully loads & parses CSV/TXT.",
        "OOP & Encapsulation Test: Validates setter constraints.",
        "Inheritance Test: Verifies overridden calculate_fee().",
        "Linked List Test: Verifies node insert/delete operations.",
        "Searching & Sorting Test: Validates Linear/Binary search & Selection/Merge sort accuracy."
    ]
    for t in test_results:
        p = tf_l14.add_paragraph()
        p.text = "• " + t
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(8)

    box_r14 = slide14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.5))
    box_r14.fill.solid()
    box_r14.fill.fore_color.rgb = CARD_BG
    box_r14.line.color.rgb = AMBER

    tf_r14 = box_r14.text_frame
    tf_r14.word_wrap = True
    tf_r14.margin_left = Inches(0.3)
    tf_r14.margin_top = Inches(0.3)

    p = tf_r14.paragraphs[0]
    p.text = "🎓 Conclusion & Summary"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = AMBER

    summary_items = [
        "100% Course Compliance: Successfully integrated all topics across Units I, II, III, and IV.",
        "Dual Interface Advantage: Seamless combination of Flask Web app and Tkinter Desktop tool.",
        "Scientific Computing: Scientific data analysis executed with Pandas, NumPy, and Matplotlib.",
        "Practical Relevance: Real-world usable application for tourism & guide booking."
    ]
    for s_item in summary_items:
        p = tf_r14.add_paragraph()
        p.text = "• " + s_item
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT
        p.space_before = Pt(10)

    p = tf_r14.add_paragraph()
    p.text = "\nThank You! Questions & Answers"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Indus_Tourist_Guide_Presentation.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    create_presentation()
