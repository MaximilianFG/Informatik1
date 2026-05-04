frames = 0
while frames < 172800:
    hours = frames // 86400
    minutes = (frames % 86400) // 1440
    seconds = (frames % 1440) // 24
    frame = frames % 24
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}:{frame:02d}")
    frames += 1
