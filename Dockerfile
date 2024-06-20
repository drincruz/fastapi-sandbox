FROM python:3.12

ENV PORT 8000

# Set the working directory
WORKDIR /usr/local/fastapi-sandbox

# Copy the current directory contents into the container at /usr/local/fastapi-sandbox/
COPY . /usr/local/fastapi-sandbox/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE ${PORT}

# Run src/main.py when the container launches
CMD ["fastapi", "dev", "src/main.py", "--host", "0.0.0.0"]
