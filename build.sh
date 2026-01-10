#!/bin/bash
set -e

echo "Building SMWS Codes..."

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Install requirements
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Generate the HTML
echo "Generating HTML..."
python render.py > public/index.html

echo "Build complete! Output: public/index.html"
