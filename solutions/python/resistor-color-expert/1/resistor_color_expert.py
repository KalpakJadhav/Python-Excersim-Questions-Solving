
COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

TOLERANCES = {
    "grey": "0.05",
    "violet": "0.1",
    "blue": "0.25",
    "green": "0.5",
    "brown": "1",
    "red": "2",
    "gold": "5",
    "silver": "10"
}


def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        digits = COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])
        multiplier = COLORS.index(colors[2])
        tolerance = TOLERANCES[colors[3]]
    else:
        digits = (
            COLORS.index(colors[0]) * 100
            + COLORS.index(colors[1]) * 10
            + COLORS.index(colors[2])
        )
        multiplier = COLORS.index(colors[3])
        tolerance = TOLERANCES[colors[4]]

    resistance = digits * (10 ** multiplier)

    if resistance >= 1_000_000:
        value = resistance / 1_000_000
        unit = "megaohms"
    elif resistance >= 1_000:
        value = resistance / 1_000
        unit = "kiloohms"
    else:
        value = resistance
        unit = "ohms"
        
    if isinstance(value, float):
        value = f"{value:g}"

    return f"{value} {unit} ±{tolerance}%"

