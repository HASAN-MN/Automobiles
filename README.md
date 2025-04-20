# Project Overview

This project consists of a **frontend** developed using **Streamlit**, a **backend** built with **FastAPI**, and utilizes **MySQL** as the database. The entire setup is containerized using Docker for ease of deployment and management.

## Features

- **Frontend:** Interactive and user-friendly interface powered by Streamlit.
- **Backend:** High-performance API developed with FastAPI.
- **Database:** Reliable and efficient data storage using MySQL.
- **Docker:** Streamlined containerization for consistent environment across systems.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Python 3.8+ (if working locally)
- MySQL server (optional if you want external database)

## Setup Instructions

### Build and Run the Docker Container

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-folder>


### FastAPI 
uvicorn api.main:app

### Frontend
streamlit run app.py --server.port=8501 --server.address=127.0.0.1
