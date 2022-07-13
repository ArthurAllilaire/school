

def freq_analysis(file_name):
    """
    File name: the name of the file that conatins the text to be tested
    """
    with open(file_name, 'r') as f:
        txt = f.read()

    result = {}

    for i in txt:
        if result.get(i):
            result[i] += 1
        else:
            result[i] = 1

    return result


print(freq_analysis('encrypted.txt'))
