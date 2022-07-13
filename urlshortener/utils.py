from django.conf import settings
from random import choice
from string import ascii_letters, digits
from django.contrib.auth.models import User


SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 6)
AVAIABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAIABLE_CHARS):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )

def create_shortened_url(model_instance):
    random_code = create_random_code()
    model_class = model_instance.__class__
    print(User)
    if model_class.objects.filter(long_url=model_instance.long_url, author=model_instance.author).exists():
            return model_class.objects.filter(long_url=model_instance.long_url, author=model_instance.author)[0].short_url, False

    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortened_url(model_instance)

    return random_code, True

