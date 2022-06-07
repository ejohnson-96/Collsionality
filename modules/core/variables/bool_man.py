
def valid_bool(
        a,
        b,
):
    if isinstance(a, bool) and isinstance(b, bool):
        return a, b
    else:
        raise ValueError(
            "Error: Only boolean arguments are allowed,"
            f" instead for a, got type {type(a)} and for "
            f"b got type {type(b)}."
        )


def _and(
        a,
        b,
):
    a, b = valid_bool(a, b)

    if a == 1 and b == 1:
        return True
    else:
        return False


def _nand(
        a,
        b,
):
    a, b = valid_bool(a, b)

    if a == 1 and b == 1:
        return False
    else:
        return True


def _or(
        a,
        b,
):
    a, b = valid_bool(a, b)

    if a == 1 or b == 1:
        return True
    else:
        return False


def _xor(
        a,
        b,
):
    a, b = valid_bool(a, b)

    if a != b:
        return True
    else:
        return False


def _not(
        a,
):
    if not isinstance(a, bool):
        raise TypeError(
            f"Error: Only boolean values allowed, instead"
            f" got argument of type {type(a)}."
        )

    return not a


def _nor(
        a,
        b,
):
    a, b = valid_bool(a, b)

    if (a == 0) and (b == 0):
        return True
    elif (a == 0) and (b == 1):
        return False
    elif (a == 1) and (b == 1):
        return False
    elif (a == 1) and (b == 1):
        return True
    else:
        raise ValueError(
            f"Error: Logic cannot be determined, arguments passed are {a}"
            f" and {b} of types {type(a)} and {type(b)} respectively."
        )


def _xnor(
        a,
        b,
):
    a, b = valid_bool(a, b)

    if (a == b):
        return True
    else:
        return False
