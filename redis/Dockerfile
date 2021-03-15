FROM redis:4-alpine

WORKDIR /redis
COPY redis.conf /user/local/etc/redis/redis.conf
COPY init.sh ./
RUN chmod +x init.sh

