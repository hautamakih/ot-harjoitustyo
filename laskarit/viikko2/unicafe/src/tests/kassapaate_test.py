import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteessa_rahaa_oikea_maara(self):
        rahaa = self.kassapaate.kassassa_rahaa

        self.assertEqual(rahaa, 100000)

    def test_edullisia_lounaita_ei_myyty_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_lounaita_ei_myyty_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliset_lounaat_kateisosto_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaat_lounaat_kateisosto_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edulliset_lounaat_kateisosto_kasvattaa_rahaa_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukkaat_lounaat_kateisosto_kasvattaa_rahaa_kassassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edulliset_lounaat_kateisosto_antaa_vaihtorahat_oikein(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(palautus, 260)

    def test_maukkaat_lounaat_kateisosto_antaa_vaihtorahat_oikein(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(palautus, 100)
    
    def test_edulliset_lounaat_kateisosto_ei_lisaa_rahaa_jos_ei_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaat_lounaat_kateisosto_ei_lisaa_rahaa_jos_ei_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_lounaat_kateisosto_ei_kasvataa_lounaiden_maaraa_jos_ei_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_lounaat_kateisosto_ei_kasvata_lounaiden_maaraa_jos_ei_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliset_lounaat_kateisosto_palauttaa_rahat_jos_ei_rahaa(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(palautus, 200)

    def test_maukkaat_lounaat_kateisosto_palauttaa_rahat_jos_ei_rahaa(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(palautus, 300)

    def test_edulliset_lounaat_korttiosto_toimii_jos_katetta(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_maukkaat_lounaat_korttiosto_toimii_jos_katetta(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_edulliset_lounaat_korttiosto_vahentaa_katetta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_maukkaat_lounaat_korttiosto_vahentaa_katetta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_edulliset_lounaat_korttiosto_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaat_lounaat_korttiosto_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edulliset_lounaat_korttiosto_ei_toimi_jos_ei_katetta(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_maukkaat_lounaat_korttiosto_ei_toimi_jos_ei_katetta(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_edulliset_lounaat_kortin_saldo_ei_muutu_jos_ei_katetta(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)

    def test_maukkaat_lounaat_kortin_saldo_ei_muutu_jos_ei_katetta(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)

    def test_edulliset_lounaat_myytyjen_lounaiden_maara_ei_muutu_jos_ei_katetta(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_lounaat_myytyjen_lounaiden_maara_ei_muutu_jos_ei_katetta(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliset_lounaat_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaat_lounaat_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_lounaat_kassan_saldo_ei_muutu_jos_ei_rahaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaat_lounaat_kassan_saldo_ei_muutu_jos_ei_rahaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_lataaminen_kasvattaa_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 1200)
    
    def test_kortille_ei_ladata_negatiivista_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_kortille_lataaminen_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
    
    def test_kortille_negatiivinen_saldo_ei_muuta_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
