# Similar Candidates Proof of Concept

This project use [Flask](https://flask.palletsprojects.com/en/1.1.x/), [RabbitMQ](https://www.rabbitmq.com/), and [Turi Create](https://github.com/apple/turicreate) to provide a similar candidates endpoint.

To start the app for development, just use docker-compose:

```sh
$ docker-compose up
```

Then you should see it running in its full glory on `localhost:5000`.

And the consumer will be listening for messages on the default exchange.
