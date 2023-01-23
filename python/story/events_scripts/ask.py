def ask(window, question, *answers):
	if len(answers) == 0:
		window.add_text(question.join("<r>"))
	else:
		window.add_text(question.join("<r>"))
		i = 0
		for answer in answers:
			q_str = f"{i+1}: {answer}"
			window.add_text(q_str)
			i += 1
	
	return window.getReturnValue()