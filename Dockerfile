# Use official Python image (slim version for smaller size)
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose port 8000 (used by Django dev server)
EXPOSE 8000

# Optional: allow passing environment variables like DEBUG and ALLOWED_HOSTS
# You must ensure settings.py uses os.environ to read these values

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]