class Profile:

    like_count = 0

    liked_people = []

    def __init__(self, user_name: str, name: str, bio: str):

        self.user_name = user_name
        self.name = name
        self.bio = bio



    def print_info(self):

        return f"User_name: @{self.user_name},\n Name: {self.name},\n bio: {self.bio}"

    def post_like(self, liked_username):

        self.liked_people.append(liked_username)

        self.like_count += 1

        return f"Hey, {self.name}. {liked_username} liked your post"


    def post_dislike(self, unliked_person):

        if self.before_liked(unliked_person):

            self.like_count -= 1
            return self.like_count


        return self.like_count



    def get_current(self):
        return self.like_count

    def before_liked(self, name):

        if name in self.liked_people:
            self.liked_people.remove(name)
            return True

        return False

    def __str__(self):
        return f"{self.bio}"






emil = Profile("emil", "Emilbek", "love is love")
nurbolot = Profile("nurbo", "Nurbolot", "To be is to do")
david = Profile("dave", "David", "my bio")

users = [emil, nurbolot, david]
print(emil)


#for i in range(len(users)):
 #   print(users[i].print_info())


def like(user_name, person):
    output = person.post_like(user_name.user_name)
    print(output)

def dislike(user_name, person):

    output = person.post_dislike(person.user_name)
    print(output)

dislike(emil, nurbolot)

like(users[0], users[1])

dislike(emil, nurbolot)

like(emil, nurbolot)

        
print(emil.like_count)
print(nurbolot.like_count)
print(david.like_count)
print(nurbolot)
print(emil)
