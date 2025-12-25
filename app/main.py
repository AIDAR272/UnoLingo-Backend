from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.score_routes import router as score_routes
from app.api.translate_routes import router as translate_router
from app.api.auth_routes import router as auth_router


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(translate_router)
app.include_router(auth_router)
app.include_router(score_routes)

@app.get("/")
def root():
    return {"status": "OK"}
