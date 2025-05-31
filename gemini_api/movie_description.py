from extract_movie_description import get_movie_description

def main():
    print("🎬 Welcome to CineInfinity-Ai Description Generator")
    title = input("Enter movie title: ")
    description = get_movie_description(title)
    print(f"\n📝 Description: {description}")

if __name__ == "__main__":
    main()
