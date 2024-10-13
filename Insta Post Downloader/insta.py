import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Ask the user for their Instagram login credentials
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

# Login to Instagram
try:
    loader.login(username, password)
    print("Login successful!")

    # Ask the user for the profile from which they want to download posts
    profile_username = input("Enter the Instagram username to download all posts from: ")

    # Load the profile
    try:
        profile = instaloader.Profile.from_username(loader.context, profile_username)

        # Download all posts of the profile
        print(f"Downloading all posts from '{profile_username}'...")
        for post in profile.get_posts():
            loader.download_post(post, target=profile_username)

        print("All posts have been downloaded successfully!")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{profile_username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

except instaloader.exceptions.BadCredentialsException:
    print("Login failed! Please check your username and password.")
except Exception as e:
    print(f"An error occurred during login: {e}")
