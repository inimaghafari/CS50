# QFFARRI Clothing Store (Python Project)

#### Video Demo: <URL>

#### Description:

This project is a console-based shopping system for a fictional clothing brand called **QFFARRI**.
Users can browse products, add items to their cart, generate a receipt as a **PDF**, store purchase history, and receive **music ** based on the clothing category they buy.
The project uses multiple Python files, JSON databases, automated testing with `pytest`, and external libraries such as **pygame** and **FPDF**.

---

## 📌 **Project Structure**

```
project/
│
├── project.py
├── store.py
├── music.py
├── test_project.py
├── pytest.ini
├── README.md
├── requirements.txt
│
├── data/
│   ├── products.json
│   ├── music.json
│   └── sales.json
│
├── music/
│   └── (mp3 music files)
│
└── receipts/
    └── (auto-generated PDFs)
```

---

## 📌 **How the Program Works**

### **1. project.py (Main Program)**

This is the main entry point of the application.

**Features:**

* Greets the user with a typing-animation effect.
* Asks for name and optionally shows previous purchases.
* Displays all available products.
* Lets the user select items by name and adds them to a shopping cart.
* Saves every purchase to `data/sales.json`.
* Creates a **PDF receipt** inside the `receipts/` folder using `FPDF`.
* Recommends and plays music based on the first product category in the cart.
* Allows clearing a customer's entire purchase history.

**Important Functions:**

* `type_print()` — typing animation
* `play_music()` — plays songs in a separate thread
* `search_product_by_name()` — finds items from JSON
* `get_cart_total()` — calculates total price
* `view_previous_purchases()` — displays purchase history
* `clear_sales_for_customer()` — removes old purchases
* PDF generation using **FPDF**
* Music recommendation and playback

---

### **2. store.py (Store & Product Classes)**

This file handles product data and shopping cart logic.

**Classes:**

* `Product` — stores name, category, price
* `Store`

  * Loads all products from `data/products.json`
  * Displays product list
  * Searches items by name
  * Adds items to cart
  * Calculates total price

---

### **3. music.py (Music Recommendations)**

Loads the music database and selects a random track for each category.

**Functions:**

* `recommend_music(category)`

  * Picks a random file from `data/music.json`
  * Returns correct file path (absolute or relative)

---

### **4. JSON Files**

#### **products.json**

Contains all clothing items with:

* name
* category
* price

Used by the Store system.

#### **music.json**

Each category (Classic, Sport, Casual, Street) has a list of recommended songs.
Files must match the mp3 names inside the `music/` folder.

#### **sales.json**

Stores purchase receipts.
Example entry:

```json
{
  "customer": "Nima",
  "items": [
    {"name": "Classic Shirt", "category": "Classic", "price": 60}
  ],
  "total": 60,
  "date": "2025-12-10 18:30"
}
```

---

### **5. test_project.py (Unit Tests)**

Uses `pytest` to verify:

* Shopping cart total calculation
* Music recommendation returns valid strings
* Product search works correctly

Covers:

* Correct product lookup
* None return for missing products
* Music recommendation functionality
* Cart total math

---

### **6. pytest.ini**

Disables a specific deprecation warning:

```
[pytest]
filterwarnings =
    ignore:pkg_resources is deprecated as an API
```

---

## 📌 **External Libraries Required**

These must be installed using pip:

```
pip install pygame
pip install fpdf
```

Both are used for:

* Music playback (pygame)
* PDF receipt generation (FPDF)

---

## 📌 **How to Run the Program**

1. Make sure folder structure is exactly like shown above.
2. Install required libraries:

   ```
   pip install pygame fpdf
   ```
3. Run the main program:

   ```
   python project.py
   ```

If you're using VS Code or PyCharm, make sure the working directory is set to the **project folder**.

---

## 📌 **Conclusion**

This project demonstrates:

* Object-oriented programming
* JSON data management
* File handling
* PDF generation
* Music playback
* Automated testing
* Clean project structure

It acts as a functional shopping system with multimedia features and persistent purchase history.

---
