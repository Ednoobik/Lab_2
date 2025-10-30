from csv import reader

def search(table,search_line):
    flag = 0
    output = open('result.txt', 'w')
    for row in table:
        if string_find(row[2],search_line) != -1:
            flag+=1
            print(row[2])
            output.write(f'{row[0]}. {row[2]} - {row[18]}\n')

    if flag == 0: print('Ничего не найдено')
    else : print(f'Найдено {flag} записей')

    output.close()



def  string_find(string,search_line):
    lower_case = string.lower()
    return lower_case.find(search_line.lower())

while True:
    search_line = input('Введите запрос: ')
    if search_line in ['0', '']:
        break


    try:
        with open('civic.csv', 'r') as csvfile:
            table = reader(csvfile, delimiter=';')
            search(table, search_line)
    except FileNotFoundError:
        print('Файл не найден')
