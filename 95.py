entry = input("Type something : ")
output = f"""
<h1> Welcome To Home Page </h1>
<p>{entry}</p>
"""
# print(output)
open("home.html", "w").write(output)
print("Done")
