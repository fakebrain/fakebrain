import pandas as pd

# Путь к файлу
file_path = "/Users/fakebrain/Downloads/GNRL. Бюджет на 2026 год. (1).xlsx"

# Чтение файла
df = pd.read_excel(file_path)

# Фильтрация только по категории "Расход"
expense_df = df[df['Категория'] == 'Расход'].copy()

print("=" * 60)
print("🔍 ГЛУБОКИЙ АНАЛИЗ КАТЕГОРИИ 'РАСХОД'")
print("=" * 60)

if len(expense_df) > 0:
    print(f"\n📊 Количество строк в категории 'Расход': {len(expense_df)}")
    total_expense = expense_df['Итог по году'].sum()
    print(f"💰 Общая сумма: {total_expense:,.0f} ₽")
    
    print("\n" + "-" * 60)
    print("📄 ДЕТАЛЬНАЯ ТАБЛИЦА:")
    print("-" * 60)
    
    # Показываем все строки (их всего 1)
    for idx, row in expense_df.iterrows():
        print(f"\n📄 Статья #{idx + 1}")
        print(f"  Название: {row['Статья']}")
        budget = row['Итог по году']
        payments = row['Payments']
        print(f"  Бюджет: {budget:,.0f} ₽")
        print(f"  Факт: {payments:,.2f} ₽")
        
        # Проверка на аномалии
        if budget > 0:
            payment_ratio = payments / budget if budget > 0 else 0
            print(f"  Реализация: {payment_ratio*100:.1f}%")
            if payment_ratio < 0.5:
                print(f"  ⚠️  ВНИМАНИЕ: Реализованность только {payment_ratio*100:.1f}%")
            elif payment_ratio > 1.0:
                print(f"  🔴 ПРЕВЫШЕНИЕ БЮДЖЕТА на {(payments - budget):,.0f} ₽")
    
    # Поиск статей без названия (NaN)
    print("\n" + "-" * 60)
    print("🔍 ПОИСК СТАТЕЙ БЕЗ НАЗВАНИЯ:")
    print("-" * 60)
    
    nan_articles = expense_df[expense_df['Статья'].isna()]
    if len(nan_articles) > 0:
        print(f"\n🔴 Найдено {len(nan_articles)} строк без названия")
        print(f"💰 Сумма необъяснимых расходов: {nan_articles['Итог по году'].sum():,.0f} ₽")
        print("\n📌 Это требует немедленного разбора!")
        
        # Группировка по месяцам для этих строк
        print("\n💰 Распределение по месяцам:")
        month_cols = ['Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        for col in month_cols:
            if col in nan_articles.columns:
                print(f"  {col}: {nan_articles[col].fillna(0).sum():,.0f} ₽")
    else:
        print("\n✅ Все статьи имеют названия")
    
    # Поиск статей с очень большими суммами
    print("\n" + "-" * 60)
    print("🔴 СТАТЬИ С БЮДЖЕТОМ > 50 000 ₽:")
    print("-" * 60)
    
    large_articles = expense_df[expense_df['Итог по году'] > 50000].sort_values('Итог по году', ascending=False)
    
    if len(large_articles) > 0:
        for idx, row in large_articles.iterrows():
            budget = row['Итог по году']
            payments = row['Payments']
            print(f"\n📄 Статья: {row['Статья']}")
            print(f"  Бюджет: {budget:,.0f} ₽")
            print(f"  Факт: {payments:,.2f} ₽")
            if budget > 0:
                ratio = payments / budget
                print(f"  Реализация: {ratio*100:.1f}%")
    else:
        print("\n✅ Нет статей с бюджетом > 50 000 ₽")
    
    # Поиск повторяющихся паттернов
    print("\n" + "-" * 60)
    print("🔍 ПОИСК ПОВТОРЯЮЩИХСЯ СТАТЕЙ:")
    print("-" * 60)
    
    # Уникальные статьи
    unique_articles = expense_df['Статья'].dropna().unique()
    print(f"\n📋 Уникальных статей: {len(unique_articles)}")
    
    # Проверка на дубликаты
    article_counts = expense_df['Статья'].value_counts()
    duplicates = article_counts[article_counts > 1]
    
    if len(duplicates) > 0:
        print("\n🔴 Повторяющиеся статьи:")
        for article, count in duplicates.items():
            total = expense_df[expense_df['Статья'] == article]['Итог по году'].sum()
            print(f"  • {article}: {count} раз(а), всего {total:,.0f} ₽")
    else:
        print("\n✅ Нет повторяющихся статей")

else:
    print("\n✅ Категория 'Расход' пуста")
