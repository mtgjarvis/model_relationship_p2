Track.objects.filter(album__title='Vinicius De Moraes')

Album.objects.filter(artist__name="Philip Glass Ensemble")

Track.objects.filter(playlists__name="Brazilian Music")

Track.objects.filter(genre__name="Jazz")

Track.objects.filter(name__icontains="My Time After Awhile").first().genre.name

Track.objects.filter(name__icontains="My Time After Awhile").first().media_types.name

Track.objects.filter(name__icontains="My Time After Awhile").first().album.title