with open('inputs/day05.txt', 'r') as f:
    lines = f.read()

sections = (lines.split('\n\n'))
rules_section,updates = sections[0].strip().split('\n'), sections[1].strip().split('\n')


rule_tree= {}
rules = []
for rule in rules_section:
    k,v = map(int,rule.split('|'))
    rules.append((k,v))
    if k not in rule_tree:
        rule_tree[k] = []
    rule_tree[k].append(v)
    if v not in rule_tree:
        rule_tree[v] = []

def is_valid(update):
    page_indices = {page : i for i,page in enumerate(update)}
    for x, y in rules:
        if x in page_indices and y in page_indices and page_indices[x] > page_indices[y]:
            return False
    return True

# Check if an update is valid using the rule_tree
# def is_valid(update):
#     page_indices = {page: i for i, page in enumerate(update)}
#     for page, followers in rule_tree.items():
#         if page in page_indices:  # Check only if the page is in the current update
#             for follower in followers:
#                 if follower in page_indices and page_indices[page] > page_indices[follower]:
#                     return False  # Invalid order found
#     return True

total = 0 

for update in updates:
    update = list(map(int,update.split(',')))
    
    if(is_valid(update)):
        total += update[len(update)//2]


print(total)
    



