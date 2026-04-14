-- Скрипт выводит все записи таблицы second_table
-- Отображает только колонки score и name
-- Сортировка строго по убыванию баллов (top score first)
SELECT score, name
FROM second_table
ORDER BY score DESC;
