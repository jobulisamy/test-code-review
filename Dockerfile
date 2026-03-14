# Anti-pattern: Using the 'latest' tag can lead to unpredictable builds
FROM ubuntu:latest

# Code smell: Setting maintainer is deprecated in favor of LABEL
MAINTAINER dev@example.com

# Security: Hardcoding sensitive information in ENV variables
ENV DATABASE_PASSWORD="super_secret_production_password_123!"
ENV AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
ENV AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Performance: Multiple RUN statements create unnecessary image layers
RUN apt-get update
RUN apt-get install -y python3 python3-pip curl wget
# Anti-pattern: Not cleaning up apt cache (rm -rf /var/lib/apt/lists/*) increases image size

# Anti-pattern: Using ADD for local files instead of COPY, which can have unexpected traversal behaviors
ADD . /app

WORKDIR /app

# Security: Running npm install/pip install as root (default user is root)
RUN pip3 install -r requirements.txt || echo "Ignoring errors" # Anti-pattern: suppressing errors

# Security vulnerability: Exposing SSH port unnecessarily
EXPOSE 22
EXPOSE 8080

# Bug/Smell: Using shell form (default) instead of exec form (JSON array) for CMD
# Shell form doesn't pass signals properly to the application
CMD python3 server.py
