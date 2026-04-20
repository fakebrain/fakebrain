import pandas as pd

# Путь к файлу
file_path = "/Users/fakebrain/Downloads/GNRL. Бюджет на 2026 год. (1).xlsx"

# Чтение файла
df = pd.read_excel(file_path)

print("=" * 60)
print("🔬 ПОДРОБНЫЙ АНАЛИЗ ГОДОВОГО ЛИЧНОГО БЮДЖЕТА")
print("=" * 60)

print(f"\n📁 Файл: {file_path}")
print(f"📊 Строк данных: {len(df)}")
print(f"📐 Колонн: {len(df.columns)}")

print("\n" + "=" * 60)
print("📈 ОБЩИЙ ОБЗОР:")
print("=" * 60)

total_budget = df['Итог по году'].sum()
print(f"💰 ОБЩИЙ ГОДОВОЙ БЮДЖЕТ: {total_budget:,.0f} ₽")

df_with_payments = df[df['Payments'] > 0]
actual_spending = df_with_payments['Итог по году'].sum()
print(f"💸 ФАКТИЧЕСКИЕ РАСХОДЫ: {actual_spending:,.0f} ₽")

print("\n" + "=" * 60)
print("📦 РАСХОДЫ ПО КАТЕГОРИЯМ:")
print("=" * 60)

cat_summary = df.groupby('Категория')['Итог по году'].sum().sort_values(ascending=False)

print(f"\n{'Категория':.<30} {'Итого (год)':>15}")
print("-" * 50)

for cat, amount in cat_summary.items():
    print(f"{str(cat):.<30} {amount:,.0f}")

print("\n" + "=" * 60)
print("⚠️  ЗАМЕТКИ ПО КАТЕГОРИЯМ:")
print("=" * 60)

# Проверка на потенциально избыточные расходы
food = cat_summary.get('Продукты', 0)
print(f"\n🛒 ПРОДУКТЫ: {food:,.0f} ₽")
print("   → Средне по Москве: 35-45 тыс. в месяц")
print("   → Ваш бюджет: {:.0f} ₽/мес".format(food / 12))
if food / 12 > 45000:
    print("   ⚠️  ВЫСОКИЕ РАСХОДЫ - проверьте состав корзины")
elif food / 12 < 35000:
    print("   ✅ Экономично")

health = cat_summary.get('Здоровье', 0)
print(f"\n🏥 ЗДОРОВЬЕ: {health:,.0f} ₽")
print("   → Медстраховка, лекарства, процедуры")

housing = cat_summary.get('Жильё', 0)
print(f"\n🏠 ЖИЛЬЁ: {housing:,.0f} ₽")
print("   → Ипотека/аренда, коммуналка, ремонт")

education = cat_summary.get('Образование', 0)
print(f"\n🎓 ОБРАЗОВАНИЕ: {education:,.0f} ₽")
print("   → Курсы, обучение, книги")

hobbies = cat_summary.get('Другое', 0)
print(f"\n🎉 ДРУГОЕ (Хобби/Развлечения): {hobbies:,.0f} ₽")
print("   → Мотоциклы, сноуборд, походы")

print("\n" + "=" * 60)
print("🔍 ПОИСК РАСХОДОВ > 100 000 ₽ ЗА ГОД:")
print("=" * 60)

large_expenses = df[df['Итог по году'] > 100000].sort_values('Итог по году', ascending=False)

if len(large_expenses) > 0:
    for _, row in large_expenses.iterrows():
        print(f"\n🔴 Статья: {row['Статья']}")
        print(f"   Категория: {row['Категория']}")
        print(f"   Сумма: {row['Итог по году']:,} ₽")
        print(f"   Payments: {row['Payments']}")
else:
    print("\n✅ Нет крупных (>100 тыс. ₽) расходов за год")

print("\n" + "=" * 60)
print("📌 ВЫВОДЫ И РЕКОМЕНДАЦИИ:")
print("=" * 60)
print("\n1. ПРОАНАЛИЗИРУЙТЕ КАЖДУЮ КАТЕГОРИЮ:")
print("   - Соответствует ли бюджет реальной нагрузке?")
print("   - Нет ли необъяснимых расходов?")

print("\n2. ПРОВЕРЬТЕ 'ДРУГОЕ':")
print("   - Эта категория часто содержит скрытые расходы")
print("   - Рассмотрите возможность консолидации")

print("\n3. МЕСЯЧНАЯ СРЕДНЯЯ:")
monthly_avg = total_budget / 12
print(f"   → {monthly_avg:,.0f} ₽/мес на покрытие всех расходов")

print("\n4. СРАВНИТЕ С ДОХОДАМИ:")
print("   → Доходы / Расходы = коэффициент накопления")
print("   → Стремитесь к коэффициенту ≥ 0.5")

print("\n5. СЛЕДУЮЩИЕ ШАГИ:")
print("   • Детализируйте необъяснимые расходы")
print("   • Консолидируйте мелкие категории")
print("   • Пересмотрите бюджет раз в квартал")

print("\n✅ ОТЧЁТ ПОДГОТОВЛЕН")
print("=" * 60)
