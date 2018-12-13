FROM python:alpine3.8
COPY requirements /requirements
RUN pip install -r requirements/prod.txt
RUN rm -rf requirements
ADD . ~/rentomatic

CMD ["gunicorn", "-b", "0.0.0.0:5000", "rentomatic.main:app"]
