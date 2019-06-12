class ILogger:

    @staticmethod
    def write(*args, **kwargs):
        print("ILogger:", *args, **kwargs)