def findDecision(obj): #obj[0]: História de Credito, obj[1]: Dívida, obj[2]: Garantia, obj[3]: Renda
	# {"feature": "Renda", "instances": 20, "metric_value": 1.7884, "depth": 1}
	if obj[3] == 'Acima_de_$35k':
		# {"feature": "Hist\u00f3ria de Credito", "instances": 9, "metric_value": 1.2244, "depth": 2}
		if obj[0] == 'Boa':
			return 'Baixo'
		elif obj[0] == 'Desconhecido':
			# {"feature": "D\u00edvida", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1] == 'Baixa':
				return 'Baixo'
			elif obj[1] == 'Alta':
				return 'Alta'
			else: return 'Alta'
		elif obj[0] == 'Ruim':
			return 'Moderado'
		else: return 'Moderado'
	elif obj[3] == '$0_a_$15k':
		# {"feature": "Garantia", "instances": 6, "metric_value": 1.2516, "depth": 2}
		if obj[2] == 'Nenhuma':
			return 'Alto'
		elif obj[2] == 'Adequada':
			# {"feature": "Hist\u00f3ria de Credito", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Boa':
				return 'Baixo'
			elif obj[0] == 'Ruim':
				return 'Moderado'
			else: return 'Moderado'
		else: return 'Baixo'
	elif obj[3] == '$15_a_$35k':
		# {"feature": "Hist\u00f3ria de Credito", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[0] == 'Desconhecido':
			# {"feature": "D\u00edvida", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1] == 'Alta':
				# {"feature": "Garantia", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2] == 'Nenhuma':
					return 'Alto'
				elif obj[2] == 'Adequada':
					return 'Moderado'
				else: return 'Moderado'
			elif obj[1] == 'Baixa':
				return 'Moderado'
			else: return 'Moderado'
		elif obj[0] == 'Boa':
			return 'Moderado'
		elif obj[0] == 'Ruim':
			return 'Alto'
		else: return 'Alto'
	else: return 'Moderado'
