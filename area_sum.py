def area_sum(rectangles):
    sum_areas = 0

    for rectangle in rectangles:
        area = 0

        area = rectangle["height"] * rectangle["width"]
        sum_areas += area

    return sum_areas
