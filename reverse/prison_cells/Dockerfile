FROM ubuntu:20.04

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src/server/* /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 1337 available to the world outside this container
EXPOSE 1337

# Run app.py when the container launches
CMD ["python3", "server.py"]