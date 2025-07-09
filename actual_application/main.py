from fastapi import FastAPI, Request
from web import explorer, creature, user
from fastapi.middleware.cors import CORSMiddleware
# import service
app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)


# CORS

app.add_middleware(CORSMiddleware, allow_origins=["https://google.com"], 
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

