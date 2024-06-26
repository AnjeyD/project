from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H1("Главная страница"),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'})
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.H3("Информация о проекте:"),
            ], style={'textAlign': 'left'})
        )
    ]),
    
    html.Br(),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.P([
                    "Проект выполнен студентами РТУ МИРЭА с направления ",
                    "Информационные системы и технологии",
                    ", заканчивающими 3 курс, из группы БСБО-14-21: ",
                    html.Strong("Долженко Андреем Владимировичем"),
                    " и ",
                    html.Strong("Седовой Марией Александровной."),
                ], style={'fontSize': '1.5rem'}),
                html.P([
                    "Наш проект — многостраничный сайт о фильмах, сделанный на Python с использованием стилей и библиотек ",
                    html.Em("Bootswatch"),
                    " и ",
                    html.Em("Bootstrap"),
                    ". В нашем меню есть 4 страницы: ",
                    html.U("Главная"),
                    ", ",
                    html.U("Подбор фильма"),
                    ", ",
                    html.U("Топ-10"),
                    " и ",
                    html.U("Статистика"),
                    ". На Главной странице вы читаете этот текст сейчас, на странице с Подбором фильмов представлены разнообразные фильтры для поиска нужного фильма. На третьей странице можно увидеть, как в зависимости от года или промежутка лет менялись ТОП-10 жанров, режиссёров, стран, производящих фильмы, и актёров. На последней странице представлена разнообразная статистика по разным характеристикам фильмов, которые не были задействованы на предыдущих страницах, а также представлена глобальная карта по всем странам и их средней статистике по выбранному году или промежутку лет."
                ], style={'fontSize': '1.5rem'}),
                html.P([
                    "В работе сайта используется датасет с информационного портала Kaggle: ",
                    html.A("сам датасет", href="https://www.kaggle.com/datasets/stefanoleone992/filmtv-movies-dataset", target="_blank"),
                ], style={'fontSize': '1.5rem'}),
                html.P("Датасет представляет собой информацию по более 41 тысяче фильмов, собранную с итальянского сайта FilmTV. Данные разбиты на 19 колонок: ID, Название, Год выпуска, Жанр, Длительность, Страну(ы) производителя(и), Актёры, Рейтинг фильма, Оценка критиков, Оценка зрителей, Общее количество голосов, отданных критиками и публикой, Описание фильма, Примечание к фильму и Оценки фильма от FilmTV по характеристикам (Юмор, Ритм, Работа над фильмом, Напряжение и Эротика).",
                       style={'fontSize': '1.5rem'}),
                html.P("Ссылка проекта на GitHub:", style={'fontSize': '1.5rem'}),
            ], className='text-primary', style={'textAlign': 'justify'})
        ),
    ]),

])