# Вебинар

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __contains__(self, item):
        for user in item:
            if self.nickname == user.nickname:




class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self._time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = 0

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                ...

    def register(self, nickname, password, age):
        tem_user = User(nickname, password, age)
        if tem_user not in self.users:
            self.users.append(tem_user)
        else:
            print()


    def log_out(self):
        ...

    def add(self):
        ...

    def get_videos(self):
        ...

u1 = User()
v1 = Video()
urban_tube = UrTube()
