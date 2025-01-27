FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY *.py .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Add a healthcheck for every 60 seconds with a 20 second timeout for the request. 
# Allow the app to take 5 seconds to start before attempting healthcheck.
# Allow for 3 failed responses before labeling container as unhealthy.
# Use python script to perform healthcheck to avoid installing additional packages.
HEALTHCHECK --interval=60s --timeout=20s --start-period=5s --retries=3 \
    CMD python /app/healthCheck.py
