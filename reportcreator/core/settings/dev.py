# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Хосты для связи фронта и бека (CORS)
CORS_ORIGIN_WHITELIST = [
    'http://localhost:4000', # React dev server
    'http://127.0.0.1:4000',
]