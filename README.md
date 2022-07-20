# Selenium+Pytest+Allure

**Описание**
Тестирование сайта yandex.ru

**Инструкция для Windows**
Тесты запускаются в браузерах Chrome, Firefox. Для работы с тестами потребуются **chromedriver** и **geckodriver**

Для создания отчетов используется **Allure**, который требуется установить.

Запускаем тесты и создаем папку для отчетов командой: ```pytest --alluredir=results```
Создание отчёта в **PowerShell**: ```allure serve reports```
Для параллельного запуска тестов: ``` pytest -v -n 3```
