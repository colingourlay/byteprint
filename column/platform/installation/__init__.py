from django.contrib.auth.models import User

def is_installed():
    try:
        superusers = User.objects.filter(is_superuser=True)
        if len(superusers) > 0:
            return True
        return False
    except:
        return False