def badge_maker(name):
    if (name == None or len(name) < 1): raise Exception("you must enter a valid name!");
    else: return f"Hello, my name is {name}.";

def batch_badge_creator(names):
    if (names == None): return None;
    elif (len(names) < 1): return [];
    else: return [badge_maker(name) for name in names];

def assign_rooms(names):
    if (names == None): return None;
    elif (len(names) < 1): return [];
    else:
        rmasmnts = ["" for i in range(len(names))];
        for i in range(len(names)):
            rmasmnts[i] = f"Hello, {names[i]}! You'll be assigned to room {(i + 1)}!";
        return rmasmnts;

def printer(names):
    mybadges = batch_badge_creator(names);
    for badge in mybadges:
        print(badge);
    rmnums = assign_rooms(names);
    for rmnum in rmnums:
        print(rmnum);
    return None;

printer(["Alan", "Tron", "Clu", "Kevin Flynn"]);
