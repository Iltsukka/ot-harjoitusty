import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")
    def test_konstruktori_asettaa_saldon_oikein(self):
        # alustetaan maksukortti, jossa on 10 euroa (1000 senttiä)
        kortti = Maksukortti(1000)
        vastaus = str(kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.50 euroa")
    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)
    
    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(self.kortti.saldo_euroina(), 35.0)

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(self.kortti.saldo_euroina(), 150.0)
    
    def test_maukkaasti_syominen_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(300)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo, 300)
    
    def test_ei_voi_ladata_negatiivista_summaa(self):
        self.kortti.lataa_rahaa(-200)

        self.assertEqual(self.kortti.saldo, 1000)
    
    def test_edullisen_lounaan_saa_ostettua(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()
        self.assertEqual(kortti.saldo, 0)
    
    def test_maukkaan_lounaan_saa_ostettua(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()
        self.assertEqual(kortti.saldo, 0)
    
