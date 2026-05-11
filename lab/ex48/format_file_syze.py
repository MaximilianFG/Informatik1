def format_file_size(size: int, use_binary):
    if use_binary:
        units = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]
        step = 1024
    else:
        units = ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
        step = 1000

    value = float(size)
    unit_index = 0

    while unit_index < len(units) - 1 and value >= step:
        value /= step
        unit_index += 1

    print(f"{value:.2f} {units[unit_index]}")


format_file_size(100000000, False)
