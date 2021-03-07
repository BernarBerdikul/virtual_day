from virtual_day.utils import constants, messages

billboard_rules_response = {
        "title": {
            "rules": {
                "required": {
                    "value": True,
                    "message": messages.REQUIRED_FIELD,
                },
                "maxLength": {
                    "value": constants.TITLE_LENGTH_MAX,
                    "message": messages.TITLE_LENGTH_MAX
                },
            },
        },
    }
