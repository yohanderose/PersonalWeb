
FROM python:3.6

WORKDIR /usr/src/app

RUN apt update && apt install vim -y
RUN pip install Flask requests numpy pandas

COPY . . 
CMD ["python", "main.py"] 
