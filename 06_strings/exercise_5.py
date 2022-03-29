#Use find and string slicing to extract the portion of the string after the colon character 
#and then use the float function to convert the extracted string into a floating point number.


line = 'X-DSPAM-Confidence: 0.8475 '

line_without_spaces = line.replace(" ","")

start_number = line_without_spaces.find(':')

host = line_without_spaces[start_number+1:-1]
host = float(host)
print(host)

