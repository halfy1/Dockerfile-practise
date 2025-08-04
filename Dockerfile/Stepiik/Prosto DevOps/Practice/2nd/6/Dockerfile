FROM openjdk:17-jdk

LABEL maintainer="you@example.com" \
    version = "1.0" \
    description = "Base Sping Boot Dockerfile with ONBUILD"

ENV SPRING_PROFILES_ACTIVE=default
ENV SERVER_PORT=8080

ONBUILD COPY target/*.jar /app/app.jar
ONBUILD EXPOSE 8080

CMD [ "java", "-jar", "/app/app.jar" ]


