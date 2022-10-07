FROM python
COPY . /app
WORKDIR "/app/"
#RUN pip install behave, works fine, but unnecessary since tests are being run through jenkins