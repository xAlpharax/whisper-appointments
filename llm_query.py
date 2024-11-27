#!/usr/bin/env python3

##############################################################################

from dotenv import load_dotenv
import os

load_dotenv()
LLM_API_URL = str(os.getenv("LLM_API_URL"))
JWT = str(os.getenv("JWT"))
HEADERS = { "Authorization": "Bearer " + JWT }

import aiohttp

async def query(payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(LLM_API_URL, headers=HEADERS, json=payload) as response:
            return await response.json()

##############################################################################

if __name__ == "__main__":

    import asyncio

    async def main():
        output = await query({
            "question": "Salut, clinica Dentix?",
            "chatId": "69420",
        })
        return output

    print(asyncio.run(main()))
