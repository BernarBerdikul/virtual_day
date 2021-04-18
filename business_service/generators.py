from virtual_day.utils import constants


def generate_class_rooms() -> list:
    return [{"value": value, "label": label}
            for value, label in constants.CLASS_ROOM]


def generate_list_roles() -> list:
    return [{"value": value, "label": label}
            for value, label in constants.USER_TYPES]


def generate_list_language() -> list:
    return [{"value": value, "label": label}
            for value, label in constants.TRANSLATION_LANGUAGES]


def generate_list_type_billboard() -> list:
    return [{"value": value, "label": label}
            for value, label in constants.BILLBOARD_TYPES]


def generate_list_unique_keys() -> list:
    return [{"value": value, "label": label}
            for value, label in constants.UNIQUE_KEY_FOR_BILLBOARD]
