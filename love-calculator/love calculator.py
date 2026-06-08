
def love_calculator(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second = l + o + v + e 
    cap_name1 = name1.title()
    cap_name2 = name2.title()

    love_meter = int(str(first) + str(second))
    if love_meter > 50:
        print(f"The love between you, {cap_name1} and your partner, {cap_name2} is {love_meter}%. ")
    else: 
        print(f"Sorry.  The love between you, {cap_name1} and your partner, {cap_name2} is only {love_meter}%. ")

        
love_calculator("kim kadashian", "kanye west")
                


