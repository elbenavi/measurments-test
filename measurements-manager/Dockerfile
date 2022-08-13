# GLOBAL ARGS
## venv location build argument (with default)
ARG DEFAULT_ENV_DIR=/opt/venv
# COMPILE-IMAGE
# Create the virtual environment to copy over to build-image
FROM python:3.9 AS compile-image
ARG DEFAULT_ENV_DIR
ENV ENV_DIR=$DEFAULT_ENV_DIR
# Create venv
RUN python -m venv $ENV_DIR

# Make sure we use the virtualenv:
ENV PATH="$ENV_DIR/bin:$PATH"
RUN echo $PATH
# upgrade pip
RUN python -m pip install --upgrade pip
# RUN pip install pip==20.1
# use working directory
WORKDIR /app
COPY requirements.txt .

RUN python -m pip install -r requirements.txt
# BUILD-IMAGE
# FROM python:3.9-slim-buster AS build-image
FROM python:3.9 AS build-image
COPY --from=compile-image $ENV_DIR $ENV_DIR
ARG DEFAULT_ENV_DIR
ENV ENV_DIR=$DEFAULT_ENV_DIR
# Make sure we use the virtualenv:
ENV PATH="$ENV_DIR/bin:$PATH"
# expose http port
EXPOSE 80
# use working directory
WORKDIR /app
# Copy app source
COPY ./app /app/app
COPY ./alembic.ini /app/alembic.ini
COPY ./alembic /app/alembic
COPY prestart.sh /app
# set default entrypoint
# ENTRYPOINT ["python"]
# set default command
# CMD ["-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

CMD ["/bin/bash","prestart.sh"]
