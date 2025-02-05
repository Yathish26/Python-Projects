import requests
import threading

def send_post_request(url, json_data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=json_data, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print("Response:", response.json() if response.headers.get('Content-Type') == 'application/json' else response.text)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    url = "https://menuapp-server.onrender.com/api/menu-manager/menu/add-menu"  
    json_data = {"menuName": "ASNBBWIFBUFEOUFEIBUF4LIB4BI4TVI4TIVT4IUITIUTIUG3TIUT3IUT3IU", "description": "AS"}
    
    threads = []
    for _ in range(5): 
        thread = threading.Thread(target=send_post_request, args=(url, json_data))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
