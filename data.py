ORDER_DATA = {
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "address": "Moscow, Lenina 1",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-09-25",
    "comment": "Test order"
}


ORDER_DATA_WITH_BLACK_COLOR = {
    **ORDER_DATA,
    "color": ["BLACK"]
}

ORDER_DATA_WITH_GREY_COLOR = {
    **ORDER_DATA,
    "color": ["GREY"]
}

ORDER_DATA_WITH_BOTH_COLORS = {
    **ORDER_DATA,
    "color": ["BLACK", "GREY"]
}

ORDER_DATA_VARIANTS = [
    ORDER_DATA_WITH_BLACK_COLOR,
    ORDER_DATA_WITH_GREY_COLOR,
    ORDER_DATA_WITH_BOTH_COLORS,
    ORDER_DATA
]