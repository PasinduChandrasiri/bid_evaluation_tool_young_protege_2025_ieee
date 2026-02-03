from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Form
from sqlalchemy.orm import Session
from app import database, models, schemas, firebase_client, evaluation
from typing import List

router = APIRouter()

@router.post("/upload", response_model=schemas.BidOut)
async def upload_bid(
    tender_id: int = Form(...),
    bidder_name: str = Form(...),
    price: float = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(database.get_db)
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Bid document is required")
    if price <= 0:
        raise HTTPException(status_code=400, detail="Bid price must be greater than zero")
    tender = db.query(models.Tender).filter(models.Tender.id == tender_id).first()
    if not tender:
        raise HTTPException(status_code=404, detail="Tender not found")
    # Upload file to Firebase Storage
    destination_path = f"bid_documents/{tender_id}_{bidder_name}_{file.filename}"
    url = firebase_client.upload_file_to_firebase(file.file, destination_path)

    # Save bid record to DB
    bid = models.Bid(
        tender_id=tender_id,
        bidder_name=bidder_name,
        price=price,
        bid_document=url,
        status=models.BidStatus.uploaded,
    )
    db.add(bid)
    db.commit()
    db.refresh(bid)

    # Run preliminary evaluation check - automate based on business logic
    evaluation.preliminary_check(bid, db)

    return bid

@router.get("/{bid_id}", response_model=schemas.BidOut)
def get_bid(bid_id: int, db: Session = Depends(database.get_db)):
    bid = db.query(models.Bid).filter(models.Bid.id == bid_id).first()
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    return bid

@router.get("/tender/{tender_id}", response_model=List[schemas.BidOut])
def list_bids_for_tender(tender_id: int, db: Session = Depends(database.get_db)):
    bids = db.query(models.Bid).filter(models.Bid.tender_id == tender_id).all()
    return bids
