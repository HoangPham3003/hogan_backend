from fastapi import FastAPI

from .config import Settings
from .services.networks.connection import connect_networks


settings = Settings()

    
app = FastAPI(
    title="Hogan API with documentation",
    description="This is Hogan's website.",
)

from .routers import page_home

app = connect_networks(app)
app.include_router(page_home.router)