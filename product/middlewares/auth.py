from django.shortcuts import redirect




def login_auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
            
        response = get_response(request, *args, **kwargs)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware