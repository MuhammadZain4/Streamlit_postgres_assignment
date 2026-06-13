FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy and install dependencies first (layer caching optimization)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app source code
COPY app/ ./app/

# Expose Streamlit's default port
EXPOSE 8501

# Run Streamlit — bind to all interfaces so Docker port mapping works
CMD ["streamlit", "run", "app/main.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.headless=true"]
