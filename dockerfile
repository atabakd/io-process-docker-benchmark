# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Install system libraries required for common OpenCV functionalities
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext-dev \
    && rm -rf /var/lib/apt/lists/*

# Install numpy and opencv-python
RUN pip install numpy==1.19.2 opencv-python==4.2.0.34

# Copy the Python script into the container at /app
COPY generate_images.py /app

# Run generate_images.py when the container launches
CMD ["python", "generate_images.py"]

