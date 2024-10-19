class DiscountRate:

    def __init__(self, customer):
        self.customer = customer

    service_discount_premium = 0.2
    service_discount_gold = 0.15
    service_discount_silver = 0.1
    product_discount_premium = 0.1
    product_discount_gold = 0.1
    product_discount_silver = 0.1


    def get_servive_discount_rate(self,type):
        if type=="premium":
            return self.service_discount_premium
        elif type=="gold":
            return self.service_discount_gold
        elif type=="silver":
            return self.service_discount_silver

    def get_product_discount_rate(self,type):
        if type=="premium":
            return self.product_discount_premium
        elif type=="gold":
            return self.product_discount_gold
        elif type=="silver":
            return self.product_discount_silver

    def set_service_discount_rate(self,type,rate):
        if type=="premium":
            self.service_discount_premium = rate
        elif type=="gold":
            self.service_discount_gold = rate
        elif type=="silver":
            self.service_discount_silver = rate
