FROM python:3.10

WORKDIR /app

# Dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy Structure 
COPY api /app
COPY scripts /app/scripts
COPY .flaskenv /app

EXPOSE 5000

RUN ls 

# CMD scripts/run_server.sh
CMD flask run --host=0.0.0.0

