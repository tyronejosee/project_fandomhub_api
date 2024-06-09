# Club <Badge type="danger" text="model" />

The Club model represents a club entity in the database. It includes various fields to store information such as the name, description, image, category, number of members, creator, and public status.

## Fields

**`name`** string

The name of the club.

---

**`description`** text

A detailed description of the club.

---

**`image`** image

An optional image representing the club. Allowed file types are jpg, png, and webp, with a maximum size of 1 MB and dimensions of 600x600 pixels.

---

**`category`** string

The category of the club. It is a choice field with predefined options.

---

**`members`** positive integer

The number of members in the club. Default value is 0.

---

**`created_by`** one-to-one field

The user who created the club. This is a one-to-one relationship with the User model and is limited to users who are available.

---

**`is_public`** boolean

Indicates whether the club is public or not.

---

# ClubMember <Badge type="danger" text="model" />

The ClubMember model represents a member of a club. It includes fields to store information about the club, user, and the date they joined.

## Fields

**`club_id`** foreign key

The club to which the member belongs. This is a foreign key relationship with the Club model and is limited to clubs that are available.

---

**`user_id`** foreign key

The user who is a member of the club. This is a foreign key relationship with the User model and is limited to users who are available.

---

**`joined_at`** datetime

The date and time when the user joined the club. This field is auto-populated when a record is created.

---

# Event <Badge type="danger" text="model" />

The Event model represents an event organized by a club. It includes fields to store information about the club, name, description, and date of the event.

## Fields

**`club_id`** foreign key

The club organizing the event. This is a foreign key relationship with the Club model and is limited to clubs that are available.

---

**`name`** string

The name of the event.

---

**`description`** text

A detailed description of the event.

---

**`date`** datetime

The date and time of the event.

---

# Topic <Badge type="danger" text="model" />

The Topic model represents a discussion topic within a club. It includes fields to store information about the name, club, and the user who created the topic.

## Fields

**`name`** string

The name of the topic.

---

**`club_id`** foreign key

The club to which the topic belongs. This is a foreign key relationship with the Club model and is limited to clubs that are available.

---

**`created_by`** foreign key

The user who created the topic. This is a foreign key relationship with the User model and is limited to users who are available. It allows null values and sets the user to null if they are deleted.

---

# Discussion <Badge type="danger" text="model" />

The Discussion model represents a discussion within a topic. It includes fields to store information about the topic, content of the discussion, and the user who created the discussion.

## Fields

**`topic_id`** foreign key

The topic to which the discussion belongs. This is a foreign key relationship with the Topic model and is limited to topics that are available.

---

**`content`** text

The content of the discussion.

---

**`created_by`** foreign key

The user who created the discussion. This is a foreign key relationship with the User model and is limited to users who are available. It allows null values and sets the user to null if they are deleted.
