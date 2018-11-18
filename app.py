from flask import Flask, render_template, redirect, url_for
import csv

application = Flask(__name__)

class Person:
	def __init__(self, name, age, bg, br, brt, dam, dege, degr, dom, exi, exp, mas, mast, nmon, own, pet, hun, pre, rig, rb, sad, slv, sub, swt, van, voy):
		self.name = name
		self.results = {
				"Ageplayer": age,
				"Boy/Girl": bg,
				"Brat": br,
				"Brat Tamer": brt,
				"Daddy/Mommy": dam,
				"Degradee": dege,
				"Degrader": degr,
				"Dominant": dom,
				"Exhibitionist": exi,
				"Experimentalist": exp,
				"Masochist": mas,
				"Master/Mistress": mast,
				"Non-monogamist": nmon,
				"Owner": own,
				"Pet": pet,
				"Hunter": hun,
				"Prey": pre,
				"Rigger": rig,
				"Rope Bunny": rb,
				"Sadist": sad,
				"Slave": slv,
				"Submissive": sub,
				"Switch": swt,
				"Vanilla": van,
				"Voyeur": voy
				}

people = []
category = ["Name", "Ageplayer", "Boy/Girl", "Brat", "Brat Tamer", "Daddy/Mommy", "Degradee", "Degrader", "Dominant", "Exhibitionist", "Experimentalist", "Masochist", "Master/Mistress", "Non-monogamist", "Owner", "Pet", "Hunter", "Prey", "Rigger", "Rope Bunny", "Sadist", "Slave", "Submissive", "Switch", "Vanilla", "Voyeur"]
def assign():
	
	with open('averages.csv', mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		count = 0
		for row in csv_reader:
			if count == 0:
				print(f'names are{", ".join(row)}')
				count+=1
			else:
				people.append(Person(row["Name"], row["Ageplayer"], row["Boy/Girl"], row["Brat"], row["Brat Tamer"], row["Daddy/Mommy"], row["Degradee"], row["Degrader"], row["Dominant"], row["Exhibitionist"], row["Experimentalist"], row["Masochist"], row["Master/Mistress"], row["Non-monogamist"], row["Owner"], row["Pet"], row["Primal(Hunter)"], row["Primal(Prey)"], row["Rigger"], row["Rope bunny"], row["Sadist"], row["Slave"], row["Submissive"], row["Switch"], row["Vanilla"], row["Voyeur"]))
	
assign()	
print(len(people))

@application.route("/")
def index():
	return redirect(url_for('home'));
	
@application.route("/home")
def home():
	return render_template('home.html')
	
@application.route("/boneless")
def boneless():
	return render_template('boneless.html', people=people, cat=category)


@application.route("/tino")
def tino():
	return render_template('tino.html')

if __name__ == "__main__":
    application.run()