
'''
my reference websites are
- https://www.autoexpress.co.uk/car-news/96570/10-most-common-car-
problems-and-the-cars-most-likely-to-have-them
- https://carbrain.com/Blog/20-most-common-car-complaints

common issues my system will diagnose will be : worn brakes, excessive oil,
emission leaks, radiator leak, uneven tire wear, transmission issues,
transmission fluid leaks, water damage, dead battery, and alternator.

symptoms will be contained in the symptoms list, issues will sometimes
share common symptoms, but the system is smart enough to differentiate
and diagnose the appropriate problem.

the system will ask you yes or no questions, and will diagnose based on
the user responses.

the problem class will contain issues found in a given problem. if all of
the issues are set to true, the problem will be diagnosed and the system
will display the issue.


'''

class problem:
    def __init__(self, signs, name):
        self.signs = signs
        self.name = name
        self.issues = {}
        self.found = {}
        keys = signs
        for i in range(len(keys)):  #set flags for issues to false initially
            self.issues[keys[i]] = False
            self.found[keys[i]] = True
            
        self.diagnosed = False      # once diagnosed is set to true, issue found
        

class hypothesis:
    def __init__(self, problems_list, symptoms):
        self.problems_list = problems_list
        print("Does your car have the following issues? y for 'yes' ")
        for i in range(len(symptoms)):  # itterate through symptoms
            print(symptoms[i] + ": ")
            flag = input();
            for x in range(len(problems_list)): # check to find issue
                if(flag == 'y'):
                    if( symptoms[i] in problems_list[x].issues):    #set flags
                        problems_list[x].issues[symptoms[i]] = True
                if(problems_list[x].issues == problems_list[x].found):
                    print("issue is " + problems_list[x].name)
                    problems_list[x].diagnosed = True
                    break   # issue diagnosed, exit loop
            if (problems_list[x].diagnosed == True):
                break
                
        if(problems_list[x].diagnosed == False):    #default case 
            print("malfunctioning check engine light, no errors found")

def main():
    print("-------check engine light diagnosing system-------")

    #full list of symptoms
    symptoms = ["squeeky brakes","unresponvive brakes", "leaks","sways to side","bad traction",
                "smells like smog", "engine failure", "leaks coolant","leaks transmission fluid",
                "wet transmission", "shakey transmission","grinding gears", "crank but won't start",
                "whinning sound", "growling sound"]

    #list of possible issues
    problem1 = ["squeeky brakes", "unresponvive brakes"]
    worn_brakes = problem(problem1, "worn breaks")

    problem2 = ["leaks","engine failure"]
    excessive_oil = problem(problem2, "excessive oil")

    problem3 = ["smells like smog","engine failure"]
    emission_leak = problem(problem3, "an emission leak")

    problem4 = ["leaks", "leaks coolant"]
    radiator_leak = problem(problem4, "a radiator leak")

    problem5 = ["sways to side", "bad traction"]
    uneven_wear = problem(problem5, "uneven tire wear")

    problem6 = ["shakey transmission", "grinding gears"]
    transmission = problem(problem6, "a bad transmission")

    problem7 = ["leaks", "leaks transmission fluid"]
    transmission_fluid_leak = problem(problem7, "a transmission fluid leak")

    problem8 = ["leaks", "wet transmission"]
    water_damage = problem(problem8, "water damage")

    problem9 = ["crank but won't start","whinning sound"]
    dead_battery = problem(problem9, "a dead battery")

    problem10 =["crank but won't start","growling sound"]
    bad_alternator = problem(problem10, "a bad alternator")

    problems = [worn_brakes, excessive_oil,emission_leak, radiator_leak, uneven_wear,
                transmission, transmission_fluid_leak, water_damage, dead_battery,
                bad_alternator]

    #initializing toubleshooting system 
    diagnoser = hypothesis(problems, symptoms)
       

main()


