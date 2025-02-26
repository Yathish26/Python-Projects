import psutil
import time

def get_speed():
    old_data = psutil.net_io_counters()
    time.sleep(0.5)
    new_data = psutil.net_io_counters()
    
    download_speed = (new_data.bytes_recv - old_data.bytes_recv) / 1024  # in KB/s
    upload_speed = (new_data.bytes_sent - old_data.bytes_sent) / 1024  # in KB/s
    
    return download_speed, upload_speed

if __name__ == "__main__":
    print("Monitoring Internet Speed... Press Ctrl+C to stop.")
    try:
        while True:
            download, upload = get_speed()
            print(f"Download Speed: {download:.2f} KB/s | Upload Speed: {upload:.2f} KB/s", end="\r", flush=True)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
