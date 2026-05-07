class NBPModel:
    def predict_probability(self, form_data, product_id):
        if product_id == "premium":
            if form_data.income > 150000:
                return 0.85
            return 0.05
            
        if product_id == "gas_deal":
            if form_data.gas_avg_check > 500:
                return 0.9
            return 0.2
            
        if product_id == "credit_card":
            if form_data.has_debit_card and not form_data.has_credit_card:
                return 0.7
            return 0.3
            
        return 0.1