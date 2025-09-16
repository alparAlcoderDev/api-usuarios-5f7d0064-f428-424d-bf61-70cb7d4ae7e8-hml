from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from adapters.http import auth_controller, item_controller

app = FastAPI(
    title="API Clean Architecture",
    description="API gerada com Clean Architecture",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_controller.router)
app.include_router(item_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)