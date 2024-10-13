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

    # Ask the user for the profile from which they want to download highlight stories
    profile_username = input("Enter the Instagram username to download all highlight stories from: ")

    # Load the profile
    try:
        profile = instaloader.Profile.from_username(loader.context, profile_username)

        # Check if the profile has any highlights
        highlights_found = False
        for highlight in loader.get_highlights(user=profile):
            print(f"Downloading highlights: {highlight.title}")
            for item in highlight.get_items():
                loader.download_storyitem(item, target=f"{profile_username}_highlights_{highlight.title}")
                highlights_found = True

        if not highlights_found:
            print("No highlight stories found for this profile.")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{profile_username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

except instaloader.exceptions.BadCredentialsException:
    print("Login failed! Please check your username and password.")
except Exception as e:
    print(f"An error occurred during login: {e}")
