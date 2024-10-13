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

    # Ask the user for the profile whose stories they want to download
    profile_username = input("Enter the Instagram username to download stories from: ")

    # Load the profile
    try:
        profile = instaloader.Profile.from_username(loader.context, profile_username)

        # Check if there are any stories available for the profile
        stories_found = False
        for story in loader.get_stories(userids=[profile.userid]):
            for item in story.get_items():
                loader.download_storyitem(item, target=profile_username)
                stories_found = True

        if not stories_found:
            print("No stories found for this profile.")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{profile_username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

except instaloader.exceptions.BadCredentialsException:
    print("Login failed! Please check your username and password.")
except Exception as e:
    print(f"An error occurred during login: {e}")
