import pandas as pd

# Путь к файлу
file_path = "/Users/fakebrain/Downloads/GNRL. Бюджет на 2026 год. (1).xlsx"

# Чтение файла
df = pd.read_excel(file_path)

print("Всего колонок:", len(df.columns))
print("\nНазвание колонок:")
for i, col in enumerate(df.columns):
    print(f"  {i}: '{col}'")
