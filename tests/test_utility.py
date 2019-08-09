"""
A micro-service passing back enhanced information from Astronomy
Picture of the Day (APOD).

Adapted from code in https://github.com/nasa/planetary-api

Created on August 8, 2019

@author=samyanez94 @email=samuelyanez94@gmail.com
"""

import unittest

from utility import additional_fields

test_apod = {
    "concepts": "concept_tags functionality turned off in current service",
    "date": "2019-07-10",
    "explanation": "Over 4000 planets are now known to exist outside our Solar System. Known as exoplanets, this milestone was passed last month, as recorded by NASA's Exoplanet Archive. The featured video highlights these exoplanets in sound and light, starting chronologically from the first confirmed detection in 1992.  The entire night sky is first shown compressed with the central band of our Milky Way Galaxy making a giant U.  Exoplanets detected by slight jiggles in their parents-star's colors (radial velocity) appear in pink, while those detected by slight dips in their parent star's brightness (transit) are shown in purple. Further, those exoplanets imaged directly appear in orange, while those detected by gravitationally magnifying the light of a background star (microlensing) are shown in green.  The faster a planet orbits its parent star, the higher the accompanying tone played. The retired Kepler satellite has discovered about half of these first 4000 exoplanets in just one region of the sky, while the new TESS mission is on track to find even more, all over the sky, orbiting the brightest nearby stars.  Finding exoplanets not only helps humanity to better understand the potential prevalence of life elsewhere in the universe, but also how our Earth and Solar System were formed.   Follow APOD on Instagram in: English, Indonesian, or Persian",
    "media_type": "video",
    "service_version": "v1",
    "title": "4000 Exoplanets",
    "url": "https://www.youtube.com/embed/aiFD_LBx2nM?rel=0"
  }

expected_apod = {
    "concepts": "concept_tags functionality turned off in current service",
    "date": "2019-07-10",
    "explanation": "Over 4000 planets are now known to exist outside our Solar System. Known as exoplanets, this milestone was passed last month, as recorded by NASA's Exoplanet Archive. The featured video highlights these exoplanets in sound and light, starting chronologically from the first confirmed detection in 1992.  The entire night sky is first shown compressed with the central band of our Milky Way Galaxy making a giant U.  Exoplanets detected by slight jiggles in their parents-star's colors (radial velocity) appear in pink, while those detected by slight dips in their parent star's brightness (transit) are shown in purple. Further, those exoplanets imaged directly appear in orange, while those detected by gravitationally magnifying the light of a background star (microlensing) are shown in green.  The faster a planet orbits its parent star, the higher the accompanying tone played. The retired Kepler satellite has discovered about half of these first 4000 exoplanets in just one region of the sky, while the new TESS mission is on track to find even more, all over the sky, orbiting the brightest nearby stars.  Finding exoplanets not only helps humanity to better understand the potential prevalence of life elsewhere in the universe, but also how our Earth and Solar System were formed.   Follow APOD on Instagram in: English, Indonesian, or Persian",
    "media_type": "video",
    "thumbnail_url": "https://img.youtube.com/vi/aiFD_LBx2nM/maxresdefault.jpg",
    "title": "4000 Exoplanets",
    "url": "https://www.youtube.com/embed/aiFD_LBx2nM?rel=0",
    "version": "v1"
  }

class TestUtility(unittest.TestCase):

    def test_additional_fields(self):
        self.assertEqual(additional_fields(test_apod, True, 'v1'), expected_apod)

if __name__ == '__main__':
    unittest.main()
