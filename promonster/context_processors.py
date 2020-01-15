from django.conf import settings


def third_parties(request):
    return {
        'GOOGLE_ANALYTICS': settings.GOOGLE_ANALYTICS,
        'YANDEX_METRICA': settings.YANDEX_METRICA,
        'TOP_MAILRU': settings.TOP_MAILRU,
        'SENTRYJS_CONFIG': settings.SENTRYJS_CONFIG
    }
