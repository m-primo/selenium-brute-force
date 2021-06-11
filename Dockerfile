FROM python:latest

COPY app.py /
COPY xreqs.txt /

RUN pip install -r xreqs.txt
CMD ["python", "-u", "app.py"]