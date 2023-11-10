#
# Регулярные выражения (Regular Expressions) - это мощный инструмент для работы с текстом, который позволяет искать,
# извлекать и изменять определенные шаблоны символов. В Python регулярные выражения реализованы в модуле re.

# 1. Импортирование модуля re:

import re

# 2. Поиск совпадений:

pattern = r"apple"
text = "I have an apple"
match = re.search(pattern, text)
if match:
    print("Найдено совпадение")
else:
    print("Совпадение не найдено")

# 3. Извлечение совпадений:

pattern = r"\d+"  # Извлечение чисел
text = "There are 123 apples and 456 oranges"
matches = re.findall(pattern, text)
for match in matches:
    print(match)

# 4. Замена совпадений:

pattern = r"apple"
text = "I have an apple"
new_text = re.sub(pattern, "orange", text)
print(new_text)

# 5. Использование специальных символов:

pattern = r"\b[A-Za-z]+\b"  # Извлечение слов
text = "Hello, world!"
matches = re.findall(pattern, text)
for match in matches:
    print(match)

# 6. Использование квантификаторов:

pattern = r"\d{3}-\d{3}-\d{4}"  # Извлечение номеров телефонов в формате XXX-XXX-XXXX
text = "My phone number is 123-456-7890"
matches = re.findall(pattern, text)
for match in matches:
    print(match)

# 7. Использование группировки:

pattern = r"(\w+), (\w+)"
text = "Bond, James"
match = re.search(pattern, text)
if match:
    print(match.group(1))  # Выводит "Bond"
    print(match.group(2))  # Выводит "James"

