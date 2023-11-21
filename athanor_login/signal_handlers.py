def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # To get the first IP, if there are multiple IPs due to proxies.
    else:
        ip = request.META.get('REMOTE_ADDR', None)
    return ip


def django_login_success(sender, **kwargs):
    if not (user := kwargs.get("user", dict())):
        return
    if not (request := kwargs.get("request", None)):
        return
    if not (ip := get_client_ip(request)):
        return
    _login_record(user, ip)


def django_login_fail(sender, **kwargs):
    if not (request := kwargs.get("request", None)):
        return
    if not (ip := get_client_ip(request)):
        return
    if not (credentials := kwargs.get("credentials", dict())):
        return
    if not (username := credentials.get("username", None)):
        return
    from evennia import DefaultAccount
    if not (account := DefaultAccount.objects.filter_family(username__iexact=username).first()):
        pass
    _login_record(account, ip, success=False, reason=kwargs.get("reason", "Failed to authenticate."))


def login_success(sender, **kwargs):
    if not (session := kwargs.get("session", None)):
        return
    _login_record(sender, session.address)


def login_fail(sender, **kwargs):
    if not (session := kwargs.get("session", None)):
        return
    _login_record(sender, session.address, success=False, reason=kwargs.get("reason", "Failed to authenticate."))


def _login_record(user, ip, success=True, reason=None):
    from .models import Host, Record
    host, created = Host.objects.get_or_create(ip=ip)
    host.records.create(user=user, is_success=success, reason=reason)
