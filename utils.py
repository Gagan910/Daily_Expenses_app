def validate_percentage_split(percentages):
    if sum(percentages) != 100:
        raise ValueError("Percentages must add up to 100%")
