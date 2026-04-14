-- Скрипт, который выводит все записи из second_table со score >= 10
-- Результат отображается в порядке убывания баллов (топ-результаты первыми)
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
