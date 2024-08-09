#!/bin/bash

# Path to the directory on the host where the images will be stored
host_data_path="$1"

# Build the Docker image
docker build -t image_processor .

# Run the Docker container, mapping the host directory to /data in the container
docker run -v "${host_data_path}:/data" image_processor

