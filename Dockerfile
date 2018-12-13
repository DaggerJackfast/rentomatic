FROM python:alpine3.8
ADD requirements /requirements
RUN pip install -r /requirements/prod.txt
ADD . /rentomatic
RUN rm -rf /requirements
WORKDIR /rentomatic
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "rentomatic.main:app"]
