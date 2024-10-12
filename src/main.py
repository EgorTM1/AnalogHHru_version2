from fastapi import FastAPI
from api.router import all_routers
import uvicorn


app = FastAPI(
    title='Analog HH.ru'
)

for router in all_routers:
    app.include_router(router)



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
    