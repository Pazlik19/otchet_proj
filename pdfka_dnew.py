from fpdf import FPDF
from pdfka import year_f
group = '1121 б'
kurs='2'

pdf = FPDF()
pdf.add_page()
# Add font "Полужирный", 'Жирный'
pdf.set_y(25)
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
pdf.set_xy(30,115)
pdf.cell(40,25, 'Место практики ', ln=0, align='L')
pdf.set_font('TNRoman', 'U',size=14)

pdf.cell(20,25, 'Югорский государственный университет                 ', ln=1, align='L')
pdf.set_x(30)
pdf.set_font('TNRoman', size=14)
pdf.cell(30,0, 'Студента', ln=0, align='L')
pdf.set_font('TNRoman', 'U',size=14)
pdf.cell(10,0, kurs, ln=0, align='L')
pdf.set_font('TNRoman', size=14)
pdf.cell(50,0, ' курса    группы ', ln=0, align='L')
pdf.set_font('TNRoman', 'U',size=14)
pdf.cell(40,0, group + '           ', ln=1, align='L')
pdf.cell(0,15,'                                                                                                                          ', ln=1, align='C')

pdf.set_font('TNRoman', size=14)
pdf.set_x(30)
pdf.cell(70,5, 'Руководитель практики от ', ln=0, align='L',border=0)
pdf.set_font('TNRoman','U', size=14)
pdf.cell(40,5, '                         /                                       ', ln=1, align='L')
pdf.set_font('TNRoman', size=14)
pdf.set_xy(30,158)
pdf.cell(150,10, 'предприятия                                         (подпись)        (ФИО, должность)', ln=0, align='L',border=0)


pdf.set_font('TNRoman', size=14)
pdf.set_xy(30,175)
pdf.cell(70,5, 'Руководитель практики  ', ln=0, align='L',border=0)
pdf.set_font('TNRoman','U', size=14)
pdf.cell(40,5, '                         /                                       ', ln=1, align='L')
pdf.set_font('TNRoman', size=14)
pdf.set_xy(30,180)
pdf.cell(150,10, 'от ЮГУ                                                  (подпись)        (ФИО, должность)', ln=0, align='L',border=0)

pdf.set_y (260)

pdf.cell(0,10, 'г. Ханты-Мансийск, '+ year_f, ln=True, align='C')

pdf.add_page()


#Save doc or changes
pdf.output('pdfka_dnew.pdf')