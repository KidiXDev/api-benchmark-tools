import requests
import threading
import time

# Endpoint API and token used
url = "https://api.example.com/v1/endpoint"
bearer_token = "YOUR_BEARER_TOKEN"


def send_request():
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        print(
            f"Status Code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def benchmark_request(thread_count, request_per_thread, delay_between_requests):
    def worker():
        for _ in range(request_per_thread):
            send_request()
            time.sleep(delay_between_requests)  # Delay time between requests

    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()


if __name__ == "__main__":
    thread_count = 8  # Number of threads running in parallel
    request_per_thread = 5  # Number of requests per thread
    delay_between_requests = 0.05  # Delay between requests (in seconds)

    print("Benchmarking started...")
    benchmark_request(thread_count, request_per_thread, delay_between_requests)
    print("Benchmarking finished!")
