class NFL_Team:

    def __init__(self, name, logo, twitter, hashtag, conf, div, num):
        self.name=name
        self.logo=logo
        self.twitter=twitter
        self.hashtag=hashtag
        self.conf=conf
        self.div=div
        self.num=num

    #### Accessor Methods ####

    def get_name(self):
        return self.name

    def get_logo(self):
        return self.logo

    def get_twitter(self):
        return self.twitter

    def get_hashtag(self):
        return self.hashtag

    def get_conf(self):
        return self.conf

    def get_div(self):
        return self.div

    def get_num(self):
        return self.num

    #### Mutator Methods ####
    def set_name(self, name):
        self.name = name

    def set_logo(self, logo):
        self.logo = logo

    def set_twitter(self, twitter):
        self.twitter = twitter

    def set_hashtag(self, hashtag):
        self.hashtag=hashtag

    def get_conf(self, conf):
        self.conf = conf

    def get_div(self, div):
        self.div = div

    def get_num(self, num):
        self.num=num
