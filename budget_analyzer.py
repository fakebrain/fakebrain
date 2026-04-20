import pandas as pd
import sys

# Путь к файлу
file_path = "/Users/fakebrain/Downloads/GNRL. Бюджет на 2026 год. (1).xlsx"

# Чтение файла
df = pd.read_excel(file_path)

print("=" * 60)
print("АНАЛИЗ ГОДОВОГО ЛИЧНОГО БЮДЖЕТА")
print("=" * 60)
print(f"\nФайл: {file_path}")
print(f"Строк данных: {len(df)}")
print(f"Колонн: {len(df.columns)}")
print(f"\nКолонны:")
for col in df.columns:
    print(f"  - {col}")

print("\n" + "=" * 60)
print("ДАННЫЕ ЗАГРУЖЕНЫ")
print("=" * 60)
