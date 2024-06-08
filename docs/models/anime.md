---
outline: deep
---

# Anime

## The anime model

The contact model contains all the information about your contacts, such as their username, avatar, and phone number. It also contains a reference to the conversation between you and the contact and information about when they were last active on Protocol.

### Properties

`id`  uuid

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---

`name`  string

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---

`name_jpn` string

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---

`name_rom` string

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---

`alternative_names` array

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---

image = models.ImageField(
    _("image"),
    upload_to=picture_image_path,
    blank=True,
    null=True,
    validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "webp"]),
        ImageSizeValidator(max_width=909, max_height=1280),
        FileSizeValidator(limit_mb=2),
    ],
)
trailer = models.URLField(_("trailer"), max_length=255, blank=True)
synopsis = models.TextField(_("synopsis"), blank=True, null=True)
background = models.TextField(_("background"), blank=True, null=True)
season = models.CharField(
    _("season"),
    max_length=10,
    db_index=True,
    choices=SeasonChoices.choices,
)
year = models.IntegerField(
    _("year"),
    default=2010,
    db_index=True,
    validators=[MinValueValidator(1900), MaxValueValidator(2100)],
)
broadcast_id = models.ForeignKey(
    Broadcast,
    on_delete=models.SET_NULL,
    blank=True,
    null=True,
    limit_choices_to={"is_available": True},
    verbose_name=_("broadcast"),
)
media_type = models.CharField(
    _("media type"),
    max_length=10,
    choices=MediaTypeChoices.choices,
    default=MediaTypeChoices.TV,
)
source = models.CharField(
    _("source"),
    max_length=10,
    choices=SourceChoices.choices,
    default=SourceChoices.MANGA,
)
episodes = models.IntegerField(
    _("episodes"),
    default=0,
    validators=[MinValueValidator(0), MaxValueValidator(1500)],
)
status = models.CharField(
    _("status"),
    max_length=10,
    choices=StatusChoices.choices,
    default=StatusChoices.AIRING,
)
aired_from = models.DateField(_("aired from"))
aired_to = models.DateField(_("aired to"), blank=True, null=True)
producers = models.ManyToManyField(
    Producer,
    limit_choices_to={
        "type": TypeChoices.DISTRIBUTOR,
        "is_available": True,
    },
    related_name="produced_animes",
    verbose_name=_("producers"),
)
licensors_id = models.ForeignKey(
    Producer,
    on_delete=models.CASCADE,
    blank=True,
    null=True,
    limit_choices_to={
        "type": TypeChoices.LICENSOR,
        "is_available": True,
    },
    related_name="licensed_animes",
    verbose_name=_("licensors"),
)
studio_id = models.ForeignKey(
    Producer,
    on_delete=models.CASCADE,
    limit_choices_to={
        "type": TypeChoices.STUDIO,
        "is_available": True,
    },
    related_name="studio_animes",
    verbose_name=_("studio"),
)
genres = models.ManyToManyField(Genre, verbose_name=_("genres"))
themes = models.ManyToManyField(Theme, verbose_name=_("themes"))
duration = models.CharField(_("duration"), max_length=20, blank=True)
rating = models.CharField(
    _("rating"),
    max_length=10,
    choices=RatingChoices.choices,
    default=RatingChoices.PG13,
)
website = models.URLField(_("website"), max_length=255, blank=True)
is_recommended = models.BooleanField(_("is recommended"), default=False)

score = models.FloatField(_("score"), blank=True, null=True)

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---
ranked = models.PositiveIntegerField(_("ranked"), default=0)

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---
popularity = models.PositiveIntegerField(_("popularity"), default=0)

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---
members = models.PositiveIntegerField(_("members"), default=0)

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---
favorites = models.PositiveIntegerField(_("favorites"), default=0)

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

---

<!-- # is_publishing = models.BooleanField(_("is_publishing"), default=False)
# premiered = season + year
# aired = aired_from / aired_to -->

- BaseModel
