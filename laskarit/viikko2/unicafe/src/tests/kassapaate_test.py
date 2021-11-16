import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class testKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.get_kassassa_rahaa(), 100000)

    def test_luodun_kassapaatteen_myydyt_lounaat_on_oikea(self):
        self.assertEqual(self.kassapaate.get_edulliset() + self.kassapaate.get_maukkaat(), 0)

    def test_lataa_rahaa_kortille_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 10)
        self.assertEqual(self.kassapaate.get_kassassa_rahaa(), 100010)
    
    def test_negatiivinen_kortinlataus_ei_muuta_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kassapaate.get_kassassa_rahaa(), 100000)

    def test_syo_edullisesti_kateisella_raha_riittaa_ja_vaihtoraha_on_oikea(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.get_kassassa_rahaa(), 100240)

    def test_syo_edullisesti_kateisella_raha_riittaa_myydyt_lounaat_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.get_edulliset(), 1)

    def test_syo_edullisesti_kateisella_raha_ei_riita_rahamaara_ei_muutu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.get_edulliset(), 0)

    def test_syo_maukkaasti_kateisella_raha_riittaa_ja_vaihtoraha_on_oikea(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.get_kassassa_rahaa(), 100400)

    def test_syo_maukkaasti_kateisella_raha_riittaa_myydyt_lounaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.get_maukkaat(), 1)

    def test_syo_maukkaasti_kateisella_raha_ei_riita_rahamaara_ei_muutu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.get_maukkaat(), 0)

    

    def test_syo_edullisesti_kortilla_raha_riittaa_ja_palauttaa_True(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(tulos)


    def test_syo_edullisesti_kortilla_raha_riittaa_myydyt_lounaat_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.get_edulliset(), 1)

    def test_syo_edullisesti_kortilla_raha_ei_riita_tulos_on_False(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertFalse(tulos)
        self.assertEqual(self.kassapaate.get_edulliset(), 4)

    def test_syo_maukkaasti_kortilla_raha_riittaa_ja_tulos_on_True(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(tulos, 100)
    

    def test_syo_maukkaasti_kortilla_raha_riittaa_myydyt_lounaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.get_maukkaat(), 1)

    def test_syo_maukkaasti_kortilla_raha_ei_riita_tulos_on_False(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertFalse(tulos)
        self.assertEqual(self.kassapaate.get_maukkaat(), 2)

    def test_syo_edullisesti_kortilla_rahamaara_ei_muut(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.get_kassassa_rahaa(), 100000)

    