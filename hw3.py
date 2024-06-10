'''  Напишіть програму обробки директорії "Хлам", яка копіює файли з заданої директорії (та всіх її піддиректорій) до цільової директорії, сортуючи їх за розширеннями.
 Програма повинна використовувати багатопотоковість для ефективної обробки великих обсягів файлів та піддиректорій.
Програма приймає два аргументи командного рядка:
шлях до директорії з файлами для обробки.
шлях до директорії, де будуть розміщені відсортовані файли. 
Вона має рекурсивно обходити всі піддиректорії джерельної директорії.    
'''   
import os
import shutil
import concurrent.futures

def copy_file(file, source_dir, target_dir):
    # Визначаємо розширення файлу
    extension = os.path.splitext(file)[1].lstrip('.')
    # Створюємо піддиректорію з назвою розширення, якщо вона ще не існує
    os.makedirs(os.path.join(target_dir, extension), exist_ok=True)
    # Копіюємо файл до піддиректорії
    shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir, extension, file))

def process_directory(source_dir, target_dir):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for dirpath, dirnames, filenames in os.walk(source_dir):
            for file in filenames:
                executor.submit(copy_file, file, dirpath, target_dir)
