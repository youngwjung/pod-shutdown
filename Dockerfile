FROM python:3.8-alpine

COPY . .
RUN chmod +x shutdown.sh

ENTRYPOINT ["python","-u","./app.py"] 
CMD ["10"]