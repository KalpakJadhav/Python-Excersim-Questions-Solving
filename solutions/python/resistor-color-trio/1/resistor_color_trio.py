
COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def label(colors):
    first = COLORS.index(colors[0])
    second = COLORS.index(colors[1])
    third = COLORS.index(colors[2])

    value = (first * 10 + second) * (10 ** third)

    if value >= 1_000_000_000:
        return f"{value // 1_000_000_000} gigaohms"
    elif value >= 1_000_000:
        return f"{value // 1_000_000} megaohms"
    elif value >= 1_000:
        return f"{value // 1_000} kiloohms"
    else:
        return f"{value} ohms"

