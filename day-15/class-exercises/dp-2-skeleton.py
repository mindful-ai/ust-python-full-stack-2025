"""
--------------------------------------------------------
StreamFlix: Video Streaming Optimization System
--------------------------------------------------------
Objective:
- Use Flyweight Pattern to share movie metadata among users
- Use Proxy Pattern to cache remote video content
--------------------------------------------------------


| Class            | Responsibility                                          |
| ---------------- | ------------------------------------------------------- |
| `MovieFlyweight` | Holds shared movie metadata                             |
| `MovieFactory`   | Creates or reuses `MovieFlyweight` objects              |
| `VideoService`   | Represents a heavy/slow video fetch operation           |
| `VideoProxy`     | Caches fetched video streams                            |
| `UserSession`    | Represents a user watching a movie (uses both patterns) |


"""

# ----------------------------
# Flyweight Pattern
# ----------------------------
class MovieFlyweight:
    """Shared movie metadata (intrinsic data)"""
    def __init__(self, title, genre, director, duration):
        # TODO: Initialize shared properties
        pass


class MovieFactory:
    """Creates or reuses shared MovieFlyweight objects"""
    _movies = {}

    @staticmethod
    def get_movie(title, genre, director, duration):
        # TODO: Implement Flyweight creation and reuse
        pass


# ----------------------------
# Proxy Pattern
# ----------------------------
class VideoService:
    """Simulates slow, costly video fetching"""
    def fetch_video(self, movie_title):
        # TODO: Simulate delay or API call
        pass


class VideoProxy:
    """Proxy adds caching to reduce redundant fetches"""
    def __init__(self):
        # TODO: Initialize cache and real VideoService
        pass

    def get_video(self, movie_title):
        # TODO: Check cache; fetch if not available
        pass


# ----------------------------
# User Session
# ----------------------------
class UserSession:
    """Represents a user watching a movie"""
    def __init__(self, user_name, movie_flyweight, video_proxy):
        # TODO: Initialize user session
        pass

    def watch_movie(self):
        # TODO: Retrieve movie info and stream via proxy
        pass


# ----------------------------
# Main Execution (Testing)
# ----------------------------
if __name__ == "__main__":
    # Step 1: Create Proxy
    video_proxy = VideoProxy()

    # Step 2: Create or reuse movie flyweights
    movie1 = MovieFactory.get_movie("Inception", "Sci-Fi", "Christopher Nolan", "2h 28m")
    movie2 = MovieFactory.get_movie("Inception", "Sci-Fi", "Christopher Nolan", "2h 28m")

    print(f"\nFlyweight objects created: {len(MovieFactory._movies)}")

    # Step 3: Create User Sessions
    user1 = UserSession("Alice", movie1, video_proxy)
    user2 = UserSession("Bob", movie2, video_proxy)

    # Step 4: Simulate watching
    user1.watch_movie()
    user2.watch_movie()
