from fpdf import FPDF

def generate_pdf(projects_data, output_path):
    pdf = FPDF()
    
    # Add Unicode fonts
    pdf.add_font('DejaVu', fname='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVuMono', fname='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', uni=True)

    for project in projects_data:
        pdf.add_page()
        pdf.set_font('DejaVu',size=18)
        pdf.cell(0,10,txt=project['project_name'],ln=True)
        pdf.ln(10)
        pdf.set_font('DejaVu',size=13)
        pdf.cell(0,5,txt='Table of contents: ',ln=True)
        pdf.ln(5)
        for file in project['files']:
            pdf.set_font('DejaVu',size=11)
            pdf.multi_cell(0,5,txt=file['path'],ln =True)
            pdf.ln(10)
        for file_info in project['files']:
            pdf.add_page()
    
            pdf.set_font('DejaVu', size=14)
            pdf.multi_cell(0, 10, txt=file_info['path'])
    
            pdf.ln(5)
    
            pdf.set_font('DejaVuMono', size=9)
            pdf.multi_cell(0, 5, txt=file_info['content'])
    
    pdf.output(output_path)
