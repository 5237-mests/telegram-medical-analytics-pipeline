# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set Python path for internal imports
ENV PYTHONPATH=/app

# Expose FastAPI default port
EXPOSE 8000

# Default command to run FastAPI
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
