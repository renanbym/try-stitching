FROM python:3.6.1-alpine
RUN pip install --upgrade pip
RUN pip install imutils
RUN pip install np
RUN pip install numpy
RUN pip install opencv-python
ENTRYPOINT ["python3", "stitching.py"]
COPY stitching.py /stitching.py