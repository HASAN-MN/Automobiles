# Base image for Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose backend FastAPI port
EXPOSE 8000

# Expose frontend Streamlit port
EXPOSE 8501

# Use process manager to run both backend and frontend
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend/app.py --server.port=8501 --server.address=0.0.0.0"]
