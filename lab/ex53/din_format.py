DIN_A0 = [841, 1189]


def din_a_format_iterative(size: int):
    s1 = DIN_A0[0]
    s2 = DIN_A0[1]
    for a in range(1, size + 1):
        if s1 > s2:
            s1 = s1 * 0.5
            wanted_size = [s1, s2]
        else:
            s2 = s2 * 0.5
            wanted_size = [s2, s1]
    return wanted_size


def din_a_format_recursive(size: int, s1: float = DIN_A0[0], s2: float = DIN_A0[1]):
    if size == 0:
        return [min(s1, s2), max(s1, s2)]

    if s1 > s2:
        s1 /= 2
    else:
        s2 /= 2

    return din_a_format_recursive(size - 1, s1, s2)


print(din_a_format_recursive(2))
