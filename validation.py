def validate_name(name):
    return bool(name.strip())


def validate_stress(stress):
    return 1 <= stress <= 10


def validate_energy(energy):
    return 1 <= energy <= 10