# Przykładowy test logiki biznesowej (bez HTTP)

def multiply_by_two(number: int) -> int:
    # Prosta funkcja pomocnicza do pokazania testu jednostkowego
    return number * 2


def test_multiply_by_two():
    assert multiply_by_two(2) == 4
    assert multiply_by_two(0) == 0
    assert multiply_by_two(-3) == -6
