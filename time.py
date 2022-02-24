def format_duration(seconds):
    times = [("yr", 365 * 24 * 60 * 60), 
            ("day", 24 * 60 * 60),
            ("hr", 60 * 60),
            ("min", 60),
            ("sec", 1)]
    if not seconds:
        return "now"

    time = []
    for i, j in times:
        qty = seconds // j
        if qty:
            if qty > 1:
                i += "s"
            time.append(str(qty) + " " + i)
        seconds = seconds % j
    return ' '.join(time)
