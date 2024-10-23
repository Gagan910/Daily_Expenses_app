def equal_split(amount, participants):
    return {participant: amount / len(participants) for participant in participants}

def exact_split(amounts, participants):
    return {participants[i]: amounts[i] for i in range(len(participants))}

def percentage_split(amount, percentages, participants):
    return {participants[i]: (amount * percentages[i] / 100) for i in range(len(participants))}
