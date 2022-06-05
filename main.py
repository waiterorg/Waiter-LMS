from fastapi import FastAPI
from api import users, courses, sections

app = FastAPI(
    title="WAITER LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Waiter",
        "email": "iwaiterorg@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)