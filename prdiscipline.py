disciplina1 = {"Disciplina":"Limba Romana", "Note": [7,8,7,7], "Teza": 8}
disciplina2 = {"Disciplina":"Matematica", "Note": [7,8,7,10], "Teza": 10}
disciplina3 = {"Disciplina":"Informatica", "Note": [7,9,10,8], "Teza": 8}
medialanote1 = sum(disciplina1["Note"]) / len(disciplina1["Note"])
mediapentruan1 = (medialanote1 + int(disciplina1["Teza"])) / 2
print("La Limba romana, media anuala este de: ", mediapentruan1)
medialanote2 = sum(disciplina2["Note"]) / len(disciplina2["Note"])
mediapentruan2 = (medialanote2 + int(disciplina2["Teza"])) / 2
print("La Matematica, media anuala este de: ", mediapentruan2)
medialanote3 = sum(disciplina3["Note"]) / len(disciplina3["Note"])
mediapentruan3 = (medialanote3 + int(disciplina3["Teza"])) / 2
print("La Limba romana, media anuala este de: ", mediapentruan3)
mediatotala = (mediapentruan1 + mediapentruan2 + mediapentruan3) / 3
print("Media anuala este:", mediatotala)
if mediatotala >= 9 and int(disciplina1["Teza"]) >= 9 and int(disciplina2["Teza"]) >= 9 and int(disciplina3["Teza"]) >= 9:
    print("Elevul este eminent.")
if mediatotala >= 8 and int(disciplina1["Teza"]) >= 8 and int(disciplina2["Teza"]) >= 8 and int(disciplina3["Teza"]) >= 8:
    print("Elevul este proeminent.") 
if mediatotala < 5 and int(disciplina1["Teza"]) < 5 and int(disciplina2["Teza"]) < 5 and int(disciplina3["Teza"]) < 5:
    print("Elevul este repetent.")



