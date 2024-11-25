FROM debian:bookworm-slim AS base

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    socat

RUN mkdir /challenge && chmod 700 /challenge

COPY joebiden.py setup-challenge.py /app/
COPY start.sh /opt/
RUN chmod +x /opt/start.sh

WORKDIR /app/
RUN tar czvf /challenge/artifacts.tar.gz joebiden.py

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py

EXPOSE 5555
# PUBLISH 5555 AS socat

CMD ["/opt/start.sh"]