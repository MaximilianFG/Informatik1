def calculateAudience(initialAudience: int, playingTime: int, rate) -> int:
    if playingTime == 0:
        return initialAudience

    previousAudience = calculateAudience(initialAudience, playingTime - 1, rate)

    return previousAudience * (1 - (rate / 100))


print(calculateAudience(1000, 0, 10))
print(calculateAudience(1000, 1, 10))
