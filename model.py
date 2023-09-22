import datetime
import json
import os


def add_to_note():
    name = input("Название заметки: ")
    note = input("Заметка: ")
    note_date = datetime.date.today()
    note_id = 0
    json_data = [{
        "name": name,
        "note": note,
        "note_date": note_date.strftime('%D:%Y:%H:%M'),
        "note_id": note_id + 1,
    }]

    if os.path.exists("db.json"):
        data = json.load(open("db.json"))

        json_data[0]["note_id"] = len(data)+1
        # data.update(json_data)
        data.append(json_data)
        with open("db.json", "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    else:
        with open('db.json', 'w') as file:
            file.write(json.dumps(json_data, indent=2, ensure_ascii=False))


def change_to_note():
    note_id = int(input("номер заметки: "))
    data = json.load(open("db.json"))
    for i in range(len(data)):
        if i == note_id-1:
            json_data = data[i]
            data.remove(data[i])
            print(json_data)
            name = input("Название заметки: ")
            note = input("Заметка: ")
            note_date = datetime.date.today()
            note_id = i+1
            json_data = [{
                "name": name,
                "note": note,
                "note_date": note_date.strftime('%D:%Y:%H:%M'),
                "note_id": note_id,
            }]
            data.append(json_data)
            with open("db.json", "w") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)


def print_the_note():

    for i in json.load(open("db.json")):
        print(i)
def del_the_note():
    note_id = int(input("номер заметки для удаления: "))
    data = json.load(open("db.json"))
    for i in range(len(data)):
        if i == note_id - 1:
            data.remove(data[i])
            with open("db.json", "w") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

# print_the_note()
# change_to_note()
# add_to_note()