FROM alpine:latest

RUN apk add --no-cache bash \
    curl \
    git \
    htop \
    coreutils 

WORKDIR /utils

RUN echo "alias ll='ls -la'" >> /etc/profile.d/custom-aliases.sh"

CMD [ "sh" ]