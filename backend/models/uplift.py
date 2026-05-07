class UpliftModel:
    def get_uplift_score(self, form_data):
        if form_data.churn_score > 0.75:
            return -0.5
            
        if form_data.is_loyal and form_data.income > 120000:
            return 0.02
            
        if form_data.has_debit_card and not form_data.has_credit_card:
            return 0.18
            
        return 0.07