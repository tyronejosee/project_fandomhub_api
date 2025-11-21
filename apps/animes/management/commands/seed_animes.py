from django.core.management.base import BaseCommand
from datetime import time, timedelta, date

from apps.animes.models import Anime, Broadcast
from apps.producers.models import Producer
from apps.genres.models import Genre, Theme
from apps.producers.choices import TypeChoices
from apps.animes.choices import (
    SeasonChoices,
    MediaTypeChoices,
    SourceChoices,
    StatusChoices,
    RatingChoices,
    DayChoices,
    TimezoneChoices,
)

# Constants
PRODUCERS: dict[str, TypeChoices] = {
    "Ufotable": TypeChoices.STUDIO,
    "MAPPA": TypeChoices.STUDIO,
    "Wit Studio": TypeChoices.STUDIO,
    "A-1 Pictures": TypeChoices.STUDIO,
    "Bones": TypeChoices.STUDIO,
    "Madhouse": TypeChoices.STUDIO,
    "Pierrot": TypeChoices.STUDIO,
    "Production I.G": TypeChoices.STUDIO,
    "Aniplex": TypeChoices.DISTRIBUTOR,
    "Crunchyroll": TypeChoices.DISTRIBUTOR,
    "Funimation": TypeChoices.LICENSOR,
    "Sentai Filmworks": TypeChoices.LICENSOR,
    "Viz Media": TypeChoices.LICENSOR,
    "White Fox": TypeChoices.STUDIO,
    "Manglobe": TypeChoices.STUDIO,
    "Sunrise": TypeChoices.STUDIO,
    "Studio Deen": TypeChoices.STUDIO,
    "Kyoto Animation": TypeChoices.STUDIO,
    "Netflix": TypeChoices.LICENSOR,
    "Tatsunoko Production": TypeChoices.STUDIO,
    "Kinema Citrus": TypeChoices.STUDIO,
}

THEME_NAMES: list[str] = [
    "Shounen",
    "School",
    "Military",
    "Historical",
    "Psychological",
    "Samurai",
    "Isekai",
    "Space",
    "Music",
    "Sports",
    "Supernatural",
]

GENRE_NAMES: list[str] = [
    "Action",
    "Adventure",
    "Fantasy",
    "Drama",
    "Comedy",
    "Sci-Fi",
    "Romance",
    "Horror",
    "Mystery",
    "Supernatural",
    "Sports",
    "Psychological",
]

