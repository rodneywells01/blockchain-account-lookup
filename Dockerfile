FROM python:3.10

WORKDIR /app

# Dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy Structure 
COPY api /app/api
COPY scripts /app/scripts
COPY .flaskenv /app

EXPOSE 5000
EXPOSE 5001

RUN ls -la

RUN export PYTHONPATH=.

# CMD scripts/run_server.sh

CMD python api/main.py
# CMD flask run --host=0.0.0.0
# CMD ls -la

