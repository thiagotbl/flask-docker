# Docker Flask Rabbit Setup

Just a simple setup for a Flask app with a RabbitMQ consumer using Docker.

To start the app for development, just build an image and start a container:

```sh
$ docker image build -t flask-docker .

$ docker container run --name my-flask-app --rm -v $(pwd)/src:/app/src -p 5000:5000 flask-docker
```

Then you should see it running in its full glory on `localhost:5000`.
