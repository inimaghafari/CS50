from fpdf import FPDF
from fpdf.enums import TextMode

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()

page_width = pdf.w
page_height = pdf.h

# Background color
pdf.set_fill_color(33, 33, 33)
pdf.rect(0, 0, page_width, page_height, style="F")


pdf.set_draw_color(125, 18, 53)
pdf.set_line_width(5)
margin = 1
pdf.rect(margin, margin, 210-2*margin, 297-2*margin)

# Add image into pdf
pdf.image("shirtificate.png", x=10, y=66, w=190)

# CS50 Shirtificate shape
pdf.set_font("Helvetica", "B", 50)
pdf.set_xy(13, 43)
with pdf.local_context(text_mode=TextMode.FILL_STROKE, line_width=1):
    pdf.set_text_color(125, 18, 53)
    pdf.set_draw_color(255, 255, 255)
    pdf.cell(0, 14, "CS50 Shirtificate", align="C")


# Input name & Name shape
name = input("Give me your name: ").strip().lower()
name = name.title()
pdf.set_font("Helvetica", "B", 21)
pdf.set_xy(13, 126)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, f"{name} Took CS50", align="C")



pdf.output("shirtificate.pdf")


