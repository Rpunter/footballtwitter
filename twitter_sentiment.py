import sentiment_classfier as s

## File directory
nw_dir = 'C:/Users/kavisid/Documents/Northwestern MSPA/Predict 452/Twitter extract/'

def on_data(self, data):
		pullData = open(nw_dir+"bulls_20150529.csv","r").read()
                lines = pullData.split('\n')
		sentiment_value, confidence = s.sentiment(lines)
		print(lines, sentiment_value, confidence)

		if confidence*100 >= 80:
			output = open("twitter-out.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

def on_error(self, status):
    print(status)
