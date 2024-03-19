import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)
    def test_rahamaara_oikein(self):
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    
    def test_alussa_lounaita_myyty_nolla(self):
        self.assertEqual(self.paate.edulliset + self.paate.maukkaat, 0)
    
    def test_edullinen_kasvattaa_rahamaaraa_ja_vaihtoraha_ok(self):
        vaihtoraha = self.paate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.paate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 60)
    def test_lounaat_kasvaa_edullinen(self):
        self.paate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.paate.edulliset,1)
    def test_edullinen_raha_ei_riita(self):
        vaihtoraha = self.paate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
    def test_maukas_kasvattaa_rahamaaraa_ja_vaihtoraha_ok(self):
        vaihtoraha = self.paate.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.paate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 10)
    def test_lounaat_kasvaa_maukas(self):
        self.paate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.paate.maukkaat,1)
    def test_maukas_raha_ei_riita(self):
        vaihtoraha = self.paate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_korttiosto_toimii_edullinen(self):
        paluuarvo = self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(paluuarvo)
        self.assertEqual(self.paate.edulliset, 1)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    def test_korttiosto_toimii_maukas(self):
        paluuarvo = self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(paluuarvo)
        self.assertEqual(self.paate.maukkaat, 1)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    def test_korttiosto_edullinen_ei_rahaa(self):
        kortti = Maksukortti(200)
        self.assertFalse(self.paate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    
    def test_korttiosto_maukas_ei_rahaa(self):
        kortti = Maksukortti(200)
        self.assertFalse(self.paate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(self.paate.maukkaat, 0)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    
    def test_rahan_lataus_kortille(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo, 1100)
        self.assertEqual(self.paate.kassassa_rahaa, 100100)

    def test_rahan_lataus_negatiivinen(self):
        self.assertFalse(self.paate.lataa_rahaa_kortille(self.kortti, -100))
    
    def test_str(self):
        self.assertEqual(self.paate.kassassa_rahaa_euroina(), 1000)
