import sqlite3

db = sqlite3.connect('db_imeninniki')

#Создаем курсор для взаимодействия с базой данных
c = db.cursor()

'''
#Создаем таблицу и подверждаем внесённые изменения в бд

c.execute("""CREATE TABLE students(
    second_name text,
    name text,
    third_name text,
    birth_day integer,
    birth_month integer,
    birth_year integer,
    grade_number integer,
    grade_letter text
)""")

#Добавляем значения в таблицу

c.execute("""INSERT INTO students VALUES 
    ('Петров', 'Артем', 'Владимирович', 11, 06, 2006, 10, 'Г'),
('Кузнецова', 'Екатерина', 'Игоревна', 30, 09, 2005, 11, 'Б'),
('Соколов', 'Алексей', 'Александрович', 02, 04, 2007, 9, 'А'),
('Михайлова', 'Ольга', 'Сергеевна', 14, 11, 2006, 10, 'В'),
('Лебедев', 'Максим', 'Дмитриевич', 08, 02, 2005, 11, 'Г'),
('Новикова', 'Анастасия', 'Ильинична', 20, 07, 2007, 9, 'Б'),
('Козлов', 'Игорь', 'Валерьевич', 25, 12, 2006, 10, 'А'),
('Сергеев', 'Даниил', 'Артемович', 03, 09, 2005, 11, 'В'),
('Павлова', 'Мария', 'Владимировна', 16, 05, 2007, 9, 'Г'),
('Васнецов', 'Артур', 'Станиславович', 29, 10, 2006, 10, 'Б'),
('Григорьева', 'Елена', 'Игоревна', 12, 03, 2005, 11, 'А'),
('Лебединский', 'Александр', 'Павлович', 25, 08, 2007, 9, 'В'),
('Смирнов', 'Дмитрий', 'Сергеевич', 07, 01, 2006, 10, 'Г'),
('Кузнецов', 'Артем', 'Валентинович', 19, 06, 2005, 11, 'Б'),
('Иванова', 'Анна', 'Дмитриевна', 01, 11, 2007, 9, 'А'),
('Петров', 'Станислав', 'Аркадьевич', 13, 04, 2006, 10, 'В'),
('Новиков', 'Даниил', 'Игоревич', 26, 09, 2005, 11, 'Г'),
('Соколова', 'Екатерина', 'Алексеевна', 08, 02, 2007, 9, 'Б'),
('Михайлов', 'Максим', 'Артемович', 21, 07, 2006, 10, 'А'),
('Лебедева', 'Ольга', 'Ильинична', 03, 12, 2005, 11, 'В'),
('Григорьев', 'Владимир', 'Валентинович', 15, 05, 2007, 9, 'Г'),
('Козлова', 'Анастасия', 'Станиславовна', 28, 10, 2006, 10, 'Б'),
('Сергеева', 'Мария', 'Викторовна', 10, 03, 2005, 11, 'А'),
('Павлов', 'Дмитрий', 'Александрович', 23, 08, 2007, 9, 'В'),
('Васнецова', 'Ирина', 'Сергеевна', 04, 01, 2006, 10, 'Г'),
('Лебединская', 'Алина', 'Валентиновна', 17, 06, 2005, 11, 'Б'),
('Смирнов', 'Илья', 'Игоревич', 29, 11, 2007, 9, 'А'),
('Кузнецов', 'Михаил', 'Артемович', 11, 04, 2006, 10, 'В'),
('Иванов', 'Артур', 'Дмитриевич', 24, 09, 2005, 11, 'Г'),
('Новикова', 'Дарья', 'Игоревна', 06, 02, 2007, 9, 'Б'),
('Петрова', 'Ксения', 'Валентиновна', 19, 07, 2006, 10, 'А'),
('Козлова', 'Вера', 'Александровна', 01, 12, 2005, 11, 'В'),
('Соколов', 'Денис', 'Станиславович', 14, 05, 2007, 9, 'Г'),
('Михайлов', 'Артем', 'Игоревич', 27, 10, 2006, 10, 'Б'),
('Лебедева', 'Анна', 'Аркадьевна', 09, 03, 2005, 11, 'А'),
('Григорьев', 'Дмитрий', 'Викторович', 22, 08, 2007, 9, 'В'),
('Васнецов', 'Максим', 'Сергеевич', 05, 01, 2006, 10, 'Г'),
('Смирнов', 'Игорь', 'Александрович', 18, 06, 2005, 11, 'Б'),
('Кузнецова', 'Анастасия', 'Дмитриевна', 30, 11, 2007, 9, 'А'),
('Иванов', 'Сергей', 'Артемович', 12, 04, 2006, 10, 'В'),
('Павлова', 'Дарья', 'Игоревна', 25, 09, 2005, 11, 'Г'),
('Соколов', 'Александр', 'Денисович', 07, 02, 2007, 9, 'Б'),
('Новикова', 'Мария', 'Анатольевна', 20, 07, 2006, 10, 'А'),
('Козлов', 'Михаил', 'Владимирович', 02, 12, 2005, 11, 'В'),
('Лебедев', 'Денис', 'Валентинович', 15, 05, 2007, 9, 'Г'),
('Григорьева', 'Екатерина', 'Артемовна', 28, 10, 2006, 10, 'Б'),
('Смирнов', 'Максим', 'Игоревич', 10, 03, 2005, 11, 'А'),
('Кузнецов', 'Артем', 'Валерьевич', 23, 08, 2007, 9, 'В'),
('Иванова', 'Анна', 'Алексеевна', 04, 01, 2006, 10, 'Г'),
('Петров', 'Дмитрий', 'Игоревич', 17, 06, 2005, 11, 'Б'),
('Новиков', 'Денис', 'Аркадьевич', 29, 11, 2007, 9, 'А'),
('Соколов', 'Артем', 'Валентинович', 11, 04, 2006, 10, 'В'),
('Михайлова', 'Мария', 'Сергеевна', 24, 09, 2005, 11, 'Г'),
('Лебедев', 'Артур', 'Станиславович', 06, 02, 2007, 9, 'Б'),
('Григорьев', 'Илья', 'Александрович', 19, 07, 2006, 10, 'А'),
('Васнецов', 'Игорь', 'Артемович', 01, 12, 2005, 11, 'В'),
('Смирнова', 'Ксения', 'Валентиновна', 14, 05, 2007, 9, 'Г'),
('Павлов', 'Денис', 'Станиславович', 09, 11, 2006, 10, 'Г'),
('Козлова', 'Анна', 'Валерьевна', 22, 04, 2005, 11, 'Б'),
('Сергеев', 'Михаил', 'Артемович', 05, 09, 2007, 9, 'А')
""")
'''
#Пропишем функцию сортировки вставками
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array

#Выбираем значения из базы данных и сортируем их (в данном случае по 1 заданию)
#Плюс оформляем форматный вывод в таблицу через цикл for, как и везде в коде ниже

c.execute("SELECT second_name, grade_number, grade_letter FROM students")
new_list1=insertion_sort(c.fetchall())
for i in new_list1:
    print(i)

#Выбираем значения из базы данных и сортируем их (в данном случае по 2 заданию)

birth_year_input = int(input('Введите год рождения студента в формате 0000: '))
c.execute('SELECT birth_month, birth_day, second_name FROM students WHERE birth_year=?', (birth_year_input,))
new_list2=insertion_sort(c.fetchall())
for i in new_list2:
    print(i)

#Выбираем значения из базы данных и сортируем их (в данном случае по 3 заданию)
grade_number_input = str(input("Введите букву класса студента в формате 'А': "))
c.execute("SELECT birth_month, birth_day, second_name FROM students WHERE grade_letter = ?", (grade_number_input,))
new_list3=insertion_sort(c.fetchall())
for i in new_list3:
    print(i)

db.commit()

db.close()