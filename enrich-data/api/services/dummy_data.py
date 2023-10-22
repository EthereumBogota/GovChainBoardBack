from sqlmodel import Session
from api.services.database import engine
from api.models.models import IndexDataBasin #, Group


def create_dummy_data():
    
    session = Session(engine)

    data_1 = IndexDataBasin(cid="0xdsfsadf4aDc123", contract_id="Alice.eth")
    data_2 = IndexDataBasin(cid="0xdsfsadf4aDddddc123", contract_id="Alic3e.eth")
    data_3 = IndexDataBasin(cid="0xdsfsadf4aDcfffff123", contract_id="Alic34e.eth")

    session.add(data_1)
    session.add(data_2)
    session.add(data_3)

    session.commit()


    print("Dummy Data was added")
    