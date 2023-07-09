FROM python:3.8


WORKDIR /app


COPY . .

ADD app.py .


RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask

EXPOSE 8000

CMD ["python", "app.py"]

