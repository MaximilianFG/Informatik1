from tools.toolbox import input

audio_length_seconds = int(input("Enter the length of the audio in seconds: "))
sample_rate_hz = int(input("Enter the sample rate of the audio in Hz: "))
bits_per_sample = int(input("Enter the number of bits per sample: "))
total_bits = audio_length_seconds * sample_rate_hz * bits_per_sample
total_mb = total_bits / (8 * 1000 * 1000)
total_mib = total_bits / (8 * 1024 * 1024)

print(
    f"The memory required for an audio of {audio_length_seconds} seconds at {sample_rate_hz} Hz with {bits_per_sample} bits per sample is {total_mb:.2f} MB or {total_mib:.2f} MiB."
)
