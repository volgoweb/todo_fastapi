FROM python:3.9.13-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /membership
WORKDIR /membership

RUN apt-get update && \
    apt-get install -y python-dev \
    python3-dev && \
    python3 -m pip install poetry && \
    poetry config virtualenvs.create false

RUN addgroup --system app && adduser --system --group app
USER app

COPY pyproject.toml poetry.lock ./
RUN python3 -m pip install --upgrade pip && \
    poetry install --no-root && \
    poetry install --no-root

COPY ./ ./

EXPOSE 80
#ENTRYPOINT ["uvicorn", "membership.main:app", "--reload"]
#CMD ["--port", "80"]
HEALTHCHECK CMD curl --fail http://localhost:80/healthcheck || exit 1
