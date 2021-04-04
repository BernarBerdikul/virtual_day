from virtual_day.utils import constants


def generate_list_roles() -> list:
    return [{"value": value, "label": label}
            for value, label in constants.USER_TYPES]
