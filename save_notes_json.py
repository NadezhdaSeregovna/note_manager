"""Выбор формата файла"""
import json
from xml.etree.ElementTree import indent


def save_notes_json(notes, filename):
    file = open('filename.json', 'x', encoding='utf-8')
    with open('filename.json', 'w', encoding='utf-8'):
        json.dump(notes, file, indent=4, ensure_ascii=False)

notes = [
    {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты",
        "status": "новая",
        "created_date": "27-11-2024",
        "issue_date": "30-11-2024"
    }
]

save_notes_json(notes, filename='filename.json')