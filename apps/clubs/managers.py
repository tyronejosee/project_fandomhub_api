"""Manager for Clubs App."""

from apps.utils.managers import BaseManager


class ClubManager(BaseManager):
    """Manager for Club model."""


class ClubMemberManager(BaseManager):
    """Manager for ClubMember model."""

    def get_by_club(self, club):
        return self.get_available().filter(club_id=club).only("user_id", "joined_at")
