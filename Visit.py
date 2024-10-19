from dis import disco

from Customer import Customer
import datetime

from DiscountRate import DiscountRate



class Visit:


    def __init__(self,customer,datetime):
        self.customer = customer
        self.datetime = datetime

    def get_customer(self):
        return self.customer


    service_expense=0.0
    product_expense=0.0

    def get_service_expense(self):
        return self.service_expense

    def get_product_expense(self):
        return self.product_expense

    def set_service_expense(self,price):
        self.service_expense=price

    def set_product_expense(self,price):
        self.product_expense=price

    def get_total_expense(self,x,y):
        discount=DiscountRate(self.get_customer())
        if (self.get_customer()).get_member_type()=="premium":
            return (1-discount.get_product_discount_rate("premium"))*x*self.product_expense+(1-discount.get_servive_discount_rate("premium"))*y*self.service_expense
        elif (self.get_customer()).get_member_type()=="gold":
            return (1-discount.get_product_discount_rate("gold"))*x*self.product_expense+(1-discount.get_servive_discount_rate("gold"))*y*self.service_expense
        elif (self.get_customer()).get_member_type()=="silver":
            return (1-discount.get_product_discount_rate("silver"))*x*self.product_expense+(1-discount.get_servive_discount_rate("silver"))*y*self.service_expense







    def __str__(self):
        return str(self.customer)+" "+str(self.datetime)+" "+"%s"%self.service_expense+" "+"%s"%self.product_expense