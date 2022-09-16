class Character:

    def __init__(self, name, photo, short):
        self.name=name
        self.photo=photo
        self.short=short


    #### Accessor Methods ####

    def get_name(self):
        return self.name

    def get_photo(self):
        return self.photo

    def get_short(self):
        return self.short


    #### Mutator Methods ####
    def set_name(self, name):
        self.name = name

    def set_photo(self, photo):
        self.photo = photo

    def set_short(self, short):
        self.short = short
