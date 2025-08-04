FROM nginx:alpine

COPY default.conf /etc/nginx/conf.d/default/conf
COPY htpasswd /etc/nginx/htpasswd
COPY index.html /usr/share/nginx/html

EXPOSE 80
