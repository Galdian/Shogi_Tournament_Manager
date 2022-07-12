

class Player:
    
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating
        self.points = 0
        self.sos = 0
        self.sosos = 0
        self.msos = 0
        self.played_versus = []
        self.results_in_order = []
        self.starting_number = 0
        self.current_place = 0
        self.got_bye = False
        self.tier_group = None
        # self.is_paired = False
    