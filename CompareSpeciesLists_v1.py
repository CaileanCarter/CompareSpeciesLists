
File1 = open(input("File path of first list in text file:"), "rt")
File2 = open(input("File path of second list in text file:"), "rt")

file = open("Compared_List.txt", "a+")

suffix_sp = [] #a list of genuses with "sp." suffix to denote the entire genus
species = [] #list of species from File1

if __name__ == "__main__":
    
    for line in File1:
        if line[-4:-1] == "sp.":
            suffix_sp.append(line[:-5]) #extracts the genus identifiers from the list seperates it into the suffix_sp list
            
        else:
            species.append(line.strip())
    File1.close()

    for line in File2:
        if line[-4:-1] == "sp.":
            #if theres a genus identifier in the file, this block will find the species in the other list under this genus.
            for spec in species:
                if line[:-5] == spec[:len(line[:-5])]:
                    file.write(spec.replace("_", " ")+"\n")
                    species.remove(spec)
            #checks whether the genus identifier is in the other list and adds to the final text file
            if line[:-5] in suffix_sp:
                file.write(line.replace("_", " "))
        #finds whether there's a species of same name in other list
        elif line[:-1] in species:
            file.write(line.replace("_", " "))
            species.remove(line[:-1])              
        
        else: #this checks whether a species is in a genus from the list of genuses.
            for suf_spec in suffix_sp:
                if suf_spec == line[:len(suf_spec)+1]:
                    file.write(line.replace("_", " "))
    File2.close()  
    file.close() #Fin. 