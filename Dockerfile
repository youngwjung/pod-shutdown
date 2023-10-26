FROM python:3.8-alpine

COPY . .

ENTRYPOINT ["python", "./app.py"] 
CMD ["10"]