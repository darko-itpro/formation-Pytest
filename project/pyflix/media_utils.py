def is_viewed(media:dict):
    viewed = int(media['viewed'])
    if viewed < 0:
        raise ValueError(f"Unexpected viewed: {viewed}")

    return bool(viewed)