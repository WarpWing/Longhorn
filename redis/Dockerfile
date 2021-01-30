FROM redis:alpine 
LABEL "repository"="https://github.com/WarpWing/Longhorn"
LABEL "maintainer"="Ty Chermsirivatana"
COPY ../config/redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
# This is a prototype. Don't pay any attention