import json
import uvicorn
import call_functions_scroll as cfs
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/proposals/")
async def proposals():
    with open("json_data/proposals.json", "r") as archivo:
        data = archivo.read()
        proposals_dict = json.loads(data)

        json_output = jsonable_encoder(str(proposals_dict))

        return JSONResponse(content=json_output)


@app.get("/votes_result/")
async def votes_result():
    with open("json_data/votes_result.json", "r") as archivo:
        data = archivo.read()
        votes_result_dict = json.loads(data)

        json_output = jsonable_encoder(str(votes_result_dict))

        return JSONResponse(content=json_output)


@app.get("/participant_data/")
async def participant_data():
    with open("json_data/participant_data.json", "r") as archivo:
        data = archivo.read()
        participant_data_dict = json.loads(data)

        json_output = jsonable_encoder(str(participant_data_dict))

        return JSONResponse(content=json_output)


@app.get("/call_token/")
async def call_token():
    cfs_obj = cfs.ScrollCalls()

    transactions = cfs_obj.call_token()

    json_output = jsonable_encoder(str(transactions))

    return JSONResponse(content=json_output)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8088)
