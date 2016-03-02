class Television(object):
    """Television simulation"""
    def __init__(self, channel=0, volume=0):
        self.channel = channel
        self.volume = volume

    def raise_volume(self):
        self.volume += 1
        if self.volume > 10:
            self.volume = 10
        print("\nVolume ", self.volume)

    def lower_volume(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
        print("\nVolume ", self.volume)

    def switch_channel_up(self):
        self.channel += 1
        if self.channel > 99:
            self.channel = 0
        print("\nChannel ", self.channel)

    def switch_channel_down(self):
        self.channel -= 1
        if self.channel < 0:
            self.channel = 99
        print("\nChannel ", self.channel)

    def specify_channel(self):
        self.channel = int(input("\nChoose channel ---> "))
        print("Channel ", self.channel)
