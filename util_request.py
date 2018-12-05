from threading import local

_thread_locals = local()


def get_current_request():
    return getattr(_thread_locals, "request", None)


def request_user():
    request = get_current_request()
    if request:
        return getattr(request, "user", None)
