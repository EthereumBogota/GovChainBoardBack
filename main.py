import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

json1 =