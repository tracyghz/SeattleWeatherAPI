FROM python:3.9-slim
LABEL authors="huizhonggao"

# Set environment variables for Flask
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0  # Allow external access

# Set the working dir in the container
WORKDIR /app

# Copy the current working dir into the container under /app
COPY . /app

# Copy the CSV file into the container
COPY static/seattle-weather.csv /app/static/seattle-weather.csv

# Install packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Expose port 443 of the container to the world
EXPOSE 443

# Run the Flask application on port 8080
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]