ANIMES_DATA: list[dict] = [
    {
        "name": "Attack on Titan",
        "name_jpn": "進撃の巨人",
        "year": 2013,
        "season": SeasonChoices.SPRING,
        "episodes": 25,
        "studio": "Wit Studio",
        "distributor": "Aniplex",
        "licensor": "Funimation",
        "genres": ["Action", "Drama"],
        "themes": ["Shounen", "Psychological"],
    },
    {
        "name": "Demon Slayer",
        "name_jpn": "鬼滅の刃",
        "year": 2019,
        "season": SeasonChoices.SPRING,
        "episodes": 26,
        "studio": "Ufotable",
        "distributor": "Aniplex",
        "licensor": "Funimation",
        "genres": ["Action", "Supernatural"],
        "themes": ["Shounen"],
    },
    {
        "name": "Jujutsu Kaisen",
        "name_jpn": "呪術廻戦",
        "year": 2020,
        "season": SeasonChoices.FALL,
        "episodes": 24,
        "studio": "MAPPA",
        "distributor": "Crunchyroll",
        "licensor": "Funimation",
        "genres": ["Action", "Supernatural"],
        "themes": ["School", "Shounen"],
    },
    {
        "name": "Fullmetal Alchemist: Brotherhood",
        "name_jpn": "鋼の錬金術師 FULLMETAL ALCHEMIST",
        "year": 2009,
        "season": SeasonChoices.SPRING,
        "episodes": 64,
        "studio": "Bones",
        "distributor": "Aniplex",
        "licensor": "Funimation",
        "genres": ["Action", "Adventure", "Drama"],
        "themes": ["Military"],
    },
    {
        "name": "Sword Art Online",
        "name_jpn": "ソードアート・オンライン",
        "year": 2012,
        "season": SeasonChoices.SUMMER,
        "episodes": 25,
        "studio": "A-1 Pictures",
        "distributor": "Aniplex",
        "licensor": "Sentai Filmworks",
        "genres": ["Action", "Fantasy"],
        "themes": ["Isekai"],
    },
    {
        "name": "Death Note",
        "name_jpn": "デスノート",
        "year": 2006,
        "season": SeasonChoices.FALL,
        "episodes": 37,
        "studio": "Madhouse",
        "distributor": "Aniplex",
        "licensor": "Viz Media",
        "genres": ["Mystery", "Psychological"],
        "themes": ["Supernatural"],
    },
    {
        "name": "One Punch Man",
        "name_jpn": "ワンパンマン",
        "year": 2015,
        "season": SeasonChoices.FALL,
        "episodes": 12,
        "studio": "Madhouse",
        "distributor": "Crunchyroll",
        "licensor": "Funimation",
        "genres": ["Action", "Comedy"],
        "themes": ["Supernatural"],
    },
    {
        "name": "Tokyo Ghoul",
        "name_jpn": "東京喰種",
        "year": 2014,
        "season": SeasonChoices.SUMMER,
        "episodes": 12,
        "studio": "Pierrot",
        "distributor": "Crunchyroll",
        "licensor": "Funimation",
        "genres": ["Action", "Horror"],
        "themes": ["Supernatural"],
    },
    {
        "name": "My Hero Academia",
        "name_jpn": "僕のヒーローアカデミア",
        "year": 2016,
        "season": SeasonChoices.SPRING,
        "episodes": 13,
        "studio": "Bones",
        "distributor": "Aniplex",
        "licensor": "Funimation",
        "genres": ["Action", "Comedy"],
        "themes": ["School", "Shounen"],
    },
    {
        "name": "Haikyuu!!",
        "name_jpn": "ハイキュー!!",
        "year": 2014,
        "season": SeasonChoices.SPRING,
        "episodes": 25,
        "studio": "Production I.G",
        "distributor": "Crunchyroll",
        "licensor": "Sentai Filmworks",
        "genres": ["Comedy", "Drama", "Sports"],
        "themes": ["School", "Sports"],
    },
    {
        "name": "Steins;Gate",
        "name_jpn": "シュタインズ・ゲート",
        "year": 2011,
        "season": SeasonChoices.SPRING,
        "episodes": 24,
        "studio": "White Fox",
        "distributor": "Crunchyroll",
        "licensor": "Funimation",
        "genres": ["Sci-Fi", "Mystery", "Drama"],
        "themes": ["Psychological"],
    },
    {
        "name": "Mob Psycho 100",
        "name_jpn": "モブサイコ100",
        "year": 2016,
        "season": SeasonChoices.SUMMER,
        "episodes": 12,
        "studio": "Bones",
        "distributor": "Crunchyroll",
        "licensor": "Funimation",
        "genres": ["Action", "Comedy", "Supernatural"],
        "themes": ["Shounen", "School"],
    },
    {
        "name": "Code Geass: Lelouch of the Rebellion",
        "name_jpn": "コードギアス 反逆のルルーシュ",
        "year": 2006,
        "season": SeasonChoices.FALL,
        "episodes": 25,
        "studio": "Sunrise",
        "distributor": "Crunchyroll",
        "licensor": "Funimation",
        "genres": ["Action", "Sci-Fi", "Drama"],
        "themes": ["Military"],
    },
    {
        "name": "Samurai Champloo",
        "name_jpn": "サムライチャンプルー",
        "year": 2004,
        "season": SeasonChoices.SPRING,
        "episodes": 26,
        "studio": "Manglobe",
        "distributor": "Crunchyroll",
        "licensor": "Funimation",
        "genres": ["Action", "Adventure"],
        "themes": ["Samurai", "Historical"],
    },
    {
        "name": "Your Lie in April",
        "name_jpn": "四月は君の嘘",
        "year": 2014,
        "season": SeasonChoices.FALL,
        "episodes": 22,
        "studio": "A-1 Pictures",
        "distributor": "Aniplex",
        "licensor": "Aniplex",
        "genres": ["Drama", "Romance"],
        "themes": ["School", "Music"],
    },
    {
        "name": "Ping Pong the Animation",
        "name_jpn": "ピンポン THE ANIMATION",
        "year": 2014,
        "season": SeasonChoices.SPRING,
        "episodes": 11,
        "studio": "Tatsunoko Production",
        "distributor": "Crunchyroll",
        "licensor": "Funimation",
        "genres": ["Drama", "Sports"],
        "themes": ["Sports", "School"],
    },
    {
        "name": "Made in Abyss",
        "name_jpn": "メイドインアビス",
        "year": 2017,
        "season": SeasonChoices.SUMMER,
        "episodes": 13,
        "studio": "Kinema Citrus",
        "distributor": "Sentai Filmworks",
        "licensor": "Sentai Filmworks",
        "genres": ["Adventure", "Fantasy", "Mystery"],
        "themes": ["Historical"],
    },
    {
        "name": "Violet Evergarden",
        "name_jpn": "ヴァイオレット・エヴァーガーデン",
        "year": 2018,
        "season": SeasonChoices.WINTER,
        "episodes": 13,
        "studio": "Kyoto Animation",
        "distributor": "Netflix",
        "licensor": "Netflix",
        "genres": ["Drama", "Fantasy"],
        "themes": ["Military"],
    },
    {
        "name": "KonoSuba: God's Blessing on This Wonderful World!",
        "name_jpn": "この素晴らしい世界に祝福を！",
        "year": 2016,
        "season": SeasonChoices.WINTER,
        "episodes": 10,
        "studio": "Studio Deen",
        "distributor": "Crunchyroll",
        "licensor": "Funimation",
        "genres": ["Comedy", "Fantasy"],
        "themes": ["Isekai"],
    },
    {
        "name": "Space Brothers",
        "name_jpn": "宇宙兄弟",
        "year": 2012,
        "season": SeasonChoices.SPRING,
        "episodes": 99,
        "studio": "A-1 Pictures",
        "distributor": "Crunchyroll",
        "licensor": "Sentai Filmworks",
        "genres": ["Drama", "Comedy"],
        "themes": ["Space"],
    },
]


