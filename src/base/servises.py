from django.core.exceptions import ValidationError


def get_path_upload_avatar(instanse , file ):
    # построение пути к файлу , format : (media)/avatar/user_id/photo.jpg
    # instanse - это обьект пользователя
    return f'avatar/{instanse.id}/{file}'

def validate_size_image(file_obj):
    # проверка размера файла
    megabite_limit = 2

    if file_obj.size > megabite_limit*1024*1024 :
        raise ValidationError(f"максимальный размер файла {megabite_limit} МБ")