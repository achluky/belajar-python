class Hewan:
    def name(self):
        pass
    def sleep(self):
        print('Tidur')
    def suara(self):
        pass

class Anjing(Hewan):
    def name(self):
        print('Saya Anjing')
    def sleep(self, status):
        print('Tidur ' + status )
    def suara(self):
        print('Gog Gog')

class Kucing(Hewan):
    def name(self):
        print('Saya Kucing')
    def suara(self):
        print('Meong')
    
class Singa(Hewan):
    def name(self):
        print('Saya Singa')
    def suara(self):
        print('Roar')

class TestHewan:
    def CetakNama(self, hewan):
        hewan.name()
    def goSleep(self, hewan, status):
        hewan.sleep(status)
    def BuatSuara(self, hewan):
        hewan.suara()

TestHewan = TestHewan()
anjing =  Anjing()
kucing =  Kucing()
singa =  Singa()

TestHewan.CetakNama(anjing)
# TestHewan.goSleep(anjing)
TestHewan.goSleep(anjing, 'sendirian')
TestHewan.BuatSuara(anjing)
# TestHewan.CetakNama(kucing)
# TestHewan.goSleep(kucing)
# TestHewan.BuatSuara(kucing)
# TestHewan.CetakNama(singa)
# TestHewan.goSleep(singa)
# TestHewan.BuatSuara(singa)