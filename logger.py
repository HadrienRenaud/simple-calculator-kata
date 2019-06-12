class ILogger:

    @staticmethod
    def write(*args, **kwargs):
        print("ILogger:", *args, **kwargs)


class IWebserver:

    @staticmethod
    def notify(*args, **kwargs):
        print("IWebserver:", *args, **kwargs)
