# Тестовое задание от Silicium

## На примере сайта https://demoqa.com

### Шаги
Тест иногда падает из-за наличия рекламы в разных местах и перекрытия элементов (зависит от страны)
повторить пару раз
1. Склонировать репозиторий "git clone"
2. Установить вирт окружение "python -m venv venv"
3. Установить зависимости "pip install -r requirements.txt"
4. Запустить тест "pytest -s -v --alluredir allure_results"
5. Просмотреть отчет "allure serve allure_results"

### Стек
- Selenium
- Webdriver-manager
- PyTest
- Allure

### Структура
./base - настройки
  - base_page.py - класс базовой страницы и основные скрипты
  - base_test.py - класс наследования для тестов
./config - данные
  - links.py - класс ссылок
./pages - страницы
  - test_page.py - класс тестируемой страницы
./tests - тесты
  - test_by_test.py - тесты
  - images.png - файл для загрузки
README.md
conftest.py - файл настройки драйвера и фикстур
pytest.ini - файл настройки pytest
requirements.txt - список модулей и пакетов
