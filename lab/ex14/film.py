from tools.toolbox import input

FRAMES_PER_SECOND = 24
SIZE_PER_FRAME_M = 0.019

lenght_hours = float(input("Wie viele ganze Stunden dauert der Film? "))
lenght_minutes = float(input("Wie viele Restminuten? "))
lenght_seconds = float(input("Wie viele Restsekunden? "))

total_lenght_seconds = (lenght_hours * 3600) + (lenght_minutes * 60) + lenght_seconds

total_frames = total_lenght_seconds * FRAMES_PER_SECOND
total_length_m = total_frames * SIZE_PER_FRAME_M

print(
    f"Der Film besteht aus {total_frames:.0f} Einzelbildern und ist damit {total_length_m:.2f} Meter lang."
)
