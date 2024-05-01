from fpdf import FPDF

# Переменные
school= 'Инженерная школа цифровых технологий'
year_s = '2023'
year_f = '2024'
year_s+'\\'+year_f
kurs = '2'
Study_form = 'Очная'
group ="1121 б"

pdf = FPDF()
pdf.add_page()
# Add font "Полужирный", 'Жирный'
pdf.add_font('TNRoman', '', 'Times_New_Roman.ttf', uni=True)
pdf.add_font('TNRoman', 'B', 'Times_New_Roman_B.ttf', uni=True)
pdf.add_font('TNRoman', 'I', 'Times_New_Roman_I.ttf', uni=True)


# Create document

#set font  "ПОЛУЖИРНЫЙ"
pdf.set_font('TNRoman', size=14)
pdf.cell(0,0, 'МИНИСТЕРСТВО НАУКИ  И ВЫСШЕГО ОБРАЗОВАНИЯ', ln=True, align='C')
pdf.cell(0,12, 'РОССИЙСКОЙ  ФЕДЕРАЦИИ', ln=True, align='C')
pdf.cell(0,0, 'ЮГОРСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ', ln=True, align='C')


#set font  "ЖИРНЫЙ"
pdf.set_font('TNRoman','B', size=14)
pdf.cell(0,20, school, ln=True, align='C')


pdf.cell(0,18, 'ОТЧЕТ', ln=True, align='C')
pdf.cell(0,0, 'о прохождении обучающимеся', ln=True, align='C')



#set font  "ЖИРНЫЙ-ПОДЧЕРКНУТЫЙ"
pdf.set_font('TNRoman','UB', size=14)
pdf.cell(0,20, 'учебной', ln=True, align='C')

# #Смещение след элемента на 72 мм от начал листа 
# pdf.set_y (72)

#set font  "Курсив"
pdf.set_font('TNRoman','I', size=12)
pdf.cell(0,-10, '(вид практики)', ln=True, align='C')


#set font  "ЖИРНЫЙ-ПОДЧЕРКНУТЫЙ"
pdf.set_font('TNRoman','UB', size=14)
pdf.cell(0,28, '(ознакомительная) практика', ln=True, align='C')

#Смещение след элемента на 89 мм от начал листа 
pdf.set_y (86)

#set font  "Курсив"
pdf.set_font('TNRoman','I', size=12)
pdf.cell(0,5, '(тип практики)', ln=True, align='C')


#set font  "ЖИРНЫЙ-ПОДЧЕРКНУТЫЙ"
pdf.set_font('TNRoman','UB', size=14)
pdf.cell(0,15, 'за '+ year_s+'\\'+year_f + ' учебный год', ln=True, align='C')

#set font  "ЖИРНЫЙ-ПОДЧЕРКНУТЫЙ"
pdf.set_font('TNRoman','UB', size=14)
pdf.cell(0,18, '09.03.01 Информатика и вычислительная техника', ln=True, align='C')


#Смещение след элемента на 89 мм от начал листа 
# pdf.set_y (122)

#set font  "Курсив"
pdf.set_font('TNRoman','I', size=12)
pdf.cell(0,-5, '(код и наименование специальности)', ln=True, align='C')


#set font  "ЖИРНЫЙ"
pdf.set_font('TNRoman','B', size=14)
pdf.cell(0,18,  Study_form + ' форма обучения', ln=True, align='C')


#set font  "ПОЛУЖИРНЫЙ"
pdf.set_font('TNRoman', size=12)
pdf.cell(0,10, 'Курс '+ kurs, ln=True, align='L')
pdf.cell(0,10, 'Группа'+ group, ln=True, align='L')


pdf.set_y (260)

pdf.cell(0,10, 'г. Ханты-Мансийск, '+ year_f, ln=True, align='C')




pdf.add_page()

















#Save doc or changes
pdf.output('pdfka_2.pdf')