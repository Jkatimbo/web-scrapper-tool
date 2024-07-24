#!/bin/bash

# Create virtual environment
python3.8 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Setup complete. You can now run the scraper using 'python scraper.py'."
