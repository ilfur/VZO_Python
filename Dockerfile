FROM python:3.6
 
WORKDIR /app
COPY . /app
 
RUN pip install -r requirements.txt
 
#ENTRYPOINT ["python"]
#CMD ["app.py"]

#ENTRYPOINT ["uwsgi"]
CMD ["uwsgi","--http", "0.0.0.0:5000", "--wsgi-file", "app.py", "--callable", "app"]
