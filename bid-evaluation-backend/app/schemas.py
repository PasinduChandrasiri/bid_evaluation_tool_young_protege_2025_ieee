from pydantic import BaseModel, EmailStr, condecimal
from typing import Optional
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    client = "client"
    committee = "committee"
    admin = "admin"

class BidStatus(str, Enum):
    uploaded = "uploaded"
    prelim_checked = "prelim_checked"
    detailed_evaluated = "detailed_evaluated"
    post_qualified = "post_qualified"
    selected = "selected"
    rejected = "rejected"

# User Schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: UserRole

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: UserRole

    class Config:
        orm_mode = True

# Auth
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Bid Schema
class BidBase(BaseModel):
    bidder_name: str
    price: condecimal(max_digits=15, decimal_places=2)
    bid_document_url: str

class BidCreate(BidBase):
    tender_id: int

class BidOut(BidBase):
    id: int
    status: BidStatus
    uploaded_at: datetime

    class Config:
        orm_mode = True

# Tender Schema
class TenderBase(BaseModel):
    title: str
    description: Optional[str] = None

class TenderCreate(TenderBase):
    client_id: int

class TenderOut(TenderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Evaluation Schema
class EvaluationBase(BaseModel):
    prelim_check: bool = False
    detail_score: Optional[float] = None
    post_qualification: bool = False
    evaluation_notes: Optional[str] = None

class EvaluationOut(EvaluationBase):
    id: int
    evaluated_at: datetime

    class Config:
        orm_mode = True

# Committee Vote
class CommitteeVoteBase(BaseModel):
    evaluation_id: int
    committee_member_id: int
    vote: str  # 'approve' or 'reject'
    comments: Optional[str] = None
