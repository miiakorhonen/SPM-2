FROM python:3.12

WORKDIR /app

COPY . /app

EXPOSE 80

CMD ["python", "SPM2.py"]