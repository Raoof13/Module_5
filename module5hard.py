# Задание "Свой YouTube"

class User:

    def __init__(self, nickname: str, password: str, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __contains__(self, item):
        for user in item:
            if self.nickname == user.nickname:
                return True
        return False


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = 0

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        tem_user = User(nickname, password, age)
        if tem_user not in self.users:
            self.users.append(tem_user)
        else:
            print(f"Пользователь {tem_user.nickname} уже существует.")
        self.log_in(tem_user.nickname, tem_user.password)


    def log_out(self):
        self.current_user = None

    def add(self, title):
        self.videos.append(title)

    def get_videos(self):
        ...

    def watch_video(self):
        ...
    

u1 = User("Igor", "abc", 19)
# v1 = Video()
urban_tube = UrTube()
