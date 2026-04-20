import pandas as pd

# Путь к файлу
file_path = "/Users/fakebrain/Downloads/GNRL. Бюджет на 2026 год. (1).xlsx"

# Чтение файла
df = pd.read_excel(file_path)

# Группировка по категориям
cat_summary = df.groupby('Категория')['Итог по году'].sum()

# Выявление статей сPayments != 0 (фактические расходы)
df_with_payments = df[df['Payments'] > 0]

print("=" * 60)
print("ПОДРОБНЫЙ АНАЛИЗ БЮДЖЕТА")
print("=" * 60)

print("\n📊 ОБЩИЙ ГОДОВОЙ БЮДЖЕТ:")
print(f"  Итого по году (все статьи): {df['Итог по году'].sum():.2f} ₽")
print(f"  Фактические расходы (Payments > 0): {df_with_payments['Итог по году'].sum():.2f} ₽")
print(f"  Прогнозируемые расходы (Payments = 0): {(df['Итог по году'] - df_with_payments['Итог по году']):.2f} ₽")

print("\n" + "-" * 60)
print("📦 КАТЕГОРИИ И ИТОГИ ПО ГОДУ:")
print("-" * 60)
for cat in cat_summary.sort_values(ascending=False).head(10):
    print(f"  {cat.name:.<20} {cat.values[0]:>12,.0f} ₽")

print("\n" + "-" * 60)
print("⚠️  ФАКТИЧЕСКИЕ РАСХОДЫ ПО КАТЕГОРИЯМ:")
print("-" * 60)
cat_actual = df_with_payments.groupby('Категория')['Итог по году'].sum()
for cat in cat_actual.sort_values(ascending=False).head(10):
    print(f"  {cat.name:.<20} {cat.values[0]:>12,.0f} ₽")

print("\n" + "-" * 60)
print("🔍 ПОИСК НЕОБЪЯСНЕННЫХ РАСХОДОВ ИЛИ ЧРЕЗВЫЧАЙНЫХ ТРАТ:")
print("-" * 60)

# Поиск статей с большим значением
large_spending = df_with_payments[df_with_payments['Итог по году'] > 50000].sort_values('Итог по год', ascending=False)

if len(large_spending) > 0:
    print("\n🔴 Статьи с расходами > 50 000 ₽:")
    for _, row in large_spending.iterrows():
        print(f"  • {row['Категория']}: {row['Статья']}: {row['Итог по году']:,} ₽")

# Поиск статей, где Planning ≠ Payments (разница между планировкой и реальностью)
planning_diff = df_with_payments[(df['Категория'] == 'Продукты') | 
                                 (df['Категория'] == 'Транспорт') | 
                                 (df['Категория'] == 'Жильё') | 
                                 (df['Категория'] == 'Образование') | 
                                 (df['Категория'] == 'Здоровье') | 
                                 (df['Категория'] == 'Развлечения') | 
                                 (df['Категория'] == 'Другое')]

print("\n" + "-" * 60)
print("✅ ЗАВЕРШЕНИЕ АНАЛИЗА")
print("-" * 60)
print("\n📌 РЕКОМЕНДАЦИИ:")
print("  1. Изучите статьи с наибольшими расходами")
print("  2. Проверьте, соответствуют ли фактические расходы плану")
print("  3. Выявите необязательные расходы")
