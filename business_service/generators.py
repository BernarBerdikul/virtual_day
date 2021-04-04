from virtual_day.utils import constants


def generate_list_roles() -> list:
    return [{"value": value, "label": label}
            for value, label in constants.USER_TYPES]


def generate_list_language() -> list:
    return [{"value": value, "label": label}
            for value, label in constants.TRANSLATION_LANGUAGES]
