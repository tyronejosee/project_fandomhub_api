# Review <Badge type="danger" text="model" />

The Review model represents a user's review of a particular content object in the database. It includes fields to store the user who made the review, the content type being reviewed, the rating, the comment, and additional metadata like whether the comment contains spoilers, and counts for helpfulness and reports.

## Fields

**`user_id`** ForeignKey

A reference to the user who created the review. This field links to the `User` model, ensuring the user is available.

---

**`content_type`** ForeignKey

A reference to the type of content being reviewed, utilizing Django's `ContentType` framework.

---

**`object_id`** UUIDField

A UUID representing the specific object being reviewed.

---

**`content_object`** GenericForeignKey

A generic relation to the object being reviewed, combining `content_type` and `object_id`.

---

**`rating`** IntegerField

The rating given to the content, with a value between 1 and 10.

---

**`comment`** TextField

The textual review or comment provided by the user.

---

**`is_spoiler`** BooleanField

A flag indicating whether the comment contains spoilers. Defaults to `False`.

---

**`helpful_count`** PositiveIntegerField

The number of times the review has been marked as helpful by other users. Defaults to `0`.

---

**`reported_count`** PositiveIntegerField

The number of times the review has been reported by other users. Defaults to `0`.
