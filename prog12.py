# FLAMES Game in python
# FLAMES stands for Friends, Lovers, Affection, Marriage, Enemy, Siblings. This is not accurate at all, it's just a fun game
# Steps to play : 
# 1. Take 2 names
# 2. Remove common characters with their respective common occurences
# 3. Get the count of characters that are left
# 4. Take FLAMES letters as ['F','L','A','M','E','S']
# 5. Start removing letters using count we got
# 6. The letter which lasts the process, is the result

# Note : This is just for fun, please don't take this seriously

def remove_char_match(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            # if common character is found, remove that character, and return lsit of concatenated list with True flag
            if(l1[i] == l2[j]):
                c = l1[i]
                # remove characters from both lists
                l1.remove(c)
                l2.remove(c)
                # concatenation of 2 list elements with *, * just acts as border mark here
                l3 = l1 + ["*"] + l2
                return [l3, True]
    # if no common characters is found, then return concatenated list with False flag
    l3 = l1 + ["*"] + l2
    return [l3, False]
# taking player's mame
p1 = input("player 1 name : ")
# converting into lowecase, so we face no issues
p1 = p1.lower()
# removing any spaces and replacing it woth empty string, so that there's no space in between
p1.replace(" ","")
# converting all letters/characters in the form of list
p1_list = list(p1)
p2 = input("player 2 name : ")
p2 = p2.lower()
p2.replace(" ","")
p2_list = list(p2)

# taking flag as True initially
proceed = True

# keep calling the function until a common character is found, or keep looping until the proceed flag is True
while proceed:
    # function calling and storing return values 
    ret_lst = remove_char_match(p1_list, p2_list)

    # take out concatenated list from return list
    con_lst = ret_lst[0]

    # take out flag value from return list
    proceed = ret_lst[1]

    star_index = con_lst.index("*")

    # all characters before * store in p1_list 
    p1_list = con_lst[: star_index]

    # all characters after * store in p2_list
    p2_list = con_lst[star_index+1 :]

count = len(p1_list) + len(p2_list)

result = ["Friends", "Lovers", "Affection", "Marriage", "Enemy", "Siblings"]

# keep looping until only one item is remaining in the list
while(len(result)>1):
    # store that index value, from where we have to perform slicing
    split_index = (count%len(result)-1)
    
    # this step is done for performing anti-clock wise circular counting
    if(split_index>=0):
        right = result[split_index+1:]
        left = result[:split_index]

        result = right+left

    else:
        result = result[:len(result)-1]
print("relationship status : ",result[0])