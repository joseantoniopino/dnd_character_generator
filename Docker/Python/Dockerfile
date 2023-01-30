# Use the official Python image
FROM python:bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
&& pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the user to be used when running the container
USER 1000

# Set the default command to run when the container starts
CMD [ "python", "main.py" ]
