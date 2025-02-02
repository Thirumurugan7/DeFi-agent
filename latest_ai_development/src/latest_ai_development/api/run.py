import uvicorn

def run_server():
    uvicorn.run("latest_ai_development.api.server:app", 
                host="0.0.0.0", 
                port=8000, 
                reload=True)

if __name__ == "__main__":
    run_server() 