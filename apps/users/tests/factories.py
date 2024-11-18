"""Factories for Users App."""

import factory

from ..models import User
from ..choices import RoleChoices


class UserBaseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        skip_postgeneration_save = True

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    role = RoleChoices.CONTRIBUTOR
    is_online = True
    is_active = True
    is_staff = False

    @factory.post_generation
    def password(obj, create, extracted, **kwargs):
        """Set a password for the user."""
        obj.set_password(extracted or "defaultpassword")
        if create:
            obj.save()


class MemberFactory(UserBaseFactory):

    role = RoleChoices.MEMBER


class PremiumFactory(UserBaseFactory):

    role = RoleChoices.PREMIUM


class ContributorFactory(UserBaseFactory):

    role = RoleChoices.CONTRIBUTOR


class ModeratorFactory(UserBaseFactory):

    role = RoleChoices.MODERATOR


class AdministratorFactory(UserBaseFactory):

    role = RoleChoices.MEMBER
    is_staff = True
