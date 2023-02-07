def ask(window, question, *answers):
	if len(answers) == 0:
		window.add_text(question + '<r>')
	else:
		window.add_text(question)
		i = 0
		for answer in answers:
			q_str = f"{i+1}: {answer}"
			
			if answer == answers[-1]:
				window.add_text(q_str + '<r>')
			else:
				window.add_text(q_str)
			i += 1

	rval = window.get_return_value()
	if type(rval) == str:
		window.add_text(rval)
	elif type(rval) == list:
		for line in rval:
			window.add_text(line)
	#window.format_render()
	return rval