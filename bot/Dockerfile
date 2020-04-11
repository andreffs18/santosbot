FROM python:3.7

WORKDIR /app

# Copy only requirements to cache them in docker layer
COPY requirements.txt ./
# Install bot requirements
RUN pip install --no-cache-dir -r requirements.txt
# Copy actual bot script
COPY main.py ./

CMD python main.py
