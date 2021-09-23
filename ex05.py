sc= input('Enter score between 0 and 1:')
try:
    score= float(sc)
except:
    print('Error')
    quit()
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')
else:
    print('Error')
    quit()
