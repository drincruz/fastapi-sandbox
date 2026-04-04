FROM python:3.12

ENV PORT 8000

# Set the working directory
WORKDIR /usr/local/fastapi-sandbox

# copy requirements.txt first
COPY ./requirements.txt /usr/local/fastapi-sandbox/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /usr/local/fastapi-sandbox/requirements.txt

# Copy the current directory contents into the container at /usr/local/fastapi-sandbox/
COPY . /usr/local/fastapi-sandbox/

# Make port 8000 available to the world outside this container
EXPOSE ${PORT}

# Run src/main.py when the container launches
CMD ["fastapi", "dev", "src/app/main.py", "--proxy-headers", "--host", "0.0.0.0"]
