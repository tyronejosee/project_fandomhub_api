class CreateMixin(mixins.CreateModelMixin):
    """
    Mixin to add a success message to the response data after creating an instance.
    """
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': self.get_create_message(), 'data': response.data}
        return response

    def get_create_message(self):
        """
        Override this method to customize the success message.
        """
        return _('Instance created successfully.')
