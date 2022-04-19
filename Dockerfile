FROM python:3
ADD getweather.py .
RUN pip install requests
CMD ["python", "/getweather.py"]