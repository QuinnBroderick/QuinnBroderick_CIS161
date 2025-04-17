
def wfq_queue(txt_file):
    premium = []
    standard = []
    economy  = []
    final_queue = []
    count = 0
    index = 0
    with open(txt_file, 'r') as file:
        for line in file:
            content = line.split()
            if content[0]== "P":
                premium.append(content[1])
            if content[0]== "S":
                standard.append(content[1])
            if content[0]== "E":
                economy.append(content[1])
            count+= 1
    while len(final_queue)<count:
        index = 0
        if len(premium)>=3:
            while index < 3:
                final_queue.append(premium[0])
                premium.pop(0)
                index += 1
        elif len(premium)>=2:
            while index < 2:
                final_queue.append(premium[0])
                premium.pop(0)
                index += 1
        elif len(premium)>=1:
            final_queue.append(premium[0])
            premium.pop(0)
            index += 1
        if len(standard)>=2:
            while index < 5:
                final_queue.append(standard[0])
                standard.pop(0)
                index += 1
        elif len(standard)>=1:
            while index < 5:
                final_queue.append(standard[0])
                standard.pop(0)
                index += 1
        if len(economy)>=1:
            final_queue.append(economy[0])
            economy.pop(0)
    return final_queue
print(wfq_queue("input_queue.txt"))
