# User <Badge type="danger" text="model" />

The User model represents a user entry in the database. It extends Django's AbstractBaseUser and PermissionsMixin to provide basic user authentication and permissions handling. The model includes various fields to store information such as the user's email, username, role, online status, account status, staff status, and timestamps for account creation and last update.

## Fields

**`id`** UUID

The unique identifier for the user. It is a UUID field that is automatically generated and not editable.

---

**`email`** string

The email address of the user. This field is unique, indexed, and required.

---

**`username`** string

The username of the user. This field is unique and required.

---

**`role`** string

The role of the user within the system. This field has predefined choices and defaults to 'Member'.

---

**`is_online`** boolean

Indicates whether the user is currently online. Defaults to False.

---

**`is_active`** boolean

Indicates whether the user's account is active. Defaults to True.

---

**`is_staff`** boolean

Indicates whether the user has staff privileges. Defaults to False.

---

**`created_at`** datetime

The date and time when the user account was created. This field is automatically set when the user is created.

---

**`updated_at`** datetime

The date and time when the user account was last updated. This field is automatically updated whenever the user data is modified.
