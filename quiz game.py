print("Welcome to my Quiz")

ans = input("Do you want to play this quiz: ")
print("-------------------------------------------------------------")

if ans == "Yes" or ans == "yes":
    print("Choose a topic: ")
    print("1. Games")
    print("2. Science")
    print("3. Sports")
    
    topic = int(input("Which one do you choose from above(1, 2 or 3): "))
    print("-------------------------------------------------------------")

    if topic == 1:
    
        score = 0
        for i in range(1, 6):
            if i == 1:
                print("Q1. In what year was the first video game invented?")
                print("1. 1958")
                print("2. 1969")
                print("3. 1943")
                print("4. 1962")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 1:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10

            elif i == 2:
                print("Q2. Which gaming console has the record for most units sold?")
                print("1. Nintendo Gamecube")
                print("2. PS2")
                print("3. XBox 360")
                print("4. Wii")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 2:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10
                
            elif i == 3:
                print("Q3. What is the strongest block you can find in Minecraft?")
                print("1. Obsidian")
                print("2. Diamond")
                print("3. Ender Chest")
                print("4. Ancient Debris")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 1:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10
                
            elif i == 4:
                print("Q4. What year was the first Super Smash Bros. released?")
                print("1. 1998")
                print("2. 1997")
                print("3. 1999")
                print("4. 1993")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 3:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10

            elif i == 5:
                print("Q5. Which of these Pokemon is the first Generation starter Pokemon?")
                print("1. Snivy")
                print("2. Litten")
                print("3. Torchic")
                print("4. Bulbasaur")
    
                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 4:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10

        if score >=10:
            print("Total score = ", score)
            print("You Won")
        else:
            print("Total score = ", score)
            print("You lose")

    elif topic == 2:
    
        score = 0
        for i in range(1, 6):
            if i == 1:
                print("Q1. NASA stands for the National _____________ and Space Administration.")
                print("1. Astronomy")
                print("2. Aeronautics")
                print("3. Acrobatics")
                print("4. Airplane")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 2:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10

            elif i == 2:
                print("Q2. You can't live without water. What is its chemical Formula?")
                print("1. H2")
                print("2. O2")
                print("3. H2O")
                print("4. H2O2")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 3:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10
                
            elif i == 3:
                print("Q3. Which of these elements is a nonmetal?")
                print("1. Silicon")
                print("2. Aluminium")
                print("3. Manganese")
                print("4. Iron")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 1:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10
                
            elif i == 4:
                print("Q4. Which of the following travels at the fastest speed possible?")
                print("1. Asteroids")
                print("2. Space Ships")
                print("3. Light")
                print("4. Sound")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 3:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10

            elif i == 5:
                print("Q5. Which of the following materials will be attracted to a magnet?")
                print("1. Diamond")
                print("2. Iron")
                print("3. Plastics")
                print("4. Cotton")
    
                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 2:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10

        if score >=10:
            print("Total score = ", score)
            print("You Won")
        else:
            print("Total score = ", score)
            print("You lose")

    elif topic == 3:
    
        score = 0
        for i in range(1, 6):
            if i == 1:
                print("Q1. After how many years FIFA World Cup held?")
                print("1. 2 Years")
                print("2. 3 Years")
                print("3. 4 Years")
                print("4. Every Year")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 3:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10

            elif i == 2:
                print("Q2. Which sport is performed by the Legend Muhammad Ali?")
                print("1. Weight Lifting")
                print("2. Swimming")
                print("3. Boxing")
                print("4. Shooting")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 3:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10
                
            elif i == 3:
                print("Q3. What is the National Game of the USA?")
                print("1. Tennis")
                print("2. Baseball")
                print("3. Soccer")
                print("4. Basketball")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 2:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10
                
            elif i == 4:
                print("Q4. What is the National Game of India?")
                print("1. Hockey")
                print("2. Kabaddi")
                print("3. Cricket")
                print("4. Football")

                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 2:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10

            elif i == 5:
                print("Q5. When did India win its first Olympic Gold Medal?")
                print("1. 1948")
                print("2. 1952")
                print("3. 1928")
                print("4. 1964")
    
                option = int(input("Enter your option(1, 2, 3 or 4): "))
                print("-------------------------------------------------------------")
                if option == 3:
                    print("Right answer.")
                    print("Your score = +10")
                    print("-------------------------------------------------------------")
                    score = score + 10
                else:
                    print("Wrong answer.")
                    print("Penalty = -10")
                    print("-------------------------------------------------------------")
                    score = score - 10

        if score >=10:
            print("Total score = ", score)
            print("You Won")
        else:
            print("Total score = ", score)
            print("You lose")
            
    else:
        print("Please choose fom the given topics.")


else:
    print("Bye bye")
