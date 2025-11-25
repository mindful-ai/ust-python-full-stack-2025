FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /usr/project

# Install dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy the current directory contents into the container at /app
COPY ./ ./

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Set the environment variables for Flask
ENV FLASK_APP=app
ENV FLASK_DEBUG=1
ENV PYTHONUNBUFFERED=1

# Run the Flask app
CMD ["python", "server.py"]