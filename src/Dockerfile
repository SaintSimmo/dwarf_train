FROM ubuntu:15.10

COPY requirements.txt /dwarf_train/requirements.txt

# install requirements
RUN apt-get update
RUN apt-get install -y python python-pip gunicorn libpq-dev python-dev
RUN pip install -r /dwarf_train/requirements.txt

EXPOSE 80

ENTRYPOINT /usr/bin/python -B /dwarf_train/src/run.py
