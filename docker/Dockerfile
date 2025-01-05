FROM python:3.11-bullseye

# https://www.baeldung.com/ops/docker-cron-job
# Add cron job
ADD docker/hello_world.sh /app/hello_world.sh

# Give execution rights to script
RUN chmod 0644 /app/hello_world.sh

ADD requirements.txt /install/requirements.txt
RUN python3 -m pip install -r /install/requirements.txt
RUN rm -rf /install/

# Install cron
RUN apt-get update
RUN apt-get install -y cron nano

# Add the cron job
RUN crontab -l | { cat; echo "* * * * * bash /app/hello_world.sh"; } | crontab -

ADD src/ /app/

CMD cron
