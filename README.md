# Docker Flask Rabbit Setup

Just a simple setup for a Flask app with a RabbitMQ consumer using Docker.

To start the app for development, just use docker-compose:

```sh
$ docker-compose up
```

Then you should see it running in its full glory on `localhost:5000`.

And the consumer will be listening for messages on the default exchange.
