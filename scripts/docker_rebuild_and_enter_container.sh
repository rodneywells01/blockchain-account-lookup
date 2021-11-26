docker compose build api
docker run -it --entrypoint=bash crypto_nw_tracker:latest -c 'python api/main.py'