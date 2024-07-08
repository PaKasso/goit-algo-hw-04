import os

def total_salary(filename):
    total_salary = 0  # Ініціалізуємо змінну для збереження загальної суми зарплат
    num_developers = 0  # Ініціалізуємо змінну для підрахунку кількості розробників

    # Отримуємо шлях до директорії, де знаходиться скрипт
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Отримуємо повний шлях до файлу
    path = os.path.join(script_dir, filename)

    # Діагностичне виведення
    print(f"Шлях до скрипту: {script_dir}")
    print(f"Список файлів у директорії скрипту: {os.listdir(script_dir)}")
    print(f"Повний шлях до файлу: {path}")

    # Перевірка існування файлу
    if not os.path.exists(path):
        print("Файл не знайдено.")
        return None

    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:  # Читаємо кожен рядок файлу
                data = line.strip().split(',')  # Розділяємо дані про розробника та його зарплату
                if len(data) == 2:  # Перевіряємо, чи є два елементи у рядку
                    try:
                        salary = int(data[1])  # Отримуємо зарплату розробника
                        total_salary += salary  # Додаємо зарплату до загальної суми
                        num_developers += 1  # Збільшуємо лічильник розробників
                    except ValueError:
                        print(f"Некоректне значення зарплати у рядку: {line}")
    except Exception as e:
        print(f"Помилка: {e}")
        return None

    if num_developers == 0:
        print("Файл порожній або не містить коректних даних.")
        return None

    average_salary = total_salary / num_developers  # Обчислюємо середню зарплату
    return total_salary, average_salary  # Повертаємо кортеж із загальною сумою та середньою зарплатою

# Приклад використання функції
result = total_salary("salary_file.txt")  # Замініть "salary_file.txt" на ім'я вашого файлу
if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")