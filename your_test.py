from fpdf_test import FPDF 

# i have imported fpdf_test | and it is the correct FPDF version that i use , but i have changed the name of it , to not import an old version accidentally.


def investment_summary(pdf, text, bullet_indent=15):
    pdf.set_font("Arial", size=8)

    for point in text.splitlines():
        if point.startswith("-"):
            pdf.set_x(bullet_indent)
        pdf.multi_cell(0, 5, point)


def add_analytics(pdf, image_paths):
    size_of_image = 150
    for image in image_paths:
        pdf.image(image, w=size_of_image, x=((pdf.w-size_of_image)/2))
        pdf.ln(h=2.5)


def create_report(county_and_state, llm_text, analytics_location_path=None):
    
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_text_color(r=50,g=108,b=175)
    pdf.set_font('Arial', 'B', 18)
    
    
    pdf.cell(w=0, h=10, txt="Verus-AI: " + county_and_state, ln=1,align='C')
    
    
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=10, txt="Investment Summary", ln=1,align='L')
    
    #investment_summary(pdf, llm_text)

    pdf.set_text_color(r=50,g=108,b=175)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=10, txt="Analytics", ln=1,align='L')
    add_analytics(pdf, analytics_location_path)

    pdf.output(f'./example1.pdf', 'F')




create_report("anything", None , ["ex.png","ex.png","ex.png","ex.png","ex.png","ex.png","ex.png","ex.png"])
