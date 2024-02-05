"""Dump classes."""

class None():
    
    def create(self, request, *args, **kwargs):
        """
        Create a new Genre instance.

        This endpoint allows the creation of a new Genre
        by providing the necessary data in the request.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {'message': _('Genre created successfully.'), 'data': serializer.data},
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        except Exception as e:
            return Response(
                {'errors': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )