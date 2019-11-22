FROM python:3.6.1-alpine
RUN pip install --upgrade pip
RUN pip install imutils
RUN pip install opencv
ENTRYPOINT [“python”, “stitching.py”]
COPY stitching.py /stitching.py