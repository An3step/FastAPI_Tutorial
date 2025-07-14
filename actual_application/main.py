from fastapi import FastAPI, Request, Query, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from web import explorer, creature, user, game
from fastapi.middleware.cors import CORSMiddleware
from typing import AsyncGenerator, Generator
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import asyncio
# import service
app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)
app.include_router(game.router)

# # CORS

app.add_middleware(CORSMiddleware, allow_origins=["http://127.0.0.1:8000"], 
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig

# model_name = 'google/flan-t5-base'

# tokenizer = AutoTokenizer.from_pretrained(model_name)

# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# config = GenerationConfig(max_new_tokens=200)

# @app.get('/ai')
# def prompt(line: str = Query(..., description="Текст для обработки")) -> str:
#     tokens = tokenizer(line, return_tensors='pt')
#     outputs = model.generate(**tokens, generation_config=config)
#     result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
#     return result[0]

@app.post('/small_file')
async def upload_small_file(file : bytes = File()) -> str:
    return f'file size {len(file)}'

@app.post('/big_file')
async def upload_big_file(file: UploadFile) -> str:
    return f'file size: {file.size}, name {file.filename}'

@app.get('/small_file/{name}')
async def dowmload_small_file(name: str):
    return FileResponse(name)

async def gen_file(path: str) -> AsyncGenerator[str, None]:
    """Асинхронно читает файл построчно"""
    with open(path, mode='r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            await asyncio.sleep(0.1)  # Имитация обработки
            yield line

@app.get('/big_file/{name}')
async def download_big_file(name: str):
    """Стримит содержимое файла клиенту"""
    try:
        file_gen = gen_file(name)
        return StreamingResponse(
            content=file_gen,
            media_type="text/plain",
            headers={"Content-Disposition": f"attachment; filename={name}"}
        )
    except FileNotFoundError:
        return {"error": "File not found"}, 404
    

top = Path(__file__).resolve().parent

# app.mount('/template', StaticFiles(directory=f'{top}/template', html=True), name='static')

app.mount("/static", StaticFiles(directory="static"), name="static")