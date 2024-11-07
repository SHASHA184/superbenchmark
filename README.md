
# SuperBenchmark

SuperBenchmark is a FastAPI application designed to manage and query benchmarking results for a Large Language Model (LLM). The application allows users to retrieve average performance statistics for generated benchmarking results either across all records or within a specified time range.

## Features

- **HTTP GET /results/average**: Retrieve the average performance statistics across all benchmarking results.
- **HTTP GET /results/average/{start_time}/{end_time}**: Retrieve the average performance statistics within a specific time range.
- **Debug Mode**: Load data from a local JSON file (`test_database.json`). In production, this feature is not implemented yet.

## Installation

### Prerequisites

- Python 3.10.12
- Git
- Virtual environment tool (optional but recommended)

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SHASHA184/superbenchmark
    cd superbenchmark
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Configuration:**

    Create a `.env` file in the root directory and set `SUPERBENCHMARK_DEBUG` to `True` to enable debug mode.

    ```plaintext
    SUPERBENCHMARK_DEBUG=True
    ```

## Usage

### Run the Application

To start the FastAPI application, use:

```bash
uvicorn main:app --reload
```

The app will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### API Endpoints

#### GET /results/average

**Description**: Returns the average performance statistics for all benchmarking results.

**Usage**:

```bash
curl -X GET "http://127.0.0.1:8000/results/average"
```

**Response**:

```json
{
    "average_token_count": 10.2,
    "average_time_to_first_token": 216,
    "average_time_per_output_token": 27.6,
    "average_total_generation_time": 485.2
}
```

#### GET /results/average/{start_time}/{end_time}

**Description**: Returns the average performance statistics within a specified time window.

**Parameters**:
- `start_time`: Start of the time window (ISO format, e.g., "2024-06-01T12:00:00").
- `end_time`: End of the time window (ISO format, e.g., "2024-06-02T10:00:00").

**Usage**:

```bash
curl -X GET "http://127.0.0.1:8000/results/average/2024-06-01T12:00:00/2024-06-02T10:00:00"
```

**Response**:

```json
{
    "average_token_count": 9.75,
    "average_time_to_first_token": 225,
    "average_time_per_output_token": 27.5,
    "average_total_generation_time": 477.5
}
```

## Project Structure

```plaintext
superbenchmark/
├── main.py               # Main FastAPI application
├── models.py             # Pydantic data models
├── utils.py              # Utility functions
├── test_database.json    # JSON file containing benchmarking data (used in DEBUG mode)
├── config.py             # Configuration for debug mode
├── requirements.txt      # Project dependencies
└── .env                  # Environment variables file
```

## Linting, Formatting, and Type Checking

- **Linting**: Run `flake8` to check for linting errors.
- **Formatting**: Use `black` to auto-format the code.
- **Type Checking**: Use `mypy` to enforce type hints.

```bash
flake8 .
black .
mypy .
```

## Debug Mode

The application’s debug mode can be controlled by setting the `SUPERBENCHMARK_DEBUG` environment variable:

- **Debug Mode Enabled** (`SUPERBENCHMARK_DEBUG=True`): Data will be loaded from `test_database.json`.
- **Debug Mode Disabled** (`SUPERBENCHMARK_DEBUG=False`): The application will return a 403 error, as live database functionality is not yet implemented.