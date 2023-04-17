import json
import datetime

def read_notes():
    try:
        with open('notes.json', 'r', encoding='utf8') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open('notes.json', 'w', encoding='utf8') as f:
        json.dump(notes, f, indent=4)

def add_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {'id': len(notes) + 1, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(note)
    save_notes(notes)
    print('Заметка добавлена.')

def edit_note():
    note_id = int(input('Введите ID заметки для редактирования: '))
    for note in notes:
        if note['id'] == note_id:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            note['title'] = title
            note['body'] = body
            note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print('Заметка отредактирована.')
            break
    else:
        print('Заметка с таким ID не найдена.')

def delete_note():
    note_id = int(input('Введите ID заметки для удаления: '))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print('Заметка удалена.')
            break
    else:
        print('Заметка с таким ID не найдена.')

def print_notes():
    for note in notes:
        print(f'ID: {note["id"]}, Заголовок: {note["title"]}, Текст: {note["body"]}, Время создания/изменения: {note["timestamp"]}')

notes = read_notes()

print("""
    ------------------------------- \n
    1 - add \n 
    2 - edit\n  
    3 - delete\n 
    4 - list\n 
    5 - exit\n 
    ------------------------------- \n 
    """)
while True:
    command = input('Введите команду: ')
    if command == '1':
        add_note()
    elif command == '2':
        edit_note()
    elif command == '3':
        delete_note()
    elif command == '4':
        print_notes()
    elif command == '5':
        print("До свидания!")
        break
    else:
        print('Неизвестная команда.')
