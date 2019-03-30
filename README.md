# Uptime kafka consumer

This project consumes data from a `uptime` kafka server and stores it in a PostgreSQL database for persistence.

## Install

Install the script in a virtualenv:

    pip3 install git+https://github.com/fmorato/uptime-consumer.git

Run from a terminal or use a supervisor such as `systemd` or `supervisord`.

    consumer --ca /path/to/ca \
            --cert /path/to/cert \
            --key /path/to/key \
            --group-id GROUP_ID \
            --topic TOPIC \
            --kafka KAFKA_URL \
            --postgres POSTGRES_URI

There is an extra script for creating the database table if it does not exist yet.

    setup-postgres --postgres POSTGRES_URI

PostgreSQL URI reference is [here](https://www.postgresql.org/docs/11/libpq-connect.html#id-1.7.3.8.3.6).

## Development

Clone the repository from github:

    git clone https://github.com/fmorato/uptime-consumer.git
    cd uptime-consumer
    mkvirtualenv -a . -p python3 uptime-consumer  # requires virtualenvwrapper
    pip install -e .

Start the consumer with:

    consumer --topic TOPIC --kafka KAFKA_URL --postgres POSTGRES_URI

# Deploying

On this screen cast I install both producer and consumer on a remote host as well as create and start the services with systemd.

[![asciicast](https://asciinema.org/a/NZdX5SGFzST3LU9XvVwyoE846.svg)](https://asciinema.org/a/NZdX5SGFzST3LU9XvVwyoE846?speed=2&autoplay=1)