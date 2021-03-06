#import requirements
import json

#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	#load users data into json
	data = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	#get intention name
	intention = intents["intent"]["intentName"]


	#extract the number the user intended
	try:
		number = intents["slots"][0]["value"]["value"]
		number = int(number)
	except Exception as e:
		print(e)
		# return false, so the server can try to use fallback skills to generate an answer
		return False

	#if the intention is to count up, count to the number the user wants to count to
	if(intention == "countto"):
		answer = ""
		for x in range(number):
			answer += str(x+1) + "\n"

		#disable translator
		return(answer),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png","answer",False

	#intention is not to count up, so count down
	else:
		answer = ""
		for x in range(number):
			answer += str(number - (x+1)) + "\n"

		# disable translator
		return(answer),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png","answer",False

	#at least one return (no in, if or try) statement has to be not indented
	#this statement is not executed. Necessary for python interpreter tho.
	return False
