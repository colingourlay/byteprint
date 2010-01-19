from django.contrib.auth.models import User

def is_installed():
    if len(User.objects.filter(is_superuser=True)) > 0:
        return True
    return False