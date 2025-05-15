is_pythonProgrammer = True
is_expert = True



#check if pythonProgrammer and expert:  then print "you are a master trainer"...
if is_pythonProgrammer and is_expert:             # is_pythonProgrammer = True
    print("you are a master trainer")             # is_expert = True





#check if pythonProgrammer but not expert:  then print "at least you're getting there"...
elif is_pythonProgrammer and not is_expert:       # is_pythonProgrammer = True
    print("at least you're getting there")        # is_expert = False





#check if you are not a pythonProgrammer: then print "you need to learn python"...
elif not is_pythonProgrammer:                     # is_pythonProgrammer = False
    print("you need to learn python")             # is_expert = True



