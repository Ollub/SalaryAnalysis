# SalaryAnalysis
Программа для анализа зарплат программистов для популярных языков программирования.  
Используются API HeadHunter и SuperJob

### Как установить

1. git clone <url репозитория> 
*Python3 должен быть уже установлен.*
*Далее приведены команды для UNIX системы*
2. Создайте и активируйте виртуальное окружение
```
$ python3 -m venv env
$ source env/bin/activate

```
3. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
$ pip install -r requirements.txt
```
4. Запуск приложения
```
$ python main.py
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корневой директории и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:
- `SJ_API_KEY` — имя пользователя инстаграм

[получение api_key SuperJob](https://api.superjob.ru/info/)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).