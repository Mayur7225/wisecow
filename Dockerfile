# Use a small Ubuntu base
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/games:/usr/bin:${PATH}"
WORKDIR /app

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      curl \
      bash \
      fortune-mod \
      cowsay \
      socat \
      netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Copy application files and certificates
COPY wisecow.sh /app/wisecow.sh
RUN chmod +x /app/wisecow.sh

# Expose TLS port
EXPOSE 4499

# Run Wisecow with TLS automatically
CMD ["/bin/bash", "/app/wisecow.sh"]

