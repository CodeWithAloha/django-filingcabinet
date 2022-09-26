FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE fc_project.settings

RUN apt-get update && apt-get install -y --no-install-recommends imagemagick tesseract-ocr poppler-utils qpdf

WORKDIR /project

RUN useradd -m -r appuser && chown appuser /project

# COPY requirements.txt ./
# RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && chown appuser /entrypoint.sh

# copy the whole project except what is in .dockerignore
COPY . .
RUN pip install -e .[annotate] gunicorn celery[redis] whitenoise

USER appuser
EXPOSE 8000

RUN python ./manage.py collectstatic