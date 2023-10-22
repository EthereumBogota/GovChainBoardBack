'''
Classes containing the shape of the data f
'''

from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from datetime import datetime
from enum import Enum

# 'User' Classes -----------------------------
# class ProposalDescription(SQLModel, table=True):
#     contract_id: str = Field(primary_key=True, max_length=50)
#     proposal_id: str = Field(max_length=20)
#     description: Optional[str] = Field(default=None, max_length=50)
#     categories: Optional[bool] = Field(default=False)


class IndexDataBasin(SQLModel, table=True):
    cid: str = Field(primary_key=True, max_length=50)
    contract_id:  str = Field(max_length=30)

    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)

