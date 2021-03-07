from django.contrib.contenttypes.models import ContentType
from virtual_day.utils.exceptions import CommonException, ForbiddenException
from virtual_day.utils import messages, codes, constants
from translations.models import Translation


def create_translation(model: object, translations: list, object_id: int) -> None:
    """ create translations objects for model which get from params """
    model_type_id = ContentType.objects.get_for_model(model).id
    list_for_create = []
    for translation, number in zip(translations, range(len(translations))):
        # special translation model's fields
        for field in model.TranslatableMeta.fields:
            list_for_create.append(Translation(text=translation[field],
                                               object_id=object_id,
                                               field=field,
                                               language=translation['language'],
                                               content_type_id=model_type_id))
    # multiple create
    Translation.objects.bulk_create(list_for_create)
    return None


def update_translation(model: object, translations: list, object_id: int) -> object:
    """ update translations objects for model which get from params """
    model_type_id = ContentType.objects.get_for_model(model).id
    list_for_update, list_for_create, list_for_delete = [], [], []
    # compare translations in db with translations in request
    for translation in translations:
        old_translations = Translation.objects.filter(object_id=object_id, language=translation['language'],
                                                      content_type_id=model_type_id)
        for trans in old_translations:
            # prepare list with translation ids, which need to exclude from translation ids in db
            if trans.language == translation['language']:
                list_for_delete.append(trans.id)

    # list with translation objects, which should be deleted from db
    Translation.objects.filter(
        object_id=object_id, content_type_id=model_type_id
    ).exclude(pk__in=list_for_delete).delete()

    for translation, number in zip(translations, range(len(translations))):
        # special translation model's fields
        for field in model.TranslatableMeta.fields:
            try:
                trans = Translation.objects.get(object_id=object_id, language=translation['language'],
                                                field=field, content_type_id=model_type_id)
                # scrip not changed translations
                if trans.text == translation[field]:
                    continue
                list_for_update.append(Translation(id=trans.id, text=translation[field]))
            except Translation.DoesNotExist:
                # if translation doesn't exist that create them
                list_for_create.append(Translation(object_id=object_id,
                                                   field=field, text=translation[field],
                                                   language=translation['language'],
                                                   content_type_id=model_type_id))
    # multiple update
    Translation.objects.bulk_update(list_for_update, ['text'])
    # multiple create
    Translation.objects.bulk_create(list_for_create)
    return None
