'''def middlewarename(get_response):
    code to be written that need to 
    be executed only once i.e
    for initialization or for 
    configuration.

    def your_functionname(request):
        code need to be executed before views function 
        is called.
        variable=get_response(request)
        code need to be executed after views function is called

        return variable

return your_functionname
1) Call to middlewarefunction()
    Middlewarefunction is called when you run django server.

2) Inner function or your_function is called when client send request.
'''

def blog_middleware(get_response):
    print("blog_middleware function is invoked when django server runs")
    print("Code need to be executed only once for intialization or configuration")

    def my_middleware(request):
        print("Hello before view function is called...")
        res=get_response(request)
        print(res)
        print("Hello from middleware after view function is being executed")

        return res
    
    return my_middleware