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

def order_update(update):
    # Create a map of current indices of each page for easy access
    page_indices = {page: i for i, page in enumerate(update)}

    # Initialize a flag to indicate if any changes were made
    changed = True
    
    while changed:
        changed = False  # Reset the change flag
        # Go through each rule and enforce the ordering
        for x, y in rules:
            if x in page_indices and y in page_indices:
                # If x comes after y, we need to swap
                if page_indices[x] > page_indices[y]:
                    # Swap x and y in the update list
                    update[page_indices[x]], update[page_indices[y]] = update[page_indices[y]], update[page_indices[x]]
                    # Update the indices in the map
                    page_indices[x], page_indices[y] = page_indices[y], page_indices[x]
                    changed = True  # Mark that a change has been made
                    break  # Restart checking from the top after a change

    return update

sum_valid = 0 
sum_corrected = 0 

for update in updates:
    update = list(map(int,update.split(',')))

    if(is_valid(update)):
        sum_valid += update[len(update)//2]
    else:
        corrected_update = order_update(update)
        sum_corrected += corrected_update[len(corrected_update)//2]

print(sum_valid)
print(sum_corrected)
