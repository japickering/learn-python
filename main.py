# Build a User Configuration Manager
from libs.configure import add_setting, view_settings, delete_setting

test_settings = {
    'theme': 'light',
    'volume': 'high'
}

print(add_setting(test_settings, ('notifications', 'enabled')))
print(delete_setting(test_settings, ('notifications')))
print(view_settings(test_settings))
