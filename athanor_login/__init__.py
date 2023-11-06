
def init(settings, plugins):
    settings.INSTALLED_APPS.append("athanor_login")
    settings.AT_SERVER_STARTSTOP_MODULE.append("athanor_login.startup_hooks")
    settings.CMD_MODULES_ACCOUNT.append("athanor_login.commands")