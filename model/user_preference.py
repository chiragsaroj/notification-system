from model.channel_type import ChannelType


class UserPreference:
    def __init__(self, user_id: str, channel_preferences: set[ChannelType]):
        self.user_id = user_id
        self.channel_preferences = channel_preferences


    def get_user_id(self):
        return self.user_id


    def get_channel_preferences(self):
        return self.channel_preferences