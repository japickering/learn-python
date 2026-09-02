def add_setting(settings, pairs):
    key = pairs[0].lower()
    value = pairs[1].lower()

    if key in settings:
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    else:
        settings.update({key: value})
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'


def update_setting(settings, pairs):
    key = pairs[0].lower()
    value = pairs[1].lower()

    if key in settings:
        settings.update({key: value})
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'


def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return f'Setting not found!'
    else:
        del settings[key]
        return f'Setting \'{key}\' deleted successfully!'


def view_settings(settings):
    if not settings:
        return 'No settings available.'
    else:
        settings_str = 'Current User Settings:\n'
        for i, v in enumerate(settings.items()):
            settings_str += f'{v[0].capitalize()}: {v[1]}\n'
        return settings_str
