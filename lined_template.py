from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    # Add Page
    pdf.add_page()

    # Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,
              h=10, 
              text=row['Topic'], 
              align="L", 
              new_x=XPos.LMARGIN, 
              new_y=YPos.NEXT
              )
    
    pdf.line(x1=10, y1=20, x2=200, y2=20)

    line_y = pdf.get_y() + 10
    footer_y = pdf.h - 15

    while line_y < footer_y:
        pdf.line(10, line_y, 200, line_y)
        line_y +=10

    
    # Set Footer
    pdf.set_y(-15)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=8, text=row['Topic'], align="R")

    # Additional pages
    for page in range(row['Pages']-1):
        pdf.add_page()
        
        line_y = pdf.get_y() + 10
        footer_y = pdf.h - 15

        while line_y < footer_y:
            pdf.line(10, line_y, 200, line_y)
            line_y +=10

        # Set Footer
        pdf.set_y(-15)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=10, text=row['Topic'], align="R")

pdf.output("lined_output.pdf")



