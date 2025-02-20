from decouple import config


class Settings:
    MIN_NUMBER = config('MIN_NUMBER', cast=int)
    MAX_NUMBER = config('MAX_NUMBER', cast=int)
    ATTEMPTS = config('ATTEMPTS', cast=int)
    INITIAL_CAPITAL = config('INITIAL_CAPITAL', cast=int)
