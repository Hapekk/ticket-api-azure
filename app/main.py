from fastapi import FastAPI

app = FastAPI()
tickets = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tickets")
def create_ticket(title: str):
    tickets.append(title)
    return {"id": len(tickets), "title": title}

@app.get("/tickets")
def list_tickets():
    return tickets