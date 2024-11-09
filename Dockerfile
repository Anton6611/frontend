# Используем образ Python 3.12 с минимальным набором пакетов
FROM python:3.12-slim
# Устанавливаем рабочий каталог в /app
RUN mkdir /app
WORKDIR /app
#RUN apt-get update && apt-get install -y python3-tk
# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y python3-tk && apt-get clean && rm -rf /var/lib/apt/lists/*
#Устанавливаем переменную DISPLAY для работы с X11
ENV DISPLAY=host.docker.internal:0
# Устанавливаем X11-клиент
RUN apt-get update && apt-get install -y x11-apps  #Устанавливаем пакеты для работы с X11
# Копируем файл requirements.txt в рабочий каталог
COPY requirements.txt .
# Устанавливаем зависимости из файла requirements.txt
RUN pip install -r requirements.txt
# Копируем текущий каталог в рабочий каталог
COPY . .
# Открываем порт 8002 для работы с приложением
EXPOSE 8002
# Устанавливаем команду для запуска приложения
CMD ["python", "main.py", "--host=0.0.0.0", "--port=8002"]