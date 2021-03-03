from virtual_day.utils.image_utils import get_full_url


def message_to_json(message):
    message_type = 'text'
    content = message.content

    return {
        'id': message.id,
        'author': message.user.login,
        'avatar': get_full_url(message.user.avatar),
        'content': content,
        'timestamp': str(message.created_at),
        'task_index': message.data['task_index'] if message.data and 'question_id' in message.data else 0,
        'type': message_type
    }
