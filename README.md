<p>Here's a simple Python API using Flask that prints the reverse of the origin IP address:</p>
To run this code, you'll need to install Flask if you haven't already: <br/>
<b>pip install flask</b> <br/>
Then you can save the code in a file (e.g., app.py) and run it using: <br/>
<b>python app.py</b> <br/>

API will be accessible at http://127.0.0.1:5000/. When you make a request to this endpoint, it will print the reverse of the origin IP address in the response.


To Dockerize the Flask solution provided, you'll need to create a Dockerfile and build a Docker image for the Flask application. Here's how you can do it:

<h4>Create a Dockerfile:</h4>
Create a file named <b>Dockerfile</b> in the same directory as your Flask application with the following content:

```
# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
RUN pip install Flask

# Expose the port the Flask app runs on
EXPOSE 5000

# Define the command to run the Flask app when the container starts
CMD ["python", "app.py"]
```


<h4>Build the Docker image:</h4>

```
docker build -t flask-app .
```

<h4>Run the docker container</h4>

```
docker run -d -p 5000:5000 flask-app
```

Now, your Flask application is Dockerized and running in a Docker container. You can access it at http://localhost:5000/ in your web browser.
