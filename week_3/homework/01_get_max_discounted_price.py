shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


max_sale = 0
def get_max_discounted_price(prices, coupons):
    global max_sale

    if len(prices) == 0:
        return max_sale
    if len(coupons) == 0:
        max_sale = max_sale + sum(prices)
        return max_sale

    prices.sort()
    coupons.sort()

    max_sale = max_sale + prices.pop() * ((100-coupons.pop())/100)

    print(prices)

    return get_max_discounted_price(prices, coupons)




print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.