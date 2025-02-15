'''Команды, использованные для создания базы данных'''
psql -U postgres
create database marmot_vision;
create role admin with login password 'sursursur';
grant all privileges on database marmot_vision to admin;

\с marmot_vision # Входим в сурковую базу данных

grant all privileges on schema public to admin;
alter default privileges in schema public grant all on tables to admin;

# Дальше создаём группового пользователя