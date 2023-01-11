from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        # Logo
        self.image('templates/images/sm-logo_4x1.jpg', 10, 8, 10)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Events', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
pdf.cell(30, 10, 'event name', 0, 0, 'L')
pdf.cell(30, 10, 'event date', 0, 1, 'L')


def generatePDF(data):
    for i in data:
        pdf.cell(30, 10, i['event_name'], 0, 0, 'L')
        pdf.cell(30, 10, i['event_date'].strftime("%m/%d/%Y"), 0, 1, 'L')
    pdf.output('events.pdf', 'F')
