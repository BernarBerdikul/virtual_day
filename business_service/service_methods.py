from django.contrib.contenttypes.models import ContentType
from virtual_day.core.models import Billboard, MediaBillboard
from virtual_day.utils.exceptions import CommonException, ForbiddenException
from virtual_day.utils import messages, codes, constants
from translations.models import Translation


def create_translation(model: object, translations: list,
                       object_id: int) -> None:
    """ create translations objects for model which get from params """
    model_type_id = ContentType.objects.get_for_model(model).id
    list_for_create, billboard_static_list_create = [], []
    for translation, number in zip(translations, range(len(translations))):
        if model is Billboard:
            if 'url_link' in translation:
                billboard_static_list_create.append(MediaBillboard(
                        billboard_id=object_id, url_link=translation['url_link'],
                        language=translation['language']))
            elif 'pdf_file' in translation:
                billboard_static_list_create.append(MediaBillboard(
                        billboard_id=object_id, pdf_file=translation['pdf_file'],
                        language=translation['language']))
        # special translation model's fields
        for field in model.TranslatableMeta.fields:
            list_for_create.append(Translation(
                text=translation[field], object_id=object_id,
                field=field, language=translation['language'],
                content_type_id=model_type_id))
    # multiple create
    Translation.objects.bulk_create(list_for_create)
    if model is Billboard:
        MediaBillboard.objects.bulk_create(billboard_static_list_create)
    return None


def update_translation(model: object, translations: list,
                       object_id: int) -> object:
    """ update translations objects for model which get from params """
    model_type_id = ContentType.objects.get_for_model(model).id
    list_for_update, list_for_create, list_for_delete = [], [], []
    billboard_static_list_create, billboard_static_list_update = [], []
    # compare translations in db with translations in request
    for translation in translations:
        old_translations = Translation.objects.filter(
            object_id=object_id, language=translation['language'],
            content_type_id=model_type_id)
        for trans in old_translations:
            """ prepare list with translation ids, 
                which need to exclude from translation ids in db """
            if trans.language == translation['language']:
                list_for_delete.append(trans.id)

    # list with translation objects, which should be deleted from db
    Translation.objects.filter(
        object_id=object_id, content_type_id=model_type_id
    ).exclude(pk__in=list_for_delete).delete()

    for translation, number in zip(translations, range(len(translations))):
        if model is Billboard:
            try:
                billboard_static = MediaBillboard.objects.get(
                    language=translation['language'],
                    billboard_id=object_id
                )
                if 'url_link' in translation:
                    billboard_static_list_update.append(
                        Translation(id=billboard_static.id,
                                    url_link=translation['url_link']))
                elif 'pdf_file' in translation:
                    billboard_static_list_update.append(
                        Translation(id=billboard_static.id,
                                    pdf_file=translation['pdf_file']))
            except MediaBillboard.DoesNotExist:
                if 'url_link' in translation:
                    billboard_static_list_create.append(
                        MediaBillboard(
                            billboard_id=object_id,
                            url_link=translation['url_link'],
                            language=translation['language']))
                elif 'pdf_file' in translation:
                    billboard_static_list_create.append(
                        MediaBillboard(
                            billboard_id=object_id,
                            pdf_file=translation['pdf_file'],
                            language=translation['language']))
        # special translation model's fields
        for field in model.TranslatableMeta.fields:
            try:
                trans = Translation.objects.get(
                    object_id=object_id, language=translation['language'],
                    field=field, content_type_id=model_type_id)
                # scrip not changed translations
                if trans.text == translation[field]:
                    continue
                list_for_update.append(
                    Translation(id=trans.id, text=translation[field]))
            except Translation.DoesNotExist:
                # if translation doesn't exist that create them
                list_for_create.append(Translation(
                    object_id=object_id, field=field, text=translation[field],
                    language=translation['language'],
                    content_type_id=model_type_id))
    # multiple update
    Translation.objects.bulk_update(
        list_for_update, ['text'])
    # multiple create
    Translation.objects.bulk_create(
        list_for_create)

    if model is Billboard:
        MediaBillboard.objects.bulk_update(
            billboard_static_list_update, ['url_link', 'pdf_file'])
        MediaBillboard.objects.bulk_create(
            billboard_static_list_create)
    return None
