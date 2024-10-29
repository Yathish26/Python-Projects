import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_request(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def stress_test(url, num_requests=500):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(send_request, url) for _ in range(num_requests)]
        
        results = []
        for future in as_completed(futures):
            results.append(future.result())

    # Print summary of results
    success_count = sum(1 for result in results if result == 200)
    error_count = len(results) - success_count
    print(f"Total Requests: {num_requests}")
    print(f"Successful Responses (200): {success_count}")
    print(f"Failed Responses: {error_count}")

# Example URL to test
test_url = "https://devloprr.com/login"
stress_test(test_url)
