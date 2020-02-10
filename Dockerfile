FROM python:3
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ africastalking==1.1.7.post4
COPY . .
CMD ["python","data.py"]