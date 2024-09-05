# Используем официальный образ с Python 3.9
FROM python:3.9-slim

# Устанавливаем необходимые пакеты: git и pip3
RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем необходимые Python-библиотеки
RUN pip3 install \
    configparser~=7.0.1 \
    ipaddress~=1.0.23 \
    dnspython~=2.6.1 \
    httpx~=0.27.0 \
    colorama~=0.4.6

# Указываем рабочую директорию для приложения
WORKDIR /app

# Клонируем репозиторий в контейнер
RUN git clone https://github.com/Ground-Zerro/DomainMapper.git /app

# Копируем конфигурационный файл config.ini (если он отсутствует в репозитории)
ADD https://github.com/Ground-Zerro/DomainMapper/blob/main/config.ini /app/config.ini

# Запускаем main.py из клонированного репозитория
CMD ["python3", "/app/main.py"]
