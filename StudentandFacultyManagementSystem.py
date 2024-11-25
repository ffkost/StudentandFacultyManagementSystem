
class Student:
    def __init__(self,ime,prezime,ocenki = [] ):
        self.ime = ime
        self.prezime = prezime
        self.ocenki = ocenki

    def __str__(self):
        return f" Ime:  {self.ime} Prezime: {self.prezime} prosek: {self.prosek()} "

    def pozdrav(self):
        return f" Pozdrav do site jas sum {self.ime} {self.prezime} {self.ocenki}"

    def suma(self):
        return sum(self.ocenki)
    def prosek(self):                            #
        return sum(self.ocenki)/len(self.ocenki) #
    def prosek(self):
        return sum(self.ocenki)/len(self.ocenki)

    # def prosek(self):
    #     return self.suma()/len(self.ocenki)  #

    def dodadi_ocenka(self,ocenka):
        self.ocenki.append(ocenka)

    def izbrisi_ocenka(self, index):
        self.ocenki.pop(index)

    def popravi(self, index): # poprava ocenka na index za 1 pogolema
        ocenka = self.ocenki[index]
        ocenka = ocenka + 1
        self.ocenki[index] = ocenka


    def vnesi_ocenki(self, broj_ocenki):
        for i in range (0, broj_ocenki):
            ocenka = int(input(f"Vnesi ocenka {i + 1}:  "))
            self.ocenki.append(ocenka)


student1 = Student("Filip","Kostadinov", [7, 7, 7, 7, 7])
print(student1.pozdrav())
print(student1.prosek())
#student1.dodadi_ocenka(5)
#student1.izbrisi_ocenka(2)
student1.popravi(3)
print(student1.pozdrav())

class Fakultet:
    def __init__(self,ime, studenti = []):
        self.ime = ime
        self.studenti = studenti

    #def pozdrav(self):
        #print(f"Fakultet:  {self.ime}, {self.iminja_na_studenti()} so prosek {self.prosek()}")
        self.iminja_na_studenti()


    #def iminja_na_studenti(self): #
        #lista_od_imina = []
        #for i in self.studenti:
            #lista_od_imina.append(i.ime)
        #return lista_od_imina

    def iminja_na_studenti(self):

        for i in self.studenti:
            print(i)

    def vnesi_studenti(self, broj_na_studenti):
        for i in range(0, broj_na_studenti):
            ime = input("Vnesete ime na studentot:   ")
            prezime = input("Vnesete prezime na studentot   ")
            a = Student(ime, prezime)
            broj_na_ocenki = int(input("Vnesi broj na ocenki:   "))
            a.vnesi_ocenki(broj_na_ocenki)
            self.studenti.append(a)
        print(f"{broj_na_studenti} se zapisaa vo fakultetot    ")

    def prosek(self): #
        lista = []
        for i in self.studenti:
            lista.append(i.prosek())
        return sum(lista)/len(lista)



#filip = Student("Filip", "Kostadinov")
#filip.vnesi_ocenki(5)
#print(filip.pozdrav())

studenti_1 = []

#broj_na_studenti = int(input("Vnesete broj na studenti:   "))
#for i in range(0, broj_na_studenti):
    #ime = input("Vnesete ime od student:   ")
    #prezime = input("Vnesete prezime od student:   ")
    #broj_na_ocenki = int(input("Vnesete broj na ocenki:   "))
    #student = Student(ime, prezime)
    #student.vnesi_ocenki(broj_na_ocenki)
    #studenti_1.append(student)

FEIT = Fakultet("Fakultet za elektrotehnika i informaciski tehnologii ", studenti_1)
FEIT.vnesi_studenti(2)
FEIT.pozdrav()

# filip = Student( "Filip", "Kostadinov", [1,2,3,4,5,6,7,8,9,10,10])
# print(filip) # zadaca 1

FEIT = Fakultet("Fakultet za elektrotehnika i informaciski tehnologii ")
FEIT.vnesi_studenti(2)
FEIT.pozdrav()
