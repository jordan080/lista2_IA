def findDecision(obj): #obj[0]: Exemplo, obj[1]: História de Credito, obj[2]: Dívida, obj[3]: Garantia, obj[4]: Renda
	# {"feature": "Exemplo", "instances": 20, "metric_value": 1.7884, "depth": 1}
	if obj[0] == 'E1':
		return 'Alto'
	elif obj[0] == 'E2':
		return 'Alto'
	elif obj[0] == 'E19':
		return 'Moderado'
	elif obj[0] == 'E18':
		return 'Baixo'
	elif obj[0] == 'E17':
		return 'Baixo'
	elif obj[0] == 'E16':
		return 'Alta'
	elif obj[0] == 'E15':
		return 'Moderado'
	elif obj[0] == 'E14':
		return 'Alto'
	elif obj[0] == 'E13':
		return 'Baixo'
	elif obj[0] == 'E12':
		return 'Moderado'
	elif obj[0] == 'E11':
		return 'Alto'
	elif obj[0] == 'E10':
		return 'Baixo'
	elif obj[0] == 'E9':
		return 'Baixo'
	elif obj[0] == 'E8':
		return 'Moderado'
	elif obj[0] == 'E7':
		return 'Alto'
	elif obj[0] == 'E6':
		return 'Baixo'
	elif obj[0] == 'E5':
		return 'Baixo'
	elif obj[0] == 'E4':
		return 'Alto'
	elif obj[0] == 'E3':
		return 'Moderado'
	elif obj[0] == 'E20':
		return 'Moderado'
	else: return 'Moderado'
