FROM python:3.12-slim

COPY . /

RUN pip install --no-cache-dir discord.py pymongo dotenv

CMD [ "python", "-u", "main.py" ]