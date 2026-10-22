from model.channel_type import ChannelType


class Notification:
    def __init__(self, user_id: str, message: str):
        self.user_id = user_id
        self.message = message
        self.channel_type: ChannelType = None


    def get_user_id(self):
        return self.user_id