FROM python:3.6.1-alpine
RUN pip install --upgrade pip
ENTRYPOINT ["python", "stitching.py"]
COPY stitching.py /stitching.py