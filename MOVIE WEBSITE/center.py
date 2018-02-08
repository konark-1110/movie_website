import fresh_tomatoes
import media


toy_story=media.Movie("Toy Story 3",
                          "A story of a boy and his toys that come to life",
                          "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                          "https://www.youtube.com/watch?v=ZZv1vki4ou4")
#print(toy_story.storyline)
avatar=media.Movie("Avatar",
                   "A marine on an alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")

skyscraper=media.Movie("Skyscraper",
                       "A retired army official struggles to protect his family",
                       "https://upload.wikimedia.org/wikipedia/en/6/6e/Skyscraper_%282018%29_film_poster.png",
                       "https://www.youtube.com/watch?v=t9QePUT-Yt8")

atomic_blonde=media.Movie("Atomic Blonde",
                          "A american spy tries to unfold truth",
                          "https://upload.wikimedia.org/wikipedia/en/b/b5/Atomic_Blonde_poster.jpg",
                          "https://www.youtube.com/watch?v=yIUube1pSC0")

mission_impossible_fallout=media.Movie("Mission Impossible Fallout",
                                       "amdduisabksdb",
                                       "https://upload.wikimedia.org/wikipedia/en/f/ff/MI_%E2%80%93_Fallout.jpg",
                                       "https://www.youtube.com/watch?v=wb49-oV0F78")


#print(avatar.storyline)
#avatar.show_trailer()
movies=[toy_story,avatar,skyscraper,atomic_blonde,mission_impossible_fallout]
fresh_tomatoes.open_movies_page(movies)   
#print(media.Movie.__doc__)
