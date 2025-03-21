
# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app
COPY requirements.txt
# i am coping ap
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Command to run FastAPI
CMD  uvicorn main:app
