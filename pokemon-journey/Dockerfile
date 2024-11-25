FROM debian:bookworm-slim AS base

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    gcc \
    libc6-dev-i386 \
    # Build in for x86
    socat

RUN mkdir /challenge && chmod 700 /challenge

COPY pokemon.c setup-challenge.py /app/
COPY start.sh /opt/
RUN chmod +x /opt/start.sh

WORKDIR /app/
RUN gcc -m32 -O0 -fno-stack-protector -fno-inline -Wall -z relro -z execstack -no-pie pokemon.c -o pokemon
RUN tar czvf /challenge/artifacts.tar.gz pokemon

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py

EXPOSE 1996
# PUBLISH 1996 AS socat

CMD ["/opt/start.sh"]