class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # 기본값 제공 (계정 생성 후 팔로워 팔로잉 0)
        self.following = 0

    def follow(self, user):
        user.followers += 1 # 매개 변수 username 의 팔로워 + 1
        self.following += 1 # 메소드 앞 계정 팔로잉 + 1 ex) user_1.follow(user_2) user_2는 팔로잉 + 1, user_1은 팔로워 + 1




user_1 = User("001", "kkr")
user_2 = User("002", "aaa")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)