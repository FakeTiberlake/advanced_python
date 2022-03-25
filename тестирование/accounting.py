
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def call_name(documents):
    '''
   Функция, которая выводит имя пользователя по номеру документа
    '''
    doc_number = input('Введите номер документа: ')
    for doc_info in documents:
        if doc_info['number'] == doc_number:
            return doc_info['name']
    else:
        return f'Несуществующий документ'


# print(call_name(documents))


def call_rack(directories):
    '''
  Функция, которая сообщает на какой полке находится запрашиваемый документ
    '''
    doc_number = input('Введите номер документа: ')
    for key, value in directories.items():
        if doc_number in value:
            return key
    else:
        return f'Несуществующий документ'


# print(call_rack(directories))


def get_all_docs(documents):
    '''
  Функция, которая покажет список всех документов
    '''
    for all_docs in documents:
        docs = ' '.join(list(all_docs.values()))
        print(docs)


# print(get_all_docs(documents))


def add_new_doc(documents, directories):
    '''
  Функция, которая по персональным данным и номеру полки добавит новый документ в каталог и в перечень полок.
    '''
    doc_type = input('Введите тип документа, который нужно добавить: ')
    doc_number = input('Введите номер документа, который нужно добавить: ')
    user_name = input('Введите фамилию имя отчество владельца: ')
    rack_number = input('Введите номер полки, на которой будет храниться документ: ')

    new_docs = {'type': doc_type, 'number': doc_number, 'name': user_name}
    documents.append(new_docs)
    print(documents)
    print('Персональные данные успешно добавлены')

    for key, value in directories.items():
        if rack_number in directories:
            key == rack_number and value.append(doc_number)
            print(key, value)
        else:
            print(f'Полки с таким номером не существует')


# print(add_new_doc(documents, directories))


def delete_doc(documents, directories):
    '''
  Функция, которая удаляет из каталога и перечня полок запрошенный документ.
    '''
    del_doc = input('Введите номер документа, который нужно удалить: ')
    origin_len = len(documents)

    for i, rem_doc in enumerate(documents):
        if rem_doc['number'] == del_doc:
            documents.pop(i)
            # print(documents)

    if origin_len == len(documents):
        return f'Документа с номером {del_doc} не существует'

    for key, value in directories.items():
        if del_doc in value:
            value.remove(del_doc)
            # print(directories)
            return f'Документ {del_doc} успешно удалён'


# print(delete_doc(documents, directories))


def move_doc(directories):
    '''
  Функция, которая перемещает необходимый документ на нужную полку.
    '''
    doc_number = input('Введите номер документа, который нужно переместить: ')
    rack_number = input('Введите номер полки, на которую необходимо переместить указанный документ: ')

    doc_exist = False

    if rack_number not in directories:
        print('Указанная полка не существует')
        return

    for doc in directories.values():
        if doc_number in doc:
            doc_exist = True
            directories[rack_number].append(doc_number)
            doc.remove(doc_number)
            print(directories)
            print(f'Документ успешно перемещён на {rack_number} полку')
            return
    else:
        print('Указанный документ не существует')


# print(move_doc(directories))


def add_rack(directories):
    '''
  Функция, которая добавляет новую полку в перечень.
    '''
    rack_number = input('Введите номер новой полки, которую нужно добавить: ')

    if rack_number in directories:
        print('Полка с таким номером уже существует')
    else:
        directories[rack_number] = []
        print(f'Полка с номером {rack_number} успешно добавлена')


# print (add_rack(directories))

def start_secretary_program():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            print(call_name(documents))
        elif user_input == 's':
            print(call_rack(directories))
        elif user_input == 'l':
            get_all_docs(documents)
        elif user_input == 'a':
            add_new_doc(documents, directories)
        elif user_input == 'd':
            print(delete_doc(documents, directories))
        elif user_input == 'm':
            move_doc(directories)
        elif user_input == 'as':
            print(add_rack(directories))
        elif user_input == 'q':
            print('Выход из программы')
            break
        else:
            print('Неверная команда')

if __name__ == '__main__':
    start_secretary_program()
