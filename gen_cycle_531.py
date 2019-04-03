'''
Note: This tool won't solve my problem. My best bet is to make a JS page on my github pages that I can use to calculate my weights for the day. Go back and work on the website, do it in react, etc...
:D


So we want to generate a full cycle of big but boring
'''


maxes = {"Bench":245, "Press":165, "Squat":385, "Deadlift":450}

tm_percent = .8

# Generate Training Maxes

lifts = ["Bench","Press","Squat","Deadlift"]

tm = {}


for i in range(len(lifts)):
    tm[lifts[i]] = maxes[lifts[i]] * tm_percent

cycle_matrix = [[.7,.8,.9],[.65,.75,.85],[.75,.85,.95]]



full_cycle = ""

start = "Warm-Up/Mobility"
throws = "Jumps/Throws 10 Total"
five_three_one = []
bbb = ""
start_space = "      "
space = "                    "

# Do week one
top = "{}Monday (Shoulders/Biceps){}Tuesday (Legs/Abs){}Thursday (Chest/Triceps){}  Friday (Back)\n".format(start_space,space,space,space,space)
full_cycle += top
top = " {}   {}      {}{}      {}{}{}    {}\n".format(start_space,start,space,start,space,start,space,start)
full_cycle += top
top = "{}  {}{}{} {}{}{}{}\n".format(start_space,throws,space,throws,space,throws,space,throws)
full_cycle += top

'''
Put in a day where all of the numbers are done automatically
'''


# This gets me the numbers for the first week of a cycle
nums = []
for j in range(3):
    for i in range(4):
        val = tm[lifts[i]]*cycle_matrix[0][j]
        nums.append(int(val))

# print(nums)

top = "     {}     {}x5  {}                 {}x5 {}             {}x5           {}     {}x5\n".format(start_space,nums[0],space,nums[1],space,nums[2],space,nums[3])
full_cycle += top

top = "     {}     {}x5  {}                {}x5 {}             {}x5           {}     {}x5\n".format(start_space,nums[4],space,nums[5],space,nums[6],space,nums[7])
full_cycle += top



print(full_cycle)
