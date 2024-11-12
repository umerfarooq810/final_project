# Use Python base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY ims /app/ims

# PYTHONPATH set karein
ENV PYTHONPATH="/app"

# Define the main script as the entrypoint
CMD ["python", "ims/main.py"]


