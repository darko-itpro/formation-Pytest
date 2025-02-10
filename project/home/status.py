def heat_status(temperature:float) -> str:
    value = "Bon"
    if temperature > 22:
        value = "Chaud"
    elif temperature < 18:
        value = "Froid"

    return value
