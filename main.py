import classes

if __name__ == '__main__':
    universityName = "Politecnico di Torino"
    poli = classes.University(universityName)

    poli.setRector("Guido", "Saracco")
    print(f"Rector of {poli.getName()} : {poli.getRector()}")

    s1 = poli.enroll("Mario","Rossi")
    s2 = poli.enroll("Giuseppe","Verdi")

    print (f"Enrolled students {s1} , {s2}")
    print(f"s1 = {poli.student(s1)}")
    print(f"s2 = {poli.student(s2)}")

    macro = poli.activate("Macro Economics", "Paul Krugman")
    oop = poli.activate("Object Oriented Programming", "James Gosling")

    print(f"Activated courses  {macro}   and   {oop}")

    poli.register(s1, macro)

    poli.register(s2, macro)
    poli.register(s2, oop)

    print(poli.listaIscritti(macro))
    print(poli.corsiFrequentati(s2))