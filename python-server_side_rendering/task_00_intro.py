import os

'''Begins here'''

def generate_invitations(template, attendees):
    """
    Генерирует персонализированные приглашения на основе шаблона и списка гостей.
    """

    # 1. Проверка типов входных данных
    if not isinstance(template, str):
        print(f"Error: Invalid input type. Template should be a string, but got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type. Attendees should be a list of dictionaries.")
        return

    # 2. Обработка пустых входных данных
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Обработка каждого участника
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template

        # Список необходимых плейсхолдеров
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:
            # Получаем значение, если оно None или отсутствует — заменяем на "N/A"
            value = attendee.get(key)
            if value is None:
                value = "N/A"

            # Заменяем плейсхолдер {key} на значение
            placeholder = "{" + key + "}"
            processed_template = processed_template.replace(placeholder, str(value))

        # 4. Генерация выходных файлов
        filename = f"output_{index}.txt"

        # Проверка на существование файла (согласно подсказке)
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists. Overwriting...")

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"An error occurred while writing {filename}: {e}")

# Пример использования (для тестирования локально)
if __name__ == "__main__":
    # Тестовый шаблон
    test_template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    # Тестовые данные
    test_attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(test_template, test_attendees)
