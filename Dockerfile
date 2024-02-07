FROM python:3.6-slim
WORKDIR /app 
COPY requirements.txt .                   
RUN pip install -r requirements.txt
ADD . /app
EXPOSE 8080
CMD ["python","app.py"]
#docker build -t flask-app .
#docker run -d -p 5000:8080 flask-app 
#http://localhost:5000
#expected result in browser: It works!
