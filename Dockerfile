FROM python:3.8
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера
WORKDIR /glossary
# Копирует все файлы из нашего локального проекта в контейнер
ADD ./glossary
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN pip install -r requirements.txt

