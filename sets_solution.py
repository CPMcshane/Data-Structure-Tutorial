"""
Sets example problem solution.
"""
pantry = ["ceral box", "soup can", "bread", "vegtable can", "chips", "dounuts", "fruit can", "ceral box", "soup can", "oatmeal",
"oatmeal", "chips", "fruit can", "chips", "dounuts", "ceral box", "vegtable can", "sugar", "flour", "dounuts", "fruit can",
"honey", "peanut butter", "vegtable can", "chips"]

def find_foods():
    print(len(set(pantry)))

find_foods()