import jdatetime

test = str(jdatetime.datetime.now())
date = test.split()

print("Emroz :", date[0])
print("Saat :", date[1][:5])
