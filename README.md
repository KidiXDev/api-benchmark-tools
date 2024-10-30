# Backend Benchmarking Tool

This repository contains two Python scripts designed to benchmark the performance of a backend API endpoint. The scripts use multithreading to send multiple requests in parallel and measure the response times.

## Files

- `app.py`: Sends authenticated requests to the API endpoint using a bearer token.
- `no-auth.py`: Sends unauthenticated requests to the API endpoint.

## Requirements

- Python 3.x
- `requests` library

You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage

### app.py

This script sends authenticated requests to the API endpoint.

1. Replace `YOUR_BEARER_TOKEN` with your actual bearer token.
2. Run the script:

```bash
python app.py
```

### no-auth.py

This script sends unauthenticated requests to the API endpoint.

1. Run the script:

```bash
python no-auth.py
```

## Configuration

Both scripts can be configured by modifying the following variables:

- `thread_count`: Number of threads running in parallel.
- `request_per_thread`: Number of requests per thread.
- `delay_between_requests`: Delay between requests (in seconds).

Example:

```python
thread_count = 8  # Number of threads running in parallel
request_per_thread = 5  # Number of requests per thread
delay_between_requests = 0.05  # Delay between requests (in seconds)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
