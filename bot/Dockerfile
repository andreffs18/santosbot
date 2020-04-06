FROM python:3.7

ENV PROJECT_DIR /app
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

COPY main.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# RUN pipenv install --system --deploy
CMD python main.py