def at_server_start():
    from evennia.server import signals

    from . signal_handlers import login_success, login_fail

    signals.SIGNAL_ACCOUNT_POST_LOGIN.connect(login_success)
    signals.SIGNAL_ACCOUNT_POST_LOGIN_FAIL.connect(login_fail)


