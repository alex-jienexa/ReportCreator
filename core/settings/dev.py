# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Хосты для связи фронта и бека (CORS)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000', # React server
    'http://127.0.0.1:3000',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000', # React server
    'http://127.0.0.1:3000',
]