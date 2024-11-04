# Задание "Свой YouTube"

import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


    def __eq__(self, other):
        return self.nickname == other.nickname

    def __str__(self):
        return f"{self.nickname}"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

    def __str__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        tem_user = User(nickname, password, age)
        if tem_user not in self.users:
            self.users.append(tem_user)
            self.current_user = tem_user
        else:
            print(f"Пользователь {nickname} уже существует.")


    def log_out(self):
            self.current_user = None

    def add(self, *args):
        for new_video in args:
            if new_video not in self.videos:
                self.videos.append(new_video)

    def get_videos(self, search_word: str):
        list_of_titles = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                list_of_titles.append(video.title)
        return list_of_titles

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(1, video.duration + 1):
                    print(second, end=' ')
                    time.sleep(1)
                print("Конец видео")
                return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')