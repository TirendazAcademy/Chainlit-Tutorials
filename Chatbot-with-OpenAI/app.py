from dotenv import load_dotenv
import chainlit as cl 
from openai import AsyncOpenAI

load_dotenv()

client = AsyncOpenAI()

cl.instrument_openai()

@cl.on_message 
async def on_message(message: cl.Message):

    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":"system",
                "content": "You are a helpful assistant."
            },
            {
                "role":"user",
                "content": message.content,
            }
        ]
    )
    
    await cl.Message(
        content=response.choices[0].message.content
    ).send()