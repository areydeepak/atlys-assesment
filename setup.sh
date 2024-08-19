#!/bin/bash

# Install Redis
echo "Installing Redis..."
sudo apt-get install -y redis-server

# Start Redis service
echo "Starting Redis server..."
sudo service redis-server start

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Starting the FastAPI server..."
uvicorn app.main:app --reload