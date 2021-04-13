import ast
import os


AVAILABLE_ENVIRON_SETTINGS = [
    'SECRET_KEY',
]

NOT_SET = object()


def get(setting, default=NOT_SET):
    if setting not in AVAILABLE_ENVIRON_SETTINGS:
        raise ValueError('Setting `{}` is not available for loading from env.'.format(setting))

    if setting not in os.environ:
        if default is NOT_SET:
            raise ValueError(
                'Setting `{}` is not in os.environ but default value is not set'.format(setting))
        return default

    try:
        value = ast.literal_eval(os.getenv(setting))
    except Exception:
        # Simply treat env variable as string.
        value = os.getenv(setting)

    return value
