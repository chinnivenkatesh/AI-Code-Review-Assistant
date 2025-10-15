# A function to process data
def process(data):
    x = []
    for i in data:
        if i > 10:
            x.append(i * 2)
    return x