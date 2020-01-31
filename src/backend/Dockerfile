###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.0-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1 


# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . /usr/src/app
RUN flake8 --ignore=E501,F401 .

# install dependencies
RUN mkdir /config
COPY config/requirements.pip /config/

#########
# FINAL #
#########

# pull official base image
FROM python:3.8.0-alpine

# create directory for the app user
RUN mkdir -p /src

# # create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/src
ENV APP_HOME=/src/backend
ENV CONFIG_HOME=/src/config
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
RUN mkdir $CONFIG_HOME
WORKDIR $APP_HOME


# install dependencies
RUN apk update && apk add libpq postgresql-dev gcc python3-dev musl-dev libffi-dev py3-cffi
COPY --from=builder /config/requirements.pip $CONFIG_HOME/requirements.pip
RUN pip install --upgrade pip
RUN pip install --no-cache -r ${CONFIG_HOME}/requirements.pip


# copy entrypoint.sh
COPY ./entrypoint.sh $HOME

# copy project
COPY . $APP_HOME 

# Make port 8000 available for the app
EXPOSE 8000

# change to the app user
USER app


ENTRYPOINT ["/src/entrypoint.sh"]



# Did you notice that we created a non-root user? By default, 
# Docker runs container processes as root inside of a container. 
# This is a bad practice since attackers can gain root access to the Docker host 
# if they manage to break out of the container. 
# If you're root in the container, you'll be root on the host.