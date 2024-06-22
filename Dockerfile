FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=api.py
EXPOSE 5000


#api mainloop
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]