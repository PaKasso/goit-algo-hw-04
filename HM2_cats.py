import os

def get_cats_info(path):
    cats_info = []  # Ініціалізуємо порожній список для збереження інформації про котів

    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')  # Розділяємо дані за комами
                if len(data) == 3:  # Перевіряємо, чи є три елементи у рядку
                    cat_id, name, age = data  # Розпаковуємо дані
                    # Додаємо словник з інформацією про кота до списку
                    cats_info.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл не знайдено за шляхом: {path}")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

    return cats_info  # Повертаємо список словників з інформацією про котів

# Приклад використання функції
if __name__ == "__main__":
    # Вкажіть правильний шлях до вашого файлу
    path_to_file = "cats_file.txt"
    # Діагностичне виведення для перевірки шляху
    print(f"Поточна директорія: {os.getcwd()}")
    print(f"Файли в поточній директорії: {os.listdir()}")
    print(f"Шлях до файлу: {path_to_file}")
    
    cats_info = get_cats_info(path_to_file)
    print(cats_info)