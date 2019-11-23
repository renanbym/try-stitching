``` sh
docker build -f dockerfile -t renanbym/python:3.6.1-alpine .
docker run -p 5000:5000 renanbym/python:3.6.1-alpine
```


python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png