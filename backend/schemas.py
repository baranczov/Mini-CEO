from pydantic import BaseModel
from typing import Optional

class ClientForm(BaseModel):
    name: str
    income: int
    is_loyal: bool
    churn_score: float
    gas_avg_check: int
    has_debit_card: bool
    has_credit_card: bool

class OfferResponse(BaseModel):
    offer_found: bool
    product_name: Optional[str] = None
    channel: Optional[str] = None
    expected_value: Optional[float] = None