FROM python:3.12.10-slim

# Set the root working directory inside the container
WORKDIR /app/task1

# Copy everything, preserving the full folder structure (task1/, templates/, etc.)
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the port the app runs on
EXPOSE 80

# Run the app from inside /app/task1 where data.json exists
CMD ["python", "matches.py"]
