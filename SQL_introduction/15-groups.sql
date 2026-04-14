-- Скрипт, который выводит количество записей с одинаковым баллом в таблице second_table
-- Выводит score и количество записей для этого балла (number)
-- Результат отсортирован по убыванию количества (number)
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
