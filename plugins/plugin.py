class Plugin:
    def __init__(self):
        self.commands = {}
        self.regexes = {}

    def command(self, commands):
        def decorator(fn):
            for cmd in commands:
                self.commands[cmd] = fn
            return fn
        return decorator
    

#@plugin.regex(...)
#def url_preview(message, match):
