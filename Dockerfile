# Use the Python 3.9 image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /python_backend

# Copy the requirements file and install dependencies
COPY requirements.txt /python_backend/
RUN pip install --no-cache-dir -r requirements.txt --upgrade

# Copy your application code into the container
COPY /python_backend /python_backend/

# Expose port 3001 (assuming your Django app is running on this port)
EXPOSE 3001

# Run migrations
RUN python manage.py migrate

# Start the Django development server
CMD python manage.py runserver 0.0.0.0:3001
