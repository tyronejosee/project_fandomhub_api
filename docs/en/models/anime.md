# Anime <Badge type="danger" text="model" />

The Anime model represents an anime entry in the database. It includes various fields to store information such as the name, alternative names, image, trailer URL, synopsis, background, season, year, broadcast details, media type, source, number of episodes, status, airing dates, producers, licensors, studio, genres, themes, duration, rating, website, and recommendation status. Additionally, it stores statistical data like the score, ranking, popularity, members, and favorites.

## Fields

**`name`** string

The name of the anime in English.

---

**`name_jpn`** string

The name of the anime in Japanese.

---

**`name_rom`** string

The romanized name of the anime.

---

**`alternative_names`** list

Alternative names for the anime.

---

**`image`** image

The image representing the anime.

---

**`trailer`** string

The URL of the trailer for the anime.

---

**`synopsis`** string

A brief summary of the anime.

---

**`background`** string

Additional background information about the anime.

---

**`season`** string

The season in which the anime aired.

---

**`year`** integer

The year in which the anime aired.

---

**`broadcast_id`** integer

The ID of the broadcast information for the anime.

---

**`media_type`** string

The media type of the anime (e.g., TV, OVA, movie).

---

**`source`** string

The source material of the anime (e.g., manga, novel).

---

**`episodes`** integer

The total number of episodes of the anime.

---

**`status`** string

The current status of the anime (e.g., airing, finished).

---

**`aired_from`** date

The date when the anime first aired.

---

**`aired_to`** date

The date when the anime last aired.

---

**`producers`** list

The production companies involved in producing the anime.

---

**`licensors_id`** integer

The ID of the licensing company for the anime.

---

**`studio_id`** integer

The ID of the studio that produced the anime.

---

**`genres`** list

The genres of the anime.

---

**`themes`** list

The themes explored in the anime.

---

**`duration`** string

The duration of each episode of the anime.

---

**`rating`** string

The age rating of the anime.

---

**`website`** string

The official website of the anime.

---

**`is_recommended`** boolean

A boolean indicating if the anime is recommended.

## Meta options

## Methods
