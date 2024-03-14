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




    # @action(detail=True, methods=['post'])
    # def add_anime(self, request, pk=None):
    #     """Pending."""
    #     playlist = self.get_object()
    #     anime_id = request.data.get('anime_id')
    #     rating = request.data.get('rating')

    #     if not anime_id or not rating:
    #         return Response(
    #             {'error': 'anime_id and rating are required'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )

    #     try:
    #         anime = Anime.objects.get(pk=anime_id)
    #     except Anime.DoesNotExist:
    #         return Response({'error': 'Anime not found'}, status=404)

    #     playlist_anime, created = PlaylistAnime.objects.get_or_create(
    #         playlist=playlist, anime=anime
    #     )
    #     playlist_anime.rating = rating
    #     playlist_anime.save()

    #     serializer = PlaylistSerializer(playlist)
    #     return Response(serializer.data)








    rating = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES,
        default="pending", db_index=True
    )
    is_watched = models.BooleanField(default=False, db_index=True)
    tags = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
