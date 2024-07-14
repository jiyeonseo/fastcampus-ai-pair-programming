import os
from app.core.config import settings
from fastapi import APIRouter
from typing import List

from openai import OpenAI

router = APIRouter()
client = OpenAI(api_key=settings.open_ai_api_key)

@router.get("/")
def chat(user_input: str):
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=settings.assistant_id
    )

    import time
  
    while run.status in ['queued', 'in_progress', 'cancelling']:
        time.sleep(1) # Wait for 1 second
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
    )
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        print(messages)
        return messages.data[0].content[0].text.value
    else:
        print(run.status)

    return "No response yet."
