from backend.models.nbp import NBPModel
from backend.models.uplift import UpliftModel

class DecisionEngine:
    def __init__(self):
        self.nbp = NBPModel()
        self.uplift = UpliftModel()
        
        self.campaigns = [
            {"id": "premium", "name": "Premium Service", "ltv": 15000, "cpa": 1000, "channel": "Personal Manager"},
            {"id": "credit_card", "name": "Credit Card", "ltv": 5000, "cpa": 150, "channel": "Push Notification"},
            {"id": "gas_deal", "name": "Gas Station Cashback", "ltv": 2000, "cpa": 350, "channel": "In-App Banner"}
        ]

    def select_offer(self, form_data):
        uplift_score = self.uplift.get_uplift_score(form_data)
        
        if uplift_score <= 0:
            return None, 0

        best_campaign = None
        max_ev = -float('inf')

        for camp in self.campaigns:
            p_conv = self.nbp.predict_probability(form_data, camp['id'])
            
            ev = (uplift_score * camp['ltv']) - camp['cpa']
            
            if ev > max_ev and ev > 0:
                max_ev = ev
                best_campaign = camp

        return best_campaign, max_ev