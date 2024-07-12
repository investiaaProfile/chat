from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from rasa.core.agent import Agent
from rasa.core.channels.channel import CollectingOutputChannel
import httpx
from starlette.responses import RedirectResponse

# Initialize your Rasa Agent
agent = Agent.load("./models/20240713-024127-active-hull.tar.gz")

# Initialize FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/favicon.ico")
async def get_favicon():
    # You can redirect to a URL or return the icon file here
    return RedirectResponse(url='/static/favicon.ico')

# Define a model for incoming user messages
class UserMessage(BaseModel):
    message: str

# URL of your Rasa server
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

# Endpoint to send user messages to Rasa
@app.post("/send_message")
async def send_message(user_message: UserMessage):
    async with httpx.AsyncClient() as client:
        try:
            # Send user message to Rasa
            response = await client.post(RASA_SERVER_URL, json={"message": user_message.message})
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))

# Define an endpoint to handle messages using Rasa directly
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("message")
    if not message:
        raise HTTPException(status_code=400, detail="Message field is required")

    # Send the message to Rasa and get the response
    responses = await agent.handle_text(message)
    if responses:
        response_text = responses[0]["text"]
    else:
        response_text = "Sorry, I didn't understand that."

    return {"message": response_text}

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
