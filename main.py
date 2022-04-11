class WebPush:
    start_date = ""
    global_frequency_capping = ""
    end_date = ""
    language = ""
    push_type = ""
    optin = False

    def send_push(self):
        print("Push Gönderildi")

class TriggerPush(WebPush):
    def __init__(self):
        self.trigger_page = ""

class BulkPush(WebPush):
    def __init__(self):
        self.send_date = 0

class SegmentPush(WebPush):
    def __init__(self):
        self.segment_name = ""

class PriceAlertPush(WebPush):
    def __init__(self):
        self.price_info = 0
        self.discount_rate = 0.0

    def discountPrice(self,price_info,discount_rate):

        if (isinstance(price_info,float) or isinstance(price_info,int)) and (isinstance(discount_rate,int) or isinstance(discount_rate,float)):
            if (discount_rate < 100 and discount_rate > 0):
                discounted_rate = price_info * (100 - discount_rate) / 100
                print(discounted_rate)
                return discounted_rate
            else:
                print("İndirim değeri 99 dan büyük veya 1 den küçük olamaz.")
        else:
            print("Değeleri sayı olarak giriniz.")

class InstockPush(WebPush):
    def __init__(self):
        self.stock_info = False

    def stockUpdate(self):
        self.stock_info = not(self.stock_info)
        print(self.stock_info)
        return self.stock_info

web_push = WebPush()
web_push.send_push()

price_push = PriceAlertPush()
price_push.discountPrice(1000,15)

ınstock_push = InstockPush()
ınstock_push.stockUpdate()

trigger_push = TriggerPush()

bulk_push = BulkPush()

segment_push = SegmentPush()
