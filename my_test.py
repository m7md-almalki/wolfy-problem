from fpdf_test import FPDF

size_of_image = 150


pdf = FPDF()
pdf.add_page()
pdf.set_margin(5.0)



pdf.image("ex.png", w=size_of_image, x=((pdf.w-size_of_image)/2))
pdf.ln(h=2.5)

pdf.image("ex.png", w=size_of_image, x=((pdf.w-size_of_image)/2))
pdf.ln(h=2.5)

pdf.image("ex.png", w=size_of_image, x=((pdf.w-size_of_image)/2))
pdf.ln(h=2.5)


pdf.output('final.pdf')