class Command(BaseCommand):
    help = "Seed 20 real animes safely."

    def handle(self, *args, **kwargs) -> None:
        self.stdout.write(self.style.WARNING("Seeding animes…"))
        self.stdout.write(self.style.WARNING("Clearing existing data…"))

        Anime.objects.all().delete()
        Broadcast.objects.all().delete()
        Genre.objects.all().delete()
        Theme.objects.all().delete()
        Producer.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("All related tables cleared."))

        producer_objs: dict = {}

        for name, t in PRODUCERS.items():
            obj, _ = Producer.objects.update_or_create(
                name=name,
                defaults={"name_jpn": name, "type": t, "is_available": True},
            )
            producer_objs[name] = obj

        genre_objs: dict[str, Genre] = {
            g: Genre.objects.get_or_create(name=g)[0] for g in GENRE_NAMES
        }

        theme_objs: dict[str, Theme] = {
            t: Theme.objects.get_or_create(name=t)[0] for t in THEME_NAMES
        }

        # Create animes safely
        for item in ANIMES_DATA:
            broadcast: Broadcast = Broadcast.objects.create(
                day=DayChoices.MONDAY,
                time=time(22, 0),
                timezone=TimezoneChoices.JST,
            )

            anime, _ = Anime.objects.update_or_create(
                name=item["name"],
                defaults={
                    "name_jpn": item["name_jpn"],
                    "year": item["year"],
                    "season": item["season"],
                    "episodes": item["episodes"],
                    "duration": timedelta(minutes=24),
                    "studio_id": producer_objs[item["studio"]],
                    "licensors_id": producer_objs[item["licensor"]],
                    "broadcast_id": broadcast,
                    "media_type": MediaTypeChoices.TV,
                    "source": SourceChoices.MANGA,
                    "status": StatusChoices.FINISHED,
                    "aired_from": date(item["year"], 4, 1),
                    "aired_to": date(item["year"], 9, 1),
                    "rating": RatingChoices.PG13,
                },
            )
            anime.producers.set([producer_objs[item["distributor"]]])
            anime.genres.set([genre_objs[g] for g in item["genres"]])
            anime.themes.set([theme_objs[t] for t in item["themes"]])

            self.stdout.write(self.style.SUCCESS(f"Created/Updated: {anime.name}"))

        self.stdout.write(self.style.SUCCESS("Seed completed."))
