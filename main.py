import fastapi

router = fastapi.APIRouter(prefix='/api')


@router.get('/problem/{id_}')
def get_problem(id_: int):
    return {'Problem number': id_}


@router.get('/problems')
def get_problems():
    problems = [{'Problem number 1': 'Error'}, {'Problem number 2': 'Connection error'},
                {'Problem number 3': 'Data error'}]
    return problems


@router.get('/create_problem_status')
def create_problem():
    return {'status': 'Successfully!'}


@router.get('/reason_error')
def reason_error():
    reason = [{'Problem 1': 'Error in import'}, {'Problem 2': 'Internet connection interrupted'},
              {'Problem 3': 'drive problems'}]
    return reason


app = fastapi.FastAPI()
app.include_router(router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, port=1026)
