import multiprocessing
import uvicorn
from ..api.server import app
from .monitor import monitor_mentions
import time

def run_api_server():
    """Run the FastAPI server"""
    uvicorn.run(app, host="0.0.0.0", port=8000)

def run_monitor():
    """Run the monitor with initial delay"""
    # Wait for API server to start
    time.sleep(5)
    monitor_mentions()

def run_services():
    """Run both API server and monitor"""
    # Create processes
    api_process = multiprocessing.Process(target=run_api_server)
    monitor_process = multiprocessing.Process(target=run_monitor)

    try:
        # Start processes
        print("Starting API server...")
        api_process.start()
        print("Starting monitor...")
        monitor_process.start()

        # Wait for processes
        api_process.join()
        monitor_process.join()

    except KeyboardInterrupt:
        print("\nShutting down services...")
        api_process.terminate()
        monitor_process.terminate()
        api_process.join()
        monitor_process.join()
        print("Services stopped")

if __name__ == "__main__":
    run_services() 