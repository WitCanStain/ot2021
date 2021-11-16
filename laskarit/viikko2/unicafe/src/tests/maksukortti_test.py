import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.3")

    def test_rahan_ottaminen_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.08")

    def test_rahan_liikaotto_ei_muuta_saldoa(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_otto_palauttaa_True_jos_toimii(self):
        self.assertTrue(self.maksukortti.ota_rahaa(2))

    def test_rahan_otto_palauttaa_False_jos_ei_toimi(self):
        self.assertFalse(self.maksukortti.ota_rahaa(200))