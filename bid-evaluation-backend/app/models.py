from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DECIMAL, Boolean, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from datetime import datetime

class UserRole(enum.Enum):
    client = "client"
    committee = "committee"
    admin = "admin"

class BidStatus(enum.Enum):
    uploaded = "uploaded"
    prelim_checked = "prelim_checked"
    detailed_evaluated = "detailed_evaluated"
    post_qualified = "post_qualified"
    selected = "selected"
    rejected = "rejected"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    tenders = relationship("Tender", back_populates="client")
    committee_votes = relationship("CommitteeVote", back_populates="committee_member")

class Tender(Base):
    __tablename__ = 'tenders'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    client_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    client = relationship("User", back_populates="tenders")
    bids = relationship("Bid", back_populates="tender")

class Bid(Base):
    __tablename__ = 'bids'

    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey("tenders.id"), nullable=False)
    bidder_name = Column(String(255), nullable=False)
    bid_document = Column(String(255), nullable=False)  # Firebase Storage URL
    price = Column(DECIMAL(15,2), nullable=False)
    status = Column(Enum(BidStatus), default=BidStatus.uploaded)
    uploaded_at = Column(TIMESTAMP, default=datetime.utcnow)

    tender = relationship("Tender", back_populates="bids")
    evaluation = relationship("Evaluation", uselist=False, back_populates="bid")

class Evaluation(Base):
    __tablename__ = 'evaluations'

    id = Column(Integer, primary_key=True, index=True)
    bid_id = Column(Integer, ForeignKey("bids.id"), nullable=False)
    prelim_check = Column(Boolean, default=False)
    detail_score = Column(DECIMAL(10,2), nullable=True)
    post_qualification = Column(Boolean, default=False)
    evaluation_notes = Column(Text, nullable=True)
    evaluated_at = Column(TIMESTAMP, default=datetime.utcnow)

    bid = relationship("Bid", back_populates="evaluation")
    committee_votes = relationship("CommitteeVote", back_populates="evaluation")

class CommitteeVote(Base):
    __tablename__ = 'committee_votes'

    id = Column(Integer, primary_key=True, index=True)
    evaluation_id = Column(Integer, ForeignKey("evaluations.id"), nullable=False)
    committee_member_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    vote = Column(Enum("approve", "reject", name="vote_enum"), nullable=False)
    comments = Column(Text, nullable=True)
    voted_at = Column(TIMESTAMP, default=datetime.utcnow)

    evaluation = relationship("Evaluation", back_populates="committee_votes")
    committee_member = relationship("User", back_populates="committee_votes")
