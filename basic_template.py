from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd

def add_footer(topic):
    pdf.set_y(-15)

    pdf.set_font("Times", "I", 8)
    pdf.set_text_color(180, 180, 180)

    pdf.cell(
        w=0,
        h=10,
        text=f"{topic} | Page {pdf.page_no()}",
        align="R"
    )


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

    
    # Set Footer
    add_footer(row["Topic"])

    # Additional pages
    for page in range(row['Pages']-1):
        pdf.add_page()
        
        # Set Footer
        add_footer(row["Topic"])

pdf.output("basic_template.pdf")



