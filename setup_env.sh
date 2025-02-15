#!/bin/bash

# Get the absolute path of the project root (where this script is located)
PROJECT_ROOT=$(dirname "$(realpath "$0")")

# Define the virtual environment directory in the project root
VENV_DIR="$PROJECT_ROOT/venv"

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "❌ Python3 is not installed. Please install it first."
    exit 1
fi

# Create the virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "🚀 Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "✅ Virtual environment already exists in $VENV_DIR."
fi

# Activate the virtual environment based on OS
if [[ "$OSTYPE" == "darwin"* || "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🔹 Activating virtual environment..."
    source "$VENV_DIR/bin/activate"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    echo "🔹 Activating virtual environment (Windows)..."
    source "$VENV_DIR/Scripts/activate"
else
    echo "❌ Unsupported OS type: $OSTYPE"
    exit 1
fi

# Install dependencies from requirements.txt if available
REQ_FILE="$PROJECT_ROOT/requirements.txt"
if [ -f "$REQ_FILE" ]; then
    echo "📦 Installing dependencies from $REQ_FILE..."
    pip install -r "$REQ_FILE"
else
    echo "⚠️ No requirements.txt found in the project root. Skipping dependency installation."
fi

echo "✅ Virtual environment setup complete!"
echo "🔹 To activate manually, run:"
echo "  source venv/bin/activate  # (Mac/Linux)"
echo "  venv\\Scripts\\activate  # (Windows)"
