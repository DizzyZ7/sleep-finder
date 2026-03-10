def filter_products(products, weight=None, height=None, price=None):

    result = []

    for p in products:

        if weight and p["max_weight"] < weight:
            continue

        if height and p["height"] != height:
            continue

        if price and p["price"] > price:
            continue

        result.append(p)

    return result
