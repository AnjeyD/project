# Дашборд для анализа кинематографа
### Это многостраничный дашборд для подбора и анализа фильмов, используя данные из датасета FilmTV. <!-- описание репозитория -->

![Просмотр фильма](https://mykaleidoscope.ru/x/uploads/posts/2023-12/1703421443_mykaleidoscope-ru-p-letnii-kinoteatr-na-dache-pinterest-85.jpg)

Ознакомиться с самим датасетом можно по [ссылке](https://www.kaggle.com/datasets/stefanoleone992/filmtv-movies-dataset).

## О проекте

Наш проект - удобный и интуитивно понятный инструмент для подбора фильмов на основе предпочтений пользователей. 
Кроме того, проект предоставляет статистический анализ, позволяя пользователям лучше понимать тенденции в киноиндустрии, изучать популярность различных жанров в разные года, информацию о том, какие страны больше всего производят фильмы и многое другое. Это может быть полезно не только для киноманов, но и для исследователей, маркетологов и специалистов, работающих в сфере кино.

Таким образом, наш проект не только упрощает процесс выбора фильмов, но и обогащает пользовательский опыт, делая его более персонализированным и информативным.

## Оглавление
- [Немножко про код](#немножко-про-код)
- [Структура проекта](#структура-проекта)
- [Использование](#использование)
- [Установка](#установка)
- [Итог](#итог)
- [Авторы](#автор)

## Немножко про код
В процессе создания многостраничного дашборда использовались:

- **Bootstrap** - это один из наиболее популярных фреймворков для создания пользовательских интерфейсов веб-приложений, который облегчает создание стильных и отзывчивых веб-страниц.
- **Фреймворк Dash**: это инструмент для создания интерактивных веб-приложений с использованием языка программирования Python. Он предоставляет возможности для быстрой разработки данных и аналитики на основе веб-технологий, таких как HTML, CSS и JavaScript.
```sh
    pip install dash
```
- **Dash Bootstrap Components (dash_bootstrap_components)**: это библиотека для фреймворка Dash, которая предоставляет компоненты пользовательского интерфейса, стилизованные в соответствии с Bootstrap.
```sh
    pip install dash_bootstrap_components
```
- **Plotly Express (px)**: высокоуровневый интерфейс для построения интерактивных графиков и визуализаций данных с использованием библиотеки Plotly. Упрощает создание сложных графиков с минимальным кодом.
```sh
    pip install plotly
```
- **Pandas (pd)**: библиотека для работы с данными, предоставляющая структуры данных и операции для манипуляций с таблицами. Используется для загрузки, обработки и анализа данных.
```sh
    pip install pandas
```
- **Plotly Graph Objects (go)**: низкоуровневый интерфейс для построения графиков и визуализаций с помощью Plotly. Предоставляет полный контроль над стилями и атрибутами графиков.

## Структура проекта

```plaintext
├── app.py                 # Главный файл приложения, содержащий настройки и маршрутизацию
├── data.py                # Файл загрузки данных датасета
└── pages/                 # Директория с файлами страниц
    ├── amain.py           # Главная страница
    ├── kinopoisk.py       # Страница подбора фильмов
    ├── topfilm.py         # Страница с топ-10 графиками
    └── xstatistics.py     # Страница статистики фильмов
```
## Использование

Приложение состоит из нескольких страниц:

- **Главная**: Основная информация о проекте.
- **Подбор фильма**: Позволяет пользователям искать фильмы по различным критериям.
- **Топ-10**: Отображает различные топ-10 графиков.
- **Статистика**: Предоставляет различные статистические данные о фильмах.

Для навигации используйте боковую панель меню, как раз таки содержащую эти страницы.

## Установка

1. Склонируйте репозиторий:
    ```sh
    git clone https://github.com/AnjeyD/project.git
    ```
2. Перейдите в директорию проекта:
    ```sh
    cd project
    ```
3. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```
4. Установите необходимые зависимости:
    ```sh
    pip install dash-bootstrap-components
    #pip install -r requirements.txt - в текстовом файле можно указать нужные вам библиотеки
    ```
5. Запуск приложения
После установки всех зависимостей, вы можете запустить приложение командой:
    ```sh
    python app.py
    ```
## Итог
Полученный многостраничный дашборд был размещен в интернете для публичного доступа с помощью ресурса [PythonAnywhere](https://www.pythonanywhere.com).
Самостоятельно ознакомиться с проектом, "пощупать" и "потрогать" его можно по [ссылке](https://doljenkoav.pythonanywhere.com/).

## Авторы
Проект подготовили студенты 3 курса РТУ МИРЭА в 2024 году:
- [Долженко А.В.](https://github.com/AnjeyD)
- [Седова М.А.](https://github.com/sedosha)

Если у вас возникли вопросы или предложения, пожалуйста, свяжитесь с авторами.
