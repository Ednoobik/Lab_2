from csv import reader

# кол-во книг с названием больше 30
with open('books.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    flag = 0
    for row in table:
        if len(row[1]) > 30:
            flag+=1
    print(f'Всего {flag} книг, название которых длиннее 30 символов')


# поиск книг по автору от 2018 года
def search(table,search_line):
    flag = 0
    for row in table:
        if string_find(row[3],search_line) != -1:
            for i in range(2018,2026):
                if str(i) in row[6]:
                    flag+=1
                    print(f'{row[3]}: {row[1]}, Год поступления: {i}')

    if flag == 0: print('Ничего не найдено')
    else : print(f'Найдено {flag} записей')



def  string_find(string,search_line):
    lower_case = string.lower()
    return lower_case.find(search_line.lower())


while True:
    search_line = input('Введите запрос: ')
    if search_line in ['0', '']:
        break

    with open('books.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        search(table, search_line)






# Генератор библиографических ссылок
from random import randint

with open('books.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    flag = 0
    output = open('bibliographic_ref.txt', 'w')
    for row in table:
        if row[0] != 'ID':
            if (randint(0,1) == 1) and (flag <20):
                flag+=1
                year = row[6].split('.')
                print(f'{row[3]}. {row[1]} - {year[2].split()[0]}')
                output.write(f'{flag}. {row[3]}. {row[1]} - {year[2].split()[0]}\n')
        
    output.close()


# Перечень тегов
with open('books.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    tags = set()
    for tag in table:
        tags.add(tag[12])
    for tag in tags:
        print(tag)

# Топ 20 книг
with open('books.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    top = []
    book_id =[]
    for i in range(20):
        bestbook = [0,1]
        maxsales = 0
        for row in table:
            if row[0] != 'ID':
                if (row[0] in book_id) == False:
                    if (int(row[8])) >= maxsales:
                        bestbook = row
                        maxsales = int(row[8])
            print(bestbook[1])
        top.append(bestbook)
        book_id.append(bestbook[0])

