from fpdf import FPDF

# Переменные
school= 'Инженерная школа цифровых технологий'
year_s = '2023'
year_f = '2024'
year_s+'\\'+year_f
kurs = '2'
Study_form = 'Очная'
group ="1121 б"
date_of_f= '2024'
date_of_s= '2023'
numb_of_order='2-222'
date_of_order='06.04.2024'


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




# Массив строк 
table= (
' Сроки практики по календарному учебному графику: с ' +date_of_s+' по '+date_of_f,
'Номер и дата приказа: №2-222 '+numb_of_order+' от ' + date_of_order,
' Вид практики: учебная',
 'Тип практики: ознакомительная',
 'Количество обучающихся прошедших практику: ____________'

)
# Создаем счетчик для нумирации строк
num=1
# Выводим строки 
for i in table:
    pdf.cell(0,5,str(num) + '. ' + i, ln=True, align='L')
    num+=1




#Create TAble

data = [['First Name', 'Last Name', 'email', 'zip','ghbdtn','fddf','dfd'],
            ['Mike', 'Driscoll', 'mike@somewhere.com', '55555','ghbdtn','fddf','dfd'], 
            ['John', 'Doe', 'jdoe@doe.com', '12345','ghbdtn','fddf','dfd'], 
            ['Nina', 'Ma', 'inane@where.com', '54321','ghbdtn','fddf','dfd'] ]


nezach = [['  ','  ','  '],[' ',' ',' '],[' ',' ',' ']]

def table( data, size, spacing):
    
        col_width = pdf.w / size
        row_height = pdf.font_size
        for row in data:
            for item in row:
                pdf.cell(col_width, row_height*spacing, item , border=1)
            pdf.ln(row_height*spacing)

   

if __name__ == '__main__': table(data,7.5,1)



pdf.cell(0,10, '6. Количество обучающихся не прошедших практику: __ ', ln=True, align='C')



if __name__ == '__main__': table(nezach,3.5,1)



pdf.cell(0,18, '7. Предложения и рекомендации об улучшении организации практик: нет', ln=True, align='C')

pdf.set_x (25)
pdf.cell(0,18, 'Руководитель практики    __________________', ln=0, align='L')
pdf.set_x (165)
pdf.set_font('TNRoman','U', size=14)
pdf.cell(10,18, '        Д.О. Змеев    ', ln=1, align='R')
pdf.set_font('TNRoman', size=14)

pdf.set_xy (85,98)
pdf.cell(10,18, '      (Подпись)	', ln=0, align='C')
pdf.set_x (165)
pdf.cell(10,18, '     (Фамилия  И.О.)	', ln=1, align='R')




pdf.set_x (25)
pdf.cell(0,18, 'Руководитель ОПОП    __________________', ln=0, align='L')
pdf.set_x (165)
pdf.set_font('TNRoman','U', size=14)
pdf.cell(10,18, '    В.А. Самарин    ', ln=1, align='R')
pdf.set_font('TNRoman', size=14)

pdf.set_xy (85,121)
pdf.cell(10,18, '      (Подпись)	', ln=0, align='C')
pdf.set_x (165)
pdf.cell(10,18, '     (Фамилия  И.О.)	', ln=1, align='R')























#Save doc or changes
pdf.output('pdfka_2.pdf')















