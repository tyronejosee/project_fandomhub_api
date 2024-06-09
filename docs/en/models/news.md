# News <Badge type="danger" text="model" />

The News model represents a news entry in the database. It includes various fields to store information such as the title, description, content, image, source URL, tag, and relations to anime and manga. Additionally, it stores information about the author of the news.

## Fields

**`name`** string

The title of the news article.

---

**`description`** string

A brief description of the news article.

---

**`content`** text

The full content of the news article.

---

**`image`** image

An image associated with the news article. The image is uploaded to a specific path defined by the `picture_image_path` function.

---

**`source`** URL

The source URL of the news article.

---

**`tag`** string

A tag categorizing the news article. The tag field has predefined choices defined by `TagChoices` and defaults to `TagChoices.PENDING`.

---

**`anime_relations`** many-to-many

A many-to-many relationship with the Anime model, allowing the news article to be associated with multiple anime entries.

---

**`manga_relations`** many-to-many

A many-to-many relationship with the Manga model, allowing the news article to be associated with multiple manga entries.

---

**`author_id`** foreign key

A foreign key relationship with the User model, referencing the author of the news article. The author must have `is_available` set to `True`. 
