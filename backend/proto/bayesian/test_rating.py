import unittest
import rating


class TestGlicko(unittest.TestCase):
    def test_constructor_default(self):
        g = rating.Glicko()
        self.assertEqual(g.rating, 1500.0)
        self.assertEqual(g.rd, 350.0)
        self.assertEqual(g.vol, 0.06)

    def test_constructor_defined(self):
        g = rating.Glicko(1600.0, 400.0, 0.04)
        self.assertEqual(g.rating, 1600.0)
        self.assertEqual(g.rd, 400.0)
        self.assertEqual(g.vol, 0.04)


class TestExpectedScore(unittest.TestCase):
    def test_mirror_match(self):
        g_1 = rating.Glicko()
        g_2 = rating.Glicko()
        e_r = rating.expected_score(g_1, g_2)
        self.assertEqual(e_r, 0.5)

    def test_g_1_advantage(self):
        g_1 = rating.Glicko(rating=1600.0)
        g_2 = rating.Glicko(rating=1400.0)
        e_r = rating.expected_score(g_1, g_2)
        self.assertGreater(e_r, 0.5)

    def test_g_2_advantage(self):
        g_1 = rating.Glicko(rating=1400.0)
        g_2 = rating.Glicko(rating=1600.0)
        e_r = rating.expected_score(g_1, g_2)
        self.assertLess(e_r, 0.5)


class TestPosteriorRatings(unittest.TestCase):
    def test_g_1_win(self):
        g_1 = rating.Glicko(rating=1500)
        g_2 = rating.Glicko(rating=1500)
        p_g_1, p_g_2 = rating.get_posterior_ratings(g_1, g_2, 1.0)
        self.assertGreater(p_g_1.rating, g_1.rating)
        self.assertLess(p_g_2.rating, g_2.rating)

    def test_g_1_lose(self):
        g_1 = rating.Glicko(rating=1500)
        g_2 = rating.Glicko(rating=1500)
        p_g_1, p_g_2 = rating.get_posterior_ratings(g_1, g_2, 0.0)
        self.assertGreater(p_g_2.rating, g_2.rating)
        self.assertLess(p_g_1.rating, g_1.rating)

    def test_draw(self):
        g_1 = rating.Glicko(rating=1550)
        g_2 = rating.Glicko(rating=1450)
        p_g_1, p_g_2 = rating.get_posterior_ratings(g_1, g_2, 0.5)
        self.assertGreater(p_g_2.rating, g_2.rating)
        self.assertLess(p_g_1.rating, g_1.rating)
        self.assertGreater(p_g_1.rating, p_g_2.rating)


class TestGFunction(unittest.TestCase):
    def test_value(self):
        g_th = 0.6690693971819845  # Calculated with rating.g_function. Might need value from another source.
        g_ex = rating.g_function(350)
        self.assertAlmostEqual(g_ex, g_th)

if __name__ == '__main__':
    unittest.main()
