from sqlalchemy.orm import Session
from app import models

def preliminary_check(bid: models.Bid, db: Session):
    """
    Preliminary check: For demo, we mark prelim_check as True all bids for simplicity.
    Real logic would involve verifying document validity, signatures, securities, etc.
    """
    eval_obj = db.query(models.Evaluation).filter(models.Evaluation.bid_id == bid.id).first()
    if not eval_obj:
        eval_obj = models.Evaluation(bid_id=bid.id)
    eval_obj.prelim_check = True
    bid.status = models.BidStatus.prelim_checked
    db.add(eval_obj)
    db.commit()
    db.refresh(eval_obj)
    return eval_obj

def detailed_evaluation(bid: models.Bid, db: Session):
    """
    Detailed evaluation: simplistic scoring - lower price gets better score (example only).
    """
    eval_obj = db.query(models.Evaluation).filter(models.Evaluation.bid_id == bid.id).first()
    if not eval_obj or not eval_obj.prelim_check:
        return None
    # Simple score inversely proportional to price -- placeholder logic
    score = 100000 / bid.price if bid.price else 0
    eval_obj.detail_score = score
    bid.status = models.BidStatus.detailed_evaluated
    db.add(eval_obj)
    db.commit()
    db.refresh(eval_obj)
    return eval_obj

def post_qualification(bid: models.Bid, db: Session):
    """
    Post qualification: dummy accepting all for demo.
    """
    eval_obj = db.query(models.Evaluation).filter(models.Evaluation.bid_id == bid.id).first()
    if not eval_obj or not eval_obj.detail_score:
        return None
    eval_obj.post_qualification = True
    bid.status = models.BidStatus.post_qualified
    db.add(eval_obj)
    db.commit()
    db.refresh(eval_obj)
    return eval_obj
