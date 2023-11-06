def at_server_start():
    from evennia.server import signals

    from . signal_handlers import login_success, login_fail, django_login_fail, django_login_success

    signals.SIGNAL_ACCOUNT_POST_LOGIN.connect(login_success)
    signals.SIGNAL_ACCOUNT_POST_LOGIN_FAIL.connect(login_fail)

    from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

    user_logged_in.connect(django_login_success)
    user_login_failed.connect(django_login_fail)
