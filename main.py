import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="portrait", unit="mm", format="A4")
    
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_no = filename.split("-")[0]
   
    pdf.set_font(family="Times", style="B", size=16) 
    pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_no}", ln=1)

    pdf.output(f"pdfs/{filename}.pdf")