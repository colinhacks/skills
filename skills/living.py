import datetime

livingGroups =  \
( 	('-------------SELECT------------',        \
		(\
			('Residence','Residence'),\
		)\
	),\

	('Dorms', \
		(  \
			('Ashdown House', 'Ashdown House'),('Baker House', 'Baker House'),('Burton-Conner House', 'Burton-Conner House'),('East Campus', 'East Campus'),('Eastgate', 'Eastgate'),('Edgerton House', 'Edgerton House'),('Green Hall', 'Green Hall'),('MacGregor House', 'MacGregor House'),('McCormick Hall', 'McCormick Hall'),('New House', 'New House'),('Next House', 'Next House'),('Random Hall', 'Random Hall'),('Senior Haus', 'Senior Haus'),('Sidney-Pacific', 'Sidney-Pacific'),('Simmons Hall', 'Simmons Hall'),('Tang Hall', 'Tang Hall'),('The Warehouse', 'The Warehouse'),('Westgate', 'Westgate'),\
		)\
	),\
	
	('ILGs', \
		(\
			('Epsilon Theta', 'Epsilon Theta'),('Fenway House', 'Fenway House'),('pika', 'pika'),('Student House', 'Student House'), ('Women\'s Independent Living Group (WILG)','Women\'s Independent Living Group (WILG)'),\
		)\
	),\
	('Fraternities', \
		(\
			('Alpha Delta Phi', 'Alpha Delta Phi'),('Alpha Epsilon Pi', 'Alpha Epsilon Pi'),('Alpha Phi Alpha', 'Alpha Phi Alpha'),('Alpha Tau Omega', 'Alpha Tau Omega'),('Beta Theta Pi', 'Beta Theta Pi'),('Chi Phi', 'Chi Phi'),('Delta Kappa Epsilon', 'Delta Kappa Epsilon'),('Delta Tau Delta', 'Delta Tau Delta'),('Delta Upsilon', 'Delta Upsilon'),('Kappa Alpha Psi', 'Kappa Alpha Psi'),('Kappa Sigma', 'Kappa Sigma'),('Lambda Chi Alpha', 'Lambda Chi Alpha'),('No. 6 Club', 'No. 6 Club'),('Nu Delta', 'Nu Delta'),('Phi Beta Epsilon', 'Phi Beta Epsilon'),('Phi Delta Theta', 'Phi Delta Theta'),('Phi Kappa Sigma', 'Phi Kappa Sigma'),('Phi Kappa Theta', 'Phi Kappa Theta'),('Phi Sigma Kappa', 'Phi Sigma Kappa'),('Pi Lambda Phi', 'Pi Lambda Phi'),('Sigma Chi', 'Sigma Chi'),('Sigma Nu', 'Sigma Nu'),('Sigma Phi Epsilon', 'Sigma Phi Epsilon'),('Tau Epsilon Phi', 'Tau Epsilon Phi'),('Theta Chi', 'Theta Chi'),('Theta Delta Chi', 'Theta Delta Chi'),('Theta Xi', 'Theta Xi'),('Zeta Beta Tau', 'Zeta Beta Tau'),('Zeta Psi', 'Zeta Psi'),\
		)\
	),\
	
	('Sororities',\
		(\
			('Alpha Chi Omega', 'Alpha Chi Omega'),('Alpha Epsilon Phi', 'Alpha Epsilon Phi'),('Alpha Kappa Alpha', 'Alpha Kappa Alpha'),('Alpha Phi Sorority', 'Alpha Phi Sorority'),('Kappa Alpha Theta', 'Kappa Alpha Theta'),('Sigma Kappa', 'Sigma Kappa')\
		)\
	),\

	('Other',        \
		(\
			('Other','Other'),\
		)\
	),\
)

yearNow = datetime.datetime.now().year
yearChoices = []
for year in range(1960, yearNow+5)+['Class Year']:
    yearChoices.append((str(year), str(year)))
yearChoices.reverse()
"""
majorChoices = [(), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
				('', ''), \
]
"""
majorChoices=range(1,25)
majorChoices.remove(13)
majorChoices.remove(19)
majorChoices.remove(23)
majorChoices.append('CMS')
majorChoices.append('CSB')
majorChoices.append('HST')
majorChoices.append('MAS')
majorChoices.append('STS')
majorChoices.append('Other')
majorChoices.insert(0,'Major')
majorChoices = [(str(year), str(year)) for year in majorChoices]
majorChoices.append(('Hello Textt','hello'))
