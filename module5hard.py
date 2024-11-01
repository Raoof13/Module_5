# Задание "Свой YouTube"

import time


class User:

    def __init__(self, nickname: str, password: str, age: int):
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

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"


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


    def watch_video(self, name_film: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        if _film.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for i in range(_film.duration):
                    print(_film, end=' ')
                    time.sleep(1)
                    _film.time_now += 1
                _film.time_now = 0
                print('Конец видео')

if __name__ == '__main__':
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