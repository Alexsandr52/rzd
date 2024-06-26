# Проверка соответствия разговоров участников железнодорожного движения

Стек решения:

- Python;
- Nvidia NeMo (ASR);
- spaCy (NLP);
- FastAPI (BACKEND для обработки запросов);
- Streamlit (FRONTEND для демонстрации работы модуля);

## Описание

Наше решение транскрибирует переговоры в текст, а затем анализирует его. Для повышения точности распознавания, из аудио переговоров удаляются шумы, повышается громкость и выбираются участки аудиодорожки с непосредственно разговорами.

### Этапы обработки

1. Транскрипция:
    - Аудиозаписи преобразуются в текстовый формат.

2. Предобработка текста:
    - Лематизация
    - Токенизация
    - Стемминг

3. Анализ текста:
    - Оценка по категориям соответствия регламенту:
    - Наличие специальных слов ("спасибо", "пожалуйста" и т.д.)
    - Соблюдение регламента начала обращения (например, "Машинист поезда №...", "Дежурный по станции..., слушаю")

4. Оценка качества речи говорящего.

5. Результаты
    - После оценки возвращается один из следующих ответов: "Соответствует"/"Не соответствует"

В случае нарушений регламента возвращается текст переговоров с указанием, в каких категориях регламента были допущены нарушения.

## Запуск (API, ASR, NLP)

1. Создайте виртуальное окружение и активируйте его:

    ```bash
    # unix
    python3 -m venv .env

    # windows
    python -m venv .env

    # activate venv
    source .env/bin/activate
    ```

2. Установите зависимости:

    ```bash
    # unix
    chmod +x get_ready.sh
    sh get_ready.sh

    # windows
    .\get_ready.bat

    # если скрипты не работают попробуйте вручную
    pip install -r requirements.txt
    pip install nemo_toolkit[all]
    python3 -m spacy download ru_core_news_sm
    ```

3. Запустите:

    ```bash
    # unix
    python3 run home.py

    # windows
    python run home.py
    ```

## Документация API

Документация API доступна по [ссылке](https://pars1vali-rzd-0f52.twc1.net/docs).

## Рабочий прототип

Рабочий прототип доступен по [ссылке](https://rzd-app.streamlit.app/).
