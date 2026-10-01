from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.emp_routers import router as emp_router
from routers.dept_router import router as dept_router
from routers.role_router import router as role_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(emp_router)
app.include_router(dept_router)
app.include_router(role_router)


@app.get("/")
def home():
    return {"message": "Employee CRUD API is Running!"}