from store import Store
from music import MusicRecommender
import sys
import json
import pygame
from datetime import datetime
from fpdf import FPDF, XPos, YPos
import time
import os
import threading


# Global setup
date = datetime.now().strftime("%Y-%m-%d %H:%M")
store = Store()
music_recommender = MusicRecommender()


# ==============================
#           FUNCTIONS
# ==============================


def play_music(file_name):
    """Plays music using pygame in a separate thread."""
    def _play():
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(file_name)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        except Exception as e:
            print("Could not play music:", e)

    threading.Thread(target=_play, daemon=True).start()


def type_print(text, speed=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()  # new line at the end


def clear_sales_for_customer(customer_name):
    file_path = r"E:/Python/CS50x/Week 9/project/data/sales.json"
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if not os.path.exists(file_path):
        print("No sales history found.")
        return

    with open(file_path, "r") as f:
        sales_data = json.load(f)

    sales_data = [s for s in sales_data if s["customer"] != customer_name]

    with open(file_path, "w") as f:
        json.dump(sales_data, f, indent=2)

    print(f"All purchase history for {customer_name} cleared.")

def search_product_by_name(name):
    return store.search_product(name)


def get_cart_total():
    return store.get_total_price()


def recommend_music_for_category(category):
    return music_recommender.recommend_music(category)


def view_previous_purchases(customer_name):
    """Display customer's older purchases."""
    with open(r"E:/Python/CS50x\Week 9/project/data/sales.json", "r") as f:
        sales_data = json.load(f)

    customer_purchases = [
        s for s in sales_data if s["customer"] == customer_name
    ]

    if not customer_purchases:
        print("You have no previous purchases.")
        return

    for purchase in customer_purchases:
        print("\nPurchase on", purchase["date"])
        for item in purchase["items"]:
            print(f"{item['name']} - {item['category']} - ${item['price']}")
        print(f"Total: ${purchase['total']}")


# ==============================
#             MAIN
# ==============================

def main():

    type_print("Welcome To QFFARRI Store!")
    type_print("Here you can choose whatever you want, in any style.\n")

    # -----------------------------
    #      INITIAL QUESTIONS
    # -----------------------------
    while True:
        try:
            yes_no = input("Are you ready? ").lower().strip()

            if yes_no not in ["yes", "no"]:
                print("Just say yes or no\n")
                continue

            if yes_no == "yes":
                type_print("So let's go!")
                customer_name = input("Enter your name to start: ").title().strip()

            elif yes_no == "no":
                type_print("Ok, see you later.")
                sys.exit()

            break

        except Exception:
            print("Just say yes or no\n")
            continue

    while True:
        try:
            view_prev = input("Do you want to see your previous purchases? (yes/no/I am new here) ").lower().strip()

            if view_prev not in["yes", "no", "i am new here"]:
                print("Just say yes or no or i am new here\n")
                continue
            elif view_prev == "yes":
                view_previous_purchases(customer_name)
                print("\n")
            elif view_prev == "no":
                type_print("Ok.............\n")
            elif view_prev == "i am new here":
                type_print("\nGreat, every new customer who comes to QFFARRI store becomes our old customer (; .\n")

            break
        except Exception:
            continue
    # -----------------------------
    #     DISPLAY PRODUCTS
    # -----------------------------
    store.display_products()

    # -----------------------------
    #      ADD TO CART LOOP
    # -----------------------------
    while True:
        try:
            customer_choice = input(
                "Tell us the name of the dress you want. (or 'done' to finish): "
            ).strip()

            if customer_choice.lower() == "done":
                break

            product = search_product_by_name(customer_choice)

            if product is None:
                type_print("We don't have what you chose, Please choose a product we have\n")
                continue

            store.add_to_cart(product)
            type_print(f"{product.name} added to your cart!")

        except Exception:
            type_print("We don't have what you chose, Please choose a product we have.\n")
            continue

    # Check if any purchase made
    if not store.cart:
        type_print("You didn't buy anything. Goodbye!")
        sys.exit()
    # -----------------------------
    #     SAVE PURCHASE TO JSON
    # -----------------------------
    receipt = {
        "customer": customer_name,
        "items": [
            {"name": p.name, "category": p.category, "price": p.price}
            for p in store.cart
        ],
        "total": get_cart_total(),
        "date": date
    }

    try:
        with open(r"E:/Python/CS50x/Week 9/project/data/sales.json", "r") as file:
            sales_data = json.load(file)
    except:
        sales_data = []

    sales_data.append(receipt)

    with open(r"E:/Python/CS50x\Week 9/project/data/sales.json", "w") as f:
        json.dump(sales_data, f, indent=2)

    # -----------------------------
    #         CREATE PDF
    # -----------------------------

    pdf = FPDF()
    pdf.add_page()

    # Colors
    burgundy = (128, 0, 32)

    # Title / Logo
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(*burgundy)
    pdf.cell(0, 15, "QFFARRI", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(12)

    # Draw border box (whole page)
    pdf.set_draw_color(100, 100, 100)   # light gray
    pdf.rect(10, 30, 190, 240)          # x, y, width, height

    pdf.ln(10)

    # Reset color for text
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", size=12)

    # Customer info
    pdf.cell(0, 10, f"Receipt for: {customer_name}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, f"Date: {date}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.ln(5)

    # Separator line
    pdf.set_draw_color(180, 180, 180)
    pdf.set_line_width(0.5)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(5)

    # Table Header
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(90, 10, "Product", border=1)
    pdf.cell(50, 10, "Category", border=1)
    pdf.cell(40, 10, "Price", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Table Rows
    pdf.set_font("Helvetica", size=12)
    for item in store.cart:
        pdf.cell(90, 10, item.name, border=1)
        pdf.cell(50, 10, item.category, border=1)
        pdf.cell(40, 10, f"${item.price}", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Total
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 12, f"TOTAL: ${get_cart_total()}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Bottom separator
    pdf.set_draw_color(180, 180, 180)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())

    pdf.ln(8)

    # Footer message
    pdf.set_font("Helvetica", "I", 13)
    pdf.set_text_color(*burgundy)
    pdf.cell(0, 10, "Thank you for shopping at QFFARRI!", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Save PDF
    os.makedirs("receipts", exist_ok=True)
    file_date = date.replace(":", "-").replace(" ", "_")
    pdf.output(f"E:/Python/CS50x/Week 9/project/receipts/{customer_name}_{file_date}.pdf")

    # -----------------------------
    #      PRINT RECEIPT IN CMD
    # -----------------------------
    print("\nYour Receipt:")
    for item in receipt["items"]:
        print(f"{item['name']} - {item['category']} - ${item['price']}")
    print(f"Total: ${receipt['total']}")
    print(f"Date: {receipt['date']}")

    # -----------------------------
    #    MUSIC RECOMMENDATION & PLAY
    # -----------------------------
    if store.cart:
        type_print("\nMusic Recommendation:")
        
        first_category = store.cart[0].category
        music_file = recommend_music_for_category(first_category)
    
        product_names = ", ".join([p.name for p in store.cart])
        print(f"You can listen to a music related to your first purchase. Your purchase: ({product_names})")

        type_print("\nPlaying your recommended music...")
        play_music(music_file)

    # -----------------------------
    #  Clear History Of sales.json
    # -----------------------------
    clear_history = input("Do you want to clear all purchase history? (yes/no) ").lower().strip()
    while clear_history not in ["yes", "no"]:
        print("Just say yes or no.")
        clear_history = input("Do you want to clear all purchase history? (yes/no) ").lower().strip()
    if clear_history == "yes":
        clear_sales_for_customer(customer_name)
    else:
        print("Ok\n")

    type_print("Hope to meet, GoodBye.")



# ==============================
#           RUN PROGRAM
# ==============================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        type_print("\nProgram stopped by user. Goodbye!")
        