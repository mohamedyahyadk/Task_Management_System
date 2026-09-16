FROM python:3.12-slim
LABEL maintainer="mohamedyahyadkhila@gmail.com"
# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure Python output is sent straight to the terminal
ENV PYTHONUNBUFFERED=1
# Use the virtual environment by default
ENV PATH="/py/bin:$PATH"
# Copy requirements first for better Docker layer caching
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
# Development mode
ARG DEV=false
# Install Python dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user
# Copy project
COPY ./app /app
# Set working directory
WORKDIR /app
# Give application ownership to django-user
RUN chown -R django-user:django-user /app
# Expose Django development port
EXPOSE 8000
# Run as non-root user
USER django-user
# Start Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]