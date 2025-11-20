    FROM python:3.12

    RUN mkdir -p /home/app
    
    COPY . /home/app

    RUN pip install -r /home/app/requirements.txt

    WORKDIR /home/app

    EXPOSE 8000

    CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]