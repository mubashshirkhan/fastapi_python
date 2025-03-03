from fastapi import FastAPI
from students.students import router as student_router
app = FastAPI()

app.include_router(student_router, prefix='/students', tags=['Students'])


@app.get('/')
def read_root():
    return {'HELLO': "SERVER IS RUNNING"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
