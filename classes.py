STARTING_COURSE = 10
STARTING_ID = 10000


class University:
    def __init__(self,name):
        self.name = name
        self.rector = []
        self.enrolled = []
        self.corsiAttivi = []

    def getName(self):
        return self.name

    def setRector(self,nome,cognome):
        self.rector.append(nome)
        self.rector.append(cognome)

    def getRector(self):
        return self.rector[0] + " " + self.rector[1]

    def enroll(self,nome,cognome):
        currID = len(self.enrolled) + STARTING_ID
        self.enrolled.append(Studente(nome, cognome,currID ))
        return currID

    def student(self,matricola):
        for studente in self.enrolled:
            if studente.ID == matricola:
                return studente.asString()
        #return self.enrolled[matricola-STARTING_ID].asString()

    def activate(self,title,prof):
        currID = len(self.corsiAttivi) + STARTING_COURSE
        self.corsiAttivi.append(Corsi(title,prof,currID))
        return currID

    def course(self,courseID):
        for corso in self.corsiAttivi:
            if corso.ID == courseID :
                return corso.asString
        #return self.corsiAttivi[courseID-STARTING_COURSE].asString()

    def register(self,matricola,courseID):
        s = None
        for studente in self.enrolled :
            if studente.ID == matricola:
                s = studente
        for corso in self.corsiAttivi :
            if corso.ID == courseID :
                corso.iscrivi(s)

    def listaIscritti(self, macro):
        for c in self.corsiAttivi :
            if macro == c.ID :
                return c.listaIscritti()

    def corsiFrequentati(self,matricola):
        res = ""
        for c in self.corsiAttivi:
            if (c.isIscritto(matricola)):
                res += c.asString() + "\n"
        return res


class Studente:
    def __init__(self,nome,cognome,ID):
        self.nome = nome
        self.cognome = cognome
        self.ID = ID

    def asString(self):
        return str(self.ID) + " " + self.nome + " " + self.cognome


class Corsi:
    def __init__(self,title,prof,courseID):
        self.title = title
        self.prof = prof
        self.ID = courseID
        self.iscritti = []

    def asString(self):
        return str(self.ID) + "," + self.title + "," + self.prof

    def iscrivi(self,studente):
        self.iscritti.append(studente)

    def isIscritto(self,matricola):
        for s in self.iscritti:
            if s.ID == matricola:
                return True
        return False

    def listaIscritti(self):
        res = ""
        for iscritto in self.iscritti:
            stud = iscritto.asString()
            res += stud + "\n"
        return res