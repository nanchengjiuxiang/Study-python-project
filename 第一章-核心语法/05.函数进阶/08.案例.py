"""
定义一个函数,用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
具体规则如下:
    1. 优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价。
    2. 积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣)
"""

def cala_order_cost(*args, coupon=0.0, score=0.0, express=0.0):
    """
    用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额
    :param args: 商品信息(商品名、价格、数量)
    :param coupon: 优惠券
    :param score: 积分抵扣
    :param express: 运费信息
    :return: 订单的总金额
    """
    # 总金额 = 商品价格 - 优惠卷 - 积分抵扣 + 运费

    # 计算商品价格
    prise = [goods[1] * goods[2] for goods in args ]
    total_prise = sum(prise)

    # 扣减优惠卷
    if coupon >= 5000 & coupon <= total_prise:
        total_prise -= coupon

    # 扣减积分抵扣
    if total_prise >= 5000 & (score // 100) <= total_prise:
        total_prise -= score // 100

    # 添加运费
    total_prise += express
    return total_prise

# 调用函数
cost = cala_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 4999, 1), coupon=500, score=9000, express=19.9)
print(f"商品价格为 {cost}")