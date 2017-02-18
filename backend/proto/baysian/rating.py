import glicko2


class Glicko:
    """ Struct like structure representing a glicko2 rating.
    """

    def __init__(self, rating=1500.0, rd=350.0, vol=0.06):
        """Parameters
        ----------
        rating : float
            expected value of the rating
            
        rd : float
            rating deviation
        
        vol : float
            volatility
        """
        self.rating = rating
        self.rd = rd
        self.vol = vol

    def __str__(self):
        out_str = "(rating : %(rating)f, rd : %(rd)f, vol : %(vol)f)" \
                  % {'rating': self.rating, 'rd': self.rd, 'vol': self.vol}
        return (out_str)

    @property
    def __repr__(self):
        out_str = "Rating(rating=%(rating)f, rd=%(rd)f, vol=%(vol)f)" \
                  % {'rating': self.rating, 'rd': self.rd, 'vol': self.vol}
        return (out_str)


def post_ratings(r_1, r_2, score_1):
    """Return posterior ratings.
    
    Parameters
    ----------
    r_1 : Glicko
        Rating of player 1

    r_2 : Glicko
        Rating of player 2

    score_1 : float
        Score achieved by player 1
    
    Info
    ----
    The value of score_1 is assume to be any real between 0.0 and 1.0 where 
    0.0 mean complete failure and 1.0 complete success.    
    """
    p1 = glicko2.Player(r_1.rating, r_1.rd, r_1.vol)
    p2 = glicko2.Player(r_2.rating, r_2.rd, r_2.vol)

    p1.update_player([r_2.rating], [r_2.rd], [score_1])
    p2.update_player([r_1.rating], [r_1.rd], [1.0 - score_1])

    new_r_1 = Rating(p1.getRating(), p1.getRd(), p1.vol)
    new_r_2 = Rating(p2.getRating(), p2.getRd(), p2.vol)

    return new_r_1, new_r_2
