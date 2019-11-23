FROM python:3.6.1-alpine
RUN apk add --update python python-dev gfortran py-pip build-base py-numpy@community
RUN pip install --upgrade pip
RUN pip install boto3
RUN pip install imutils
RUN pip install np
RUN pip install numpy
RUN pip install opencv-python
ENTRYPOINT ["python", "stitching.py"]
COPY stitching.py /stitching.py