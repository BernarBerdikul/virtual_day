from firebase_admin import messaging


def sendPush(title, msg, image, registration_token, data_object=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg,
            image=image
        ),
        data=data_object,
        tokens=registration_token,
    )
    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    return response
