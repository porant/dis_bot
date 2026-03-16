from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = [
            "id",
            "created_at",
            "finished_at",
            "external_id",
            "external_match_key",
            "lobby_id",
            "lobby_name",
            "mode",
            "status",
            "captain_1",
            "captain_2",
            "team_1",
            "team_2",
            "winner_team",
            "map_name",
            "sides",
            "duration_seconds",
            "score_team1",
            "score_team2",
            "region",
            "overtime",
            "forfeit",
            "forfeit_reason",
            "discord_guild_id",
            "discord_channel_id",
            "discord_message_id",
            "win_message_id",
        ]

class SetWinnerSerializer(serializers.Serializer):
    winner_team = serializers.ChoiceField(choices=[1, 2])