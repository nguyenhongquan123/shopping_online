def only_admin(context):
    def decorator(view_func):
        def wrap(request,*args, **kwargs):
            if request.user.is_owner:
                return view_func(request)
            return HttpResponse(context)
        return wrap
    return decorator