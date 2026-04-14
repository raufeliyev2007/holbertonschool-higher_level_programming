-- Скрипт выводит все записи из second_table, где заполнено поле name
-- Результат отсортирован по убыванию баллов
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
