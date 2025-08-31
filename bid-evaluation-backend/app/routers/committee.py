from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from app import database, models, schemas, evaluation, letter_generator
from app.auth import get_current_active_user

router = APIRouter()

@router.get("/evaluations")
def list_evaluations(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_active_user)):
    if current_user.role != models.UserRole.committee:
        raise HTTPException(status_code=403, detail="Not authorized")
    evals = db.query(models.Evaluation).all()
    return evals

@router.post("/approve/{bid_id}")
def approve_bid(bid_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_active_user)):
    if current_user.role != models.UserRole.committee:
        raise HTTPException(status_code=403, detail="Not authorized")

    bid = db.query(models.Bid).filter(models.Bid.id == bid_id).first()
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")

    # Mark selected and generate Letter of Acceptance
    bid.status = models.BidStatus.selected
    db.commit()

    # Generate the Letter of Acceptance PDF response
    tender_title = bid.tender.title if bid.tender else "N/A"
    pdf_response = letter_generator.letter_response(bid.bidder_name, tender_title, float(bid.price))
    return pdf_response
