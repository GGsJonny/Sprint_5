# Sprint_5 
# Проект: Stellar Burgers

## Описание
Проект Stellar Burgers представляет собой веб-приложение для заказа бургеров. Пользователи могут создавать свои собственные бургеры, добавлять их в корзину и оформлять заказ. Приложение также включает личный кабинет, где пользователи могут просматривать и редактировать свои данные.

## Установка
Для установки и запуска проекта выполните следующие шаги:

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/yourusername/stellar-burgers.git
Перейдите в директорию проекта:

cd stellar-burgers
Установите зависимости:

pip install -r requirements.txt
Запуск тестов
Для запуска тестов выполните следующие шаги:

Активируйте виртуальное окружение:

source venv/bin/activate
Убедитесь, что все зависимости установлены:

pip install -r requirements.txt
Запустите тесты с помощью команды:

pytest
Структура проекта
stellar-burgers/
├── .gitignore
├── README.md
├── conftest.py
├── data.py
├── helper_test.py
├── locators.py
└── test/
    ├── test_go_to_page.py
    ├── test_login.py
    ├── test_registration.py
    └── test_section_constructor.py
Проект включает следующие тесты:
test_go_to_personal_account_from_main: Проверяет переход в личный кабинет с главной страницы.
test_go_to_designer_from_personal_account_click_button: Проверяет переход в конструктор бургеров из личного кабинета по кнопке.
test_go_to_designer_from_personal_account_click_logo: Проверяет переход в конструктор бургеров из личного кабинета по логотипу.
test_logout_in_personal_account_page: Проверяет выход из личного кабинета.
test_add_burger_to_cart: Проверяет добавление бургера в корзину.
test_remove_burger_from_cart: Проверяет удаление бургера из корзины.
test_place_order: Проверяет оформление заказа.
test_edit_user_profile: Проверяет редактирование профиля пользователя.
test_view_order_history: Проверяет просмотр истории заказов.
test_login_with_invalid_credentials: Проверяет вход с неверными учетными данными.
test_register_new_user: Проверяет регистрацию нового пользователя.
Используемые технологии
Selenium WebDriver: Для автоматизации тестирования веб-приложений.
Python: Основной язык программирования.
Pytest: Фреймворк для тестирования.
Контакты
Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами по адресу: [praktikum@support.yandex.ru]
