# Reco-AI-Agent

Reco-AI-Agent is a recommendation system for electronics products, integrating a local MCP (Master Control Program) server with a PostgreSQL database and a Streamlit frontend. The system uses a recommendation AI agent powered by LlamaIndex and Mem0 to provide personalized product recommendations based on vendor and product data. Users can view products, select vendors, see recommendations, and submit reviews.

## Project Overview

- **Purpose**: Provide a scalable, AI-driven recommendation system for electronics products.
- **Tech Stack**:
  - **Python 3.10**: Core language for API and AI logic.
  - **FastAPI**: RESTful API for MCP server.
  - **LlamaIndex SDK**: Orchestrates AI agent workflows.
  - **Streamlit**: Interactive frontend for product browsing and reviews.
  - **Mem0**: Context retention for personalized recommendations.
  - **Postgres VectorDB**: Stores product data with vector embeddings for similarity searches.
  - **Pydantic**: Data validation.
  - **Pytest**: Automated testing.

## Repository Structure

```
Reco-AI-Agent/
├── api/
│   ├── endpoints/           # FastAPI endpoint definitions
│   ├── models/             # Pydantic models for data validation
│   ├── services/           # Business logic and AI agent integration
├── frontend/               # Streamlit frontend code
├── tests/                  # Pytest test cases
├── config/                 # Configuration files (e.g., database, environment)
├── migrations/             # Alembic migration scripts for PostgreSQL
├── scripts/                # Utility scripts
├── docs/                   # Documentation
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
├── requirements.txt         # Python dependencies
├── main.py                 # FastAPI application entry point
└── docker-compose.yml      # Docker Compose for local development
```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Reco-AI-Agent
   ```

2. **Set Up Python Environment**:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Install PostgreSQL and pgvector**:
   - Install PostgreSQL locally or use a Docker container.
   - Enable the `pgvector` extension: `CREATE EXTENSION vector;`

4. **Configure Environment**:
   - Copy `.env.example` to `.env` and update with your PostgreSQL credentials and other settings.

5. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

6. **Start the FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```

7. **Start the Streamlit Frontend**:
   ```bash
   streamlit run frontend/app.py
   ```

8. **Run Tests**:
   ```bash
   pytest tests/
   ```

## Usage

- Access the Streamlit frontend at `http://localhost:8501` to browse products, select vendors, view recommendations, and submit reviews.
- API endpoints are available at `http://localhost:8000/docs` (FastAPI Swagger UI).
- Recommendations are generated using LlamaIndex and Mem0, leveraging product embeddings stored in PostgreSQL.

## Contributing

- Fork the repository.
- Create a feature branch (`git checkout -b feature/your-feature`).
- Commit changes (`git commit -m "Add your feature"`).
- Push to the branch (`git push origin feature/your-feature`).
- Open a pull request.

## License

MIT License
