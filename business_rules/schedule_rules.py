from virtual_day.utils import constants, messages

""" Rules for front forms """

schedule_rules_response = {
    "event": {
        "rules": {
            "required": {
                "value": True,
                "message": messages.REQUIRED_FIELD,
            },
            "maxLength": {
                "value": constants.EVENT_LENGTH_MAX,
                "message": messages.EVENT_LENGTH_MAX
            },
        },
    },
    "period_start": {
        "rules": {
            "required": {
                "value": True,
                "message": messages.REQUIRED_FIELD,
            },
        },
    },
    "period_end": {
        "rules": {
            "required": {
                "value": True,
                "message": messages.REQUIRED_FIELD,
            },
        },
    },
}
