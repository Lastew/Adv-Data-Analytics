Employee = [
{'ID':'001', 'Name':'Mary', 'Pay_Rate':15.00,'Hours_Worked':40},
{'ID':'002', 'Name':'John', 'Pay_Rate':22.00,'Hours_Worked':25},
{'ID':'003', 'Name':'Bob', 'Pay_Rate':35.00,'Hours_Worked':4},
{'ID':'004', 'Name':'Mel', 'Pay_Rate':43.00,'Hours_Worked':62},
{'ID':'005', 'Name':'Jan', 'Pay_Rate':17.00,'Hours_Worked':33},
{'ID':'006', 'Name':'Sue', 'Pay_Rate':29.00,'Hours_Worked':45},
{'ID':'007', 'Name':'Ken', 'Pay_Rate':40.00,'Hours_Worked':36},
{'ID':'008', 'Name':'Dave', 'Pay_Rate':20.00,'Hours_Worked':17},
{'ID':'009', 'Name':'Beth', 'Pay_Rate':37.00,'Hours_Worked':37},
{'ID':'010', 'Name':'Ray', 'Pay_Rate':16.50,'Hours_Worked':80}
]

for emp in Employee:
	if int(emp['Hours_Worked']) > 40:
		pay = (40 + (int(emp['Hours_Worked']) - 40) * 1.5)) * int(emp['Pay_Rate'])
	else:
		pay = int(emp['Pay_Rate']) * int(emp['Hours_Worked'])
	
	print(emp['Name'], 'pay is:', pay)
