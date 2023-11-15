from fastapi import FastAPI

from routers import router

app = FastAPI()
app.include_router(router=router)


@app.get("/health-check")
def health_check():
    return {"pai": "On"}
