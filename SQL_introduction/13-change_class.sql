-- Скрипт, который удаляет все записи со score <= 5 в таблице second_table
-- Это очистит таблицу от "неуспевающих" студентов
DELETE FROM second_table 
WHERE score <= 5;
