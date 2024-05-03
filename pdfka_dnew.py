from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
# Add font "Полужирный", 'Жирный'
pdf.add_font('TNRoman', '', 'Times_New_Roman.ttf', uni=True)
pdf.add_font('TNRoman', 'B', 'Times_New_Roman_B.ttf', uni=True)
pdf.add_font('TNRoman', 'I', 'Times_New_Roman_I.ttf', uni=True)



#set font  "ПОЛУЖИРНЫЙ"
pdf.set_font('TNRoman', size=14)
pdf.cell(0,0, 'МИНИСТЕРСТВО НАУКИ  И ВЫСШЕГО ОБРАЗОВАНИЯ', ln=True, align='C')
pdf.cell(0,12, 'РОССИЙСКОЙ  ФЕДЕРАЦИИ', ln=True, align='C')
pdf.cell(0,0, 'ЮГОРСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ', ln=True, align='C')
pdf.set_y(70)
pdf.cell(0,18, 'ОТЧЕТ', ln=True, align='C')
pdf.cell(0,0, 'о прохождении обучающимеся', ln=True, align='C')

pdf.cell(0,25, '«Учебная практика»', ln=True, align='C')
pdf.set_xy(50,115)
pdf.cell(40,25, 'Место практики ', ln=0, align='L')
pdf.set_font('TNRoman', 'U',size=14)

pdf.cell(20,25, 'Югорский государственный университет ', ln=0, align='L')

pdf.set_font('TNRoman', size=14)
pdf.cell(0,0, 'Студента', ln=True, align='C')





#Save doc or changes
pdf.output('pdfka_dnew.pdf')