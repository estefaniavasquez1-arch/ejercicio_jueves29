from fastapi import FastAPI
from google import genai

app = FastAPI()

client = genai.Client()

@app.get("/chat/{saludo}")
def read_root(saludo):
    intruccion = "rima tu respuesta siempre"
    inferencia = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=intruccion + saludo
    )
    return {"Respuesta": inferencia.output_text }
       


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}