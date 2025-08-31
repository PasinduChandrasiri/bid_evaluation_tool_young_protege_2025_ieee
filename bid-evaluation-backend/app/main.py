from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, bids, committee

app = FastAPI(title="Bid Evaluation API")

# Allow CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # To restrict to your frontend domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(bids.router, prefix="/bids", tags=["bids"])
app.include_router(committee.router, prefix="/committee", tags=["committee"])


@app.get("/")
async def root():
    return {"message": "Welcome to Automated Bid Evaluation API"}
