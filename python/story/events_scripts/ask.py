def ask(window, question, answers = {}):
	if len(answers) == 0:
		window.add_text(question + '<r>')
	else:
		window.add_text(question)
		i = 0
		answers_list = list(answers.keys())
		for answer in answers_list:
			q_str = f"{answer}"
			
			if answer == answers_list[-1]:
				window.add_text(q_str + '<r>')
			else:
				window.add_text(q_str)
			i += 1

	windowVal = window.get_return_value()

	if len(answers) == 0:
		return windowVal

	rval = ''
	for answer, value in answers.items():
		if windowVal.casefold().strip() == answer.casefold().strip():
			rval = value

	try:
		rval = int(rval)
	except:
		rval = ask(window, question + ' Wrong input, please try again.', answers)

	rvalues = list(answers.values())
	if rval == '':
		rval = rvalues[int(windowVal) - 1]
	
	return rval