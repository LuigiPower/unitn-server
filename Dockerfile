FROM python:3-onbuild
ENV FLASK_APP=runserver.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
