from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


import os



from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# User modules 
from api.services.database import sqlite_file_name, create_db_and_tables
from api.services.dummy_data import create_dummy_data
from api.routers import proposal_description
from fastapi.middleware.cors import CORSMiddleware


if os.environ["ENVIRONMENT"] == "PROD":
    # create_db_and_tables()
    pass
else:
    # --------------------------------------
    # CREATING DUMMY DATABASE AND DATA
    # ADD dummy data in sqlite database (Only Dev Mode)----
    try:
        os.remove(sqlite_file_name)  # START FROM SCRATCH
        print("DB was removed")
    except:
        pass
    create_db_and_tables()
    print("Tables were created")
    create_dummy_data()
    # -------------------------------------

description = """
    This api is created to serve the neccesities 
    of the Meet Dapp as IPFS, Users and Events.
"""

app = FastAPI(
    title="GovChainBoard",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Your Name",
        "url": "http://your-website-url.com",  # Replace with your actual website URL
        "email": "your@email.com",  # Replace with your actual email
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

origins = ["*"]  # You can specify a list of allowed origins instead of "*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods if needed
    allow_headers=["*"],  # You can specify specific headers if needed
)

 
@app.get("/", summary="Root Redirect", description="Redirect to ReDoc Documentation")
async def root_redirect(): return RedirectResponse("/docs")

# ROUTERS
app.include_router(proposal_description.router)

