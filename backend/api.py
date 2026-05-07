from fastapi import APIRouter
from backend.schemas import ClientForm, OfferResponse
from backend.engine import DecisionEngine

router = APIRouter()
engine = DecisionEngine()

@router.post("/predict", response_model=OfferResponse)
def predict_offer(form: ClientForm):
    best_campaign, ev = engine.select_offer(form)

    if not best_campaign:
        return OfferResponse(offer_found=False)

    return OfferResponse(
        offer_found=True,
        product_name=best_campaign['name'],
        channel=best_campaign['channel'],
        expected_value=round(ev, 2)
    )