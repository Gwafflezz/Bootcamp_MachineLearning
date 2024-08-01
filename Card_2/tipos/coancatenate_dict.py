davi =  {
    "idade" : 24,
    "formado" : "nao"
}
rhayron = {
    "idade" : 26,
    "formado?" : "sim"
}
    
pedrola = {
    "idade" : 25,
    "formado?" : "nao"
}
 
residents = {
 "davi" : davi,
 "rhayron" : rhayron,
 "pedrola" : pedrola
 }

for x,y in residents.items():
	print(x,y)
    
print("\n")
    
tramontina = {
	"idade" : 25,
	"formado?" : "sim"

}

residents.update({"tramontina" : tramontina})

for x,y in residents.items():
	print(x,y)
    

print("\nidade de pedro: " + str( residents["pedrola"]["idade"]))