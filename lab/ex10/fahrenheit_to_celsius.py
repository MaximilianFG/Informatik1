def convert_c_to_f():
    """Convert a temperature from Celsius to Fahrenheit."""
    fahrenheit = 100.0
    celsius = (fahrenheit - 32) * 5 / 9
    print(
        f"{fahrenheit:.1f} degrees Fahrenheit is equal to {celsius:.1f} degrees Celsius."
    )


convert_c_to_f()
