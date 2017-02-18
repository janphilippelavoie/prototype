import glicko2
import math


class Glicko(object):
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
        out_str = "(rating : {}, rd : {}, vol : {})".format(self.rating, self.rd, self.vol)
        return out_str


def get_posterior_ratings(g_1, g_2, score_1):
    """Return posterior ratings.

    Parameters
    ----------
    g_1 : Glicko
        Rating of player 1

    g_2 : Glicko
        Rating of player 2

    score_1 : float
        Score achieved by player 1
    
    Info
    ----
    The value of score_1 is assume to be any real between 0.0 and 1.0 where 
    0.0 mean complete failure and 1.0 complete success.    
    """
    p1 = glicko2.Player(g_1.rating, g_1.rd, g_1.vol)
    p2 = glicko2.Player(g_2.rating, g_2.rd, g_2.vol)
    p1.update_player([g_2.rating], [g_2.rd], [score_1])
    p2.update_player([g_1.rating], [g_1.rd], [1.0 - score_1])
    new_r_1 = Glicko(p1.getRating(), p1.getRd(), p1.vol)
    new_r_2 = Glicko(p2.getRating(), p2.getRd(), p2.vol)
    return new_r_1, new_r_2


def expected_score(g_1, g_2):
    """ Calculate expected score

    :param g_1: Glicko
    :param g_2: Glicko
    :return: float

    The expected score is from the point of view of g_1.
    """
    rd_1 = g_1.rd
    rd_2 = g_2.rd

    r_1 = g_1.rating
    r_2 = g_2.rating

    e_s = 1.0 / (1.0 + 10.0 ** (-g_function(math.sqrt(rd_1 ** 2 + rd_2 ** 2)) * (r_1 - r_2) / 400.0))

    return e_s


def g_function(rd):
    """ Part of the glicko algorithm

    :param rd: float
    :return: float

    See www.glicko.net for details.
    """
    q = math.log(10) / 400
    g_of_rd = 1.0 / math.sqrt(1.0 + 3.0 * q ** 2 * rd ** 2 / math.pi ** 2)
    return g_of_rd
