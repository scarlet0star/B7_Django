# start from an official image
FROM python:3.8

# arbitrary location choice: you can change the directory

WORKDIR /app

# install our two dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt


# copy our project code
COPY . .