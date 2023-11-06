
def login_success(sender, **kwargs):
    if not (session := kwargs.get("session", None)):
        return
    ip = session.address

    from .models import Host, Record

    host, created = Host.objects.get_or_create(ip=ip)
    host.records.create(user=sender, is_success=True)


def login_fail(sender, **kwargs):
    if not (session := kwargs.get("session", None)):
        return
    ip = session.address

    from .models import Host, Record

    host, created = Host.objects.get_or_create(ip=ip)
    host.records.create(user=sender, is_success=False, reason="Failed to authenticate")