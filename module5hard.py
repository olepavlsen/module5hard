import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *new_video):
        for video in new_video:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, seek_video):
        self.my_seek = []
        for video in self.videos:
            if seek_video.lower() in video.title.lower():
                self.my_seek.append(video.title)
        return self.my_seek

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user not in self.users:
            self.users.append(user)
            self.current_user = user
        else:
            print(f'Пользователь {nickname} уже существует')  # for user in self.videos:
            return

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return self.current_user

    def watch_video(self, movie):
        if self.current_user is None:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if video.title == movie and not video.adult_mode:
                    for i in range(video.duration):
                        video.time_now = i + 1
                        print(video.time_now, end=" ")
                        time.sleep(1)
                    print(f'Конец видео')
                elif video.title == movie and video.adult_mode:
                    if self.current_user.age >= 18:
                        for j in range(video.duration):
                            video.time_now = j + 1
                            print(video.time_now, end=" ")
                            time.sleep(1)
                        print(f'Конец видео')
                    else:
                        print(f'Вам нет 18 лет, пожалуйста покиньте страницу')

    def log_out(self):
        self.current_user = None
        return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
