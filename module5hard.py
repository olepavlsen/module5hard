import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


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
        self.current_user = None

    def add(self, *args):
        ver_video = False
        for i in args:
            video = [i.title, i.duration, i.time_now, i.adult_mode]
            if not self.videos:
                self.videos.append(video)
            else:
                for j in self.videos:
                    if i.title != j[0]:
                        ver_video = True
                    else:
                        ver_video = False
                    break
                if ver_video:
                    self.videos.append(video)

    def get_videos(self, seek_video):
        self.seek_video = seek_video.lower()
        self.my_seek = []
        for i in self.videos:
            s_str = i[0]
            self.s_str = s_str.lower()
            if self.s_str.find(self.seek_video) != -1:
                self.my_seek.append(i[0])
        return self.my_seek

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.user = [self.nickname, self.password, self.age]
        self.ver_user = 0
        for i in self.users:
            if i[0] == self.nickname:
                self.log_in(self.nickname, self.password)
        if self.ver_user == 0:
            self.users.append(self.user)
            self.log_in(self.nickname, self.password)
        elif self.ver_user == 1:
            self.log_in(self.nickname, self.password)
        elif self.ver_user == 2:
            print(f'Пользователь {self.nickname} уже существует')

    def log_in(self, login, password):
        self.login = login
        self.password = password
        for i in self.users:
            if i[0] == self.login and i[1] == self.password:
                self.current_user = self.login
                self.ver_user = 1
            elif i[0] != self.login or i[1] != self.password:
                self.ver_user = 2
        return self.ver_user

    def watch_video(self, movie):
        self.movie = movie
        if self.current_user == None:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if i[0] == self.movie and i[3] != True:
                    self.scale = i[1]
                    self.time_ = i[2]
                    for j in range(self.scale):
                        self.time_ = j + 1
                        print(self.time_, end=" ")
                        time.sleep(1)
                    print(f'Конец видео')
                elif i[0] == self.movie and i[3] == True:
                    self.scale = i[1]
                    self.time_ = i[2]
                    if self.age > 18:
                        for j in range(self.scale):
                            self.time_ = j + 1
                            print(self.time_, end=" ")
                            time.sleep(1)
                        print(f'Конец видео')
                    else:
                        print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                        self.log_out()

    def log_out(self):
        self.current_user = None
        return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# Добавление видео
ur.add(v1, v2)
#
# # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# #
# # # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# #
# # # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
