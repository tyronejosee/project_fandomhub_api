# Character <Badge type="danger" text="model" />

The Character model represents a character entry in the database. It includes various fields to store information such as the name, kanji name, description, role, image, and the number of favorites.

## Fields

**`name`** string

The name of the character.

---

**`name_kanji`** string

The kanji name of the character.

---

**`about`** text

A description of the character.

---

**`role`** string

The role of the character, with choices defined by `RoleChoices`.

---

**`image`** image

An optional image of the character, with specific validation for file extension, size, and dimensions (max 600x600 pixels, max 1 MB).

---

**`favorites`** integer

The number of users who have favorited the character. Default value is 0.

---

---

# CharacterVoice <Badge type="danger" text="model" />

The CharacterVoice model represents the relationship between a character and its voice actor. It includes references to both the character and the voice actor.

## Fields

**`character_id`** foreign key

A foreign key to the Character model, limited to characters marked as available.

---

**`voice_id`** foreign key

A foreign key to the Person model, limited to voice actors marked as available.

---

---

# CharacterAnime <Badge type="danger" text="model" />

The CharacterAnime model represents the relationship between a character and an anime. It includes references to both the character and the anime.

## Fields

**`character_id`** foreign key

A foreign key to the Character model, limited to characters marked as available.

---

**`anime_id`** foreign key

A foreign key to the Anime model, limited to animes marked as available.

---

---

# CharacterManga <Badge type="danger" text="model" />

The CharacterManga model represents the relationship between a character and a manga. It includes references to both the character and the manga.

## Fields

**`character_id`** foreign key

A foreign key to the Character model, limited to characters marked as available.

---

**`manga_id`** foreign key

A foreign key to the Manga model, limited to mangas marked as available.

---

---

Let me know if you need any changes or additional details.
