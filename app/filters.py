def apply_filters(data, price=None, height=None, weight=None):

    result = []

    for p in data:

        if price and int(p["price"].replace(" ","")) > price:
            continue

        if height and p["height"] != height:
            continue

        if weight and p["max_weight"] < weight:
            continue

        result.append(p)

    return result
