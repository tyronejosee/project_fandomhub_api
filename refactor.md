    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.clear()
        return response