import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_ok(self):
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_rahan_lataus_ok(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 1100)
    
    def test_saldo_vahenee_rahaa_ottaessa(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 900)
    def test_saldo_ei_muutu_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo, 1000)
    def test_lataa_rahaa_palauttaa_true_jos_ok(self):
        paluuarvo = self.maksukortti.ota_rahaa(100)
        self.assertTrue(paluuarvo)
    def test_lataa_rahaa_palauttaa_false_jos_ei_ok(self):
        paluuarvo = self.maksukortti.ota_rahaa(1100)
        self.assertFalse(paluuarvo)

    def test_saldo_euroina_palauttaa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
    def test_str_metodi(self):
        kortti = Maksukortti(200)
        self.assertEqual(str(kortti), 'Kortilla on rahaa 2.00 euroa')