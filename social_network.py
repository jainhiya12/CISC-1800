# Hiya Jain
# Lab 09: The Social Network
# CISC 1800 - Introduction to Computer Programming

class User:
  def __init__(self, username, display_name):
    self.username = username
    self.display_name = display_name
    self.friends = []
    self.posts = []
    
  def __str__(self):
    return f"{self.display_name} ({self.username})"
    
  def add_friend(self, user):
    if user not in self.friends:
      self.friends.append(user)
      user.friends.append(self)
  
  def remove_friend(self, user):
    if user in self.friends:
      self.friends.remove(user)
      user.friends.remove(self)
      
  def create_post(self, content):
    post = Post(self, content)
    self.posts.append(post)
    return post

class Post:
  def __init__(self, user, content):
    self.user = user
    self.content = content
    
  def __str__(self):
     return f"{self.user}: {self.content}"

class SocialNetwork:
  def __init__(self):
    self.users = []

  def register_user(self, username, display_name):
    user = User(username, display_name)
    self.users.append(user)
    return user

  def find_user(self, username):
    for i in range(len(self.users)):
      if self.users[i].username == username:
        return self.users[i]
      else:
       return None

# Test case
# 1. Create a new SocialNetwork object called "network".
network = SocialNetwork()

# 2. Register three users with the network
user1 = network.register_user("user1", "User One")
user2 = network.register_user("user2", "User Two")
user3 = network.register_user("user3", "User Three")

# 3. Make two users friends.
user1.add_friend(user2)

# 4. Create posts for all three users
post1 = user1.create_post("Hello, this is my first post!")
post2 = user2.create_post("Hello, world!")
post3 = user3.create_post("Hey!")

# Print out the users and their posts
for user in network.users:
  for post in user.posts:
    print(post)
