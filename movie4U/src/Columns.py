class COLUMNS:
    DATE = "timestamp"

    class USER:
        ID = "userID"

    class MOVIE:
        ID = "movieID"
        TITLE = "title"
        TAG  = "tag"
        RATING = "rating"
        YEAR = "year"

        class GENRE:
            LABEL = "genres"
            COUNT = "n_genres"

        