# Анализ связи ключевых показателей игровой статистики с успешностью команды в профессиональном Counter-Strike
*HSE economics — data analysis project 2025 by Vasiliy Bloshenko*

## О чём проект
Как и в традиционном спорте, в киберспорте совсем непросто установить, какие факторы влияют на успешность игрока или команды. В этом проекте я собираюсь рассмотреть, как связаны некоторые ключевые показатели игровой статистики команд в мировом профессиональном Counter-Strike с их успешностью. Надеюсь, что анализ статистики покажет какие-нибудь корреляционные связи. А если нет — скажем, что спорт непредсказуемая штука.

## Репозиторий
main.ipynb — основной файл с анализом данных

dataset.csv — датасет в формате csv.

parser.py — парсер

## Данные
Данные взяты парсингом с крупнейшего агрегатора hltv.org. Использованы данные за 2012-2025 годы. В датасете представлены следующие показатели:
1. Доля выигранных раундов — она будет основной мерой успешности.
2. Доля раундов с первым убийством.
3. Доля раундов со множественными убийствами.
4. Доля выигранных раундов в большинстве.
5. Доля выигранных раундов в меньшинстве.
6. Доля разменянных смертей.
7. Средний урон гранатами за раунд.
8. Среднее количество убийств ослеплённых противников за раунд.
9. Доля выигранных стартовых раундов
10. Доля побед в раундах после выигранного стартового.
11. Доля побед в раундах после проигранного стартового.

Важно: сайт не горит желанием отдавать данные мутным личностям, обойти HTTP 403 у меня получилось только с моего ПК. Проще говоря, парсер работает настолько, насколько hltv.org не блокирует запрос. Я данные сумел вытащить, а это главное.
