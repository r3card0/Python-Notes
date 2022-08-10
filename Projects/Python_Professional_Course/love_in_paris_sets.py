#

alice = ['Ⅱ', 'Ⅳ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅱ']
bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']
alice_set = set(alice)
bob_set = set(bob)
silvester_set = set(silvester)

def love_meet(bob, alice):
    district_meet = {} 
    district_meet = set(district_meet)
    
    if alice_set & bob_set:
        district_meet.update(alice_set & bob_set)
    return district_meet

def affair_meet(bob, alice, silvester):
    alice_silvester_meet = {}
    alice_silvester_meet = set(alice_silvester_meet)
    alice_silvester_love = {}
    alice_silvester_love = set(alice_silvester_love)
    
    if alice_set & silvester_set: # and silvestre_set - bob_set:
        alice_silvester_meet.update(alice_set & silvester_set)
        if alice_silvester_meet - bob_set:
            alice_silvester_love.update(alice_silvester_meet - bob_set)
           
        return alice_silvester_love


print(love_meet(bob, alice),"-", affair_meet(bob, alice, silvester))

#affair_meet(bob, alice, silvester)