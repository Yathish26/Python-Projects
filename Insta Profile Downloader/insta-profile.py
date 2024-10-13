import instaloader

ig = instaloader.Instaloader()

user = input("Enter the Username: ")

ig.download_profile(user,profile_pic_only=False)