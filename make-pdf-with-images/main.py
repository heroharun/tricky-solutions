from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from PIL import Image
import os
import re

def makePDFwithImages(input, output):
    # create a new PDF with Reportlab
    pdf = canvas.Canvas(output, pagesize=letter)
    width, height = letter

    # sort the images by name
    resim_dosyalari = sorted([dosya for dosya in os.listdir(input) if dosya.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))],
                             key=lambda x: int(re.search(r'\d+', x).group()))

    for sayfa_numarasi, resim_dosyasi in enumerate(resim_dosyalari, start=1):
        # add image to canvas
        resim_yolu = os.path.join(input, resim_dosyasi)
        pdf.drawInlineImage(resim_yolu, 0, 0, width, height)

        # add page number
        pdf.setFont("Helvetica", 12)
        pdf.drawString(10, 10, f"Sayfa {sayfa_numarasi}")

        # add new page
        pdf.showPage()

    # save PDF
    pdf.save()

if __name__ == "__main__":
    input = "1.pdf"
    output = "1a.pdf"

    makePDFwithImages(input, output)
    print(f"{output} oluştu)")

