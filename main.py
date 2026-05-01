import uvicorn
from fastapi import FastAPI

from myapp.ui.routes import router


app = FastAPI(title="Decentralized Lost & Found", version="0.1.0")
app.include_router(router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Dobrodošli u Decentralized Lost & Found sustav"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
