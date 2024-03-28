class WebPush():
    def __init__(self, platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.opt_in = opt_in
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        return "Push gönderildi!"


class TriggerPush(WebPush):
    def __init__(self, trigger_page, platform, opt_in, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page

    def send_push(self):
        return "Trigger " + super().send_push()


class BulkPush(WebPush):
    def __init__(self, send_date, platform, opt_in, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date

    def send_push(self):
        return "Bulk " + super().send_push()


class SegmentPush(WebPush):
    def __init__(self, segment_name, platform, opt_in, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name

    def send_push(self):
        return "Segment " + super().send_push()


class PriceAlertPush(WebPush):
    def __init__(self, price_info, discount_rate, platform, opt_in, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    def send_push(self):
        return "Price Alert " + super().send_push()

    def discountPrice(self):
        return self.price_info - (self.price_info * self.discount_rate)


class InStockPush(WebPush):
    def __init__(self, stock_info, platform, opt_in, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, opt_in, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def send_push(self):
        return "In Stock " + super().send_push()

    def stockUpdate(self):
        if self.stock_info:
            return False
        else:
            return True


triggerPush = TriggerPush("product", "web", True, "5",
                          "20/10/2024", "20/10/2028", "tr_TR", "Trigger")
print(triggerPush.send_push())

bulkPush = BulkPush(2024, "mobile", True, "2", "20/10/2024",
                    "20/10/2028", "tr_TR", "Bulk")
print(bulkPush.send_push())

segmentPush = SegmentPush("single", "web", True, "4",
                          "20/10/2028", "20/10/2029", "tr_TR", "Segment")
print(segmentPush.send_push())

priceAlertPush = PriceAlertPush(303, 20.5, "mobile", False, "8",
                                "2/1/2024", "20/10/2024", "tr_TR", "Price Alert")
print(priceAlertPush.send_push())

inStockPush = InStockPush(True, "web", True, "1",
                          "2/1/2023", "2/1/2025", "tr_TR", "In Stock")
print(inStockPush.send_push())
