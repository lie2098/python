FROM python:3.12.3

WORKDIR /app

COPY . /app

CMD ["python", "interactive_mode.py"]