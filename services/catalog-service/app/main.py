from fastapi import FastAPI

app = FastAPI(title="catalog-service", docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
