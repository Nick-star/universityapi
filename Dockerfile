# Базовый образ Python
FROM python:3.10

# Рабочая директория в контейнере
WORKDIR /app

# Копия файлов проекта в контейнер
COPY . /app

# Установка зависимостей проекта
RUN pip install --no-cache-dir -r requirements.txt

# Запуск приложения FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
