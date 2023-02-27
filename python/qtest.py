def testfn(window, question, answers):
	print (window, question, answers)

var = ["&4", "Where do you want to go?", {"Home":1, "School":2, "Work":3}]
testfn(*var)