<!DOCTYPE html>
<html>
<head>
<link href=".css.css" rel="stylesheet" type="text/css">

<title>OOP Gestione Ateneo</title>
</head>
<body>

<h1 style="text-align: center;">Gestione Ateneo</h1>
<br>
Progettare ed implementare un programma che possa gestire corsi, docenti e studenti di un ateneo. 
Tutte le classi devono appartenere al pacakge <b>university</b>.
<p>
Il programma interagisce con i propri clienti attraverso la classe di facciata <b>University</b>.

<h2 id="R1">R1. Ateneo</h2>
<p>
La classe principale &egrave; <b>University</b> che riceve, 
come parametro del costruttore, il nome dell'ateneo.
</p><p>
Il nome dell'ateneo &egrave; leggibile tramite il metodo getter <b>getName()</b>.
</p><p>
&Egrave; possibile definire il nome del rettore di un ateneo tramite il metodo
<b>setRector()</b> che riceve come parametri nome e cognome del rettore.
</p><p>
Il metodo getter <b>getRector()</b> restituisce nome e cognome del rettore 
concatenati e separati da uno spazio (<i>" "</i>).
</p>

<h2 id="R2">R2. Studenti</h2>
<p>
&Egrave; possibile inserire le informazioni relative ad un nuovo studente 
tramite il metodo <b>enroll()</b> della classe <i>University</i>, che riceve come parametri
il nome ed il cognome dello studente; il metodo restituisce il numero di matricola che &egrave; 
stato assegnato allo studente.<br>
I numeri di matricola vengono assegnati, in maniera progressiva per ciascun ateneo a partire 
dal numero 10000. Quindi il primi studente iscritto ad ogni ateneo avrÃ  matricola <i>10000</i>
</p><p>
Per ottenere le informazioni relative ad uno studente si utilizza il metodo
<b>student()</b> che riceve come parametro la matricola e restituisce una 
stringa composta da numero di matricola, nome e cognome separati da spazi,
es. <i>"10000 Giuseppe Verdi"</i>.
</p>

<ul class="hint">
<li>Si assuma che ciascun ateneo non possa contenere pi&ugrave; di 1000 studenti.
</ul>

<h2 id="R3">R3. Insegnamenti</h2>
<p>
Per definire un nuovo insegnamento si utilizza il metodo <b>activate()</b> che riceve come 
parametri il titolo del corso e il nome del docente titolare. Il metodo restituisce un
intero che corrisponde al codice del corso. I codici vengono assegnati progressivamente a 
partire da 10.
</p><p>
Per conoscere le informazioni relative ad un corso si usa il metodo <b>course()</b> che riceve 
come parametro il codice del corso e resituisce una stringa contenente codice, titolo e titolare
del corso, separati da virgole, es. <i>"10,Programmazione a Oggetti,James Gosling"</i>.
</p>

<ul class="hint">
<li>Si assuma che ciascun ateneo non possa attivare pi&ugrave; di 50 insegnamenti.
</ul>


<h2 id="R4">R4. Iscritti agli insegnamenti</h2>
<p>
Gli studenti possono essere iscritti agli insegnamenti tramite il metodo <b>register()</b> che 
riceve come parametro la matricola dello studente ed il codice dell'insegnamento.
</p><p>
Per ottenere l'elenco degli iscritti ad un insegnamento &egrave; disponibile il metodo
<b>listAttendees()</b> che riceve come parametro il codice dell'insegnamento e restituisce una
stringa contenente l'elenco degli studenti iscritti.
</p><p>
Gli studenti compaiono uno per riga (le righe sono terminate da un a-capo <i>"\n"</i>) secondo
il formato descritto al punto <a href="#R2">R2</a>.
</p><p>
Data la matricola di uno studente, tramite il metodo <b>studyPlan()</b>, &egrave; possibile conoscere
l'elenco degli insegnamenti a cui &egrave; iscritto, gli insegnamenti sono descritti come 
al <a href="#R3">punto precedente</a>.
</p>

<ul class="hint">
<li>Si assuma che ciascuno studente non possa essere iscritto a pi&ugrave; di 25 insegnamenti 
e che un insegnamento non possa avere pi&ugrave; di 100 iscritti.
</ul>
<footer>
Version 1.2.1 - March 26, 2020
</footer>
</body>
</html>
