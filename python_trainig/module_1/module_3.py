try:
    import json

    with open('D:\\cctech\\python-training\\test.json', 'r') as file:
        json_data = json.load(file)

    # input_list = json_data['lists']
    input_list = json_data['list']
    # from math import sqrts
    from math import sqrt
    i = 0
    sqrt_list = []
    while i in range(len(input_list)):
        sqrt_list.append(sqrt(input_list[i]))
        i+= 1

    json_data['sqrt_list'] = sqrt_list

    json = json.dumps(json_data)

    with open('D:\\cctech\\python-training\\test.json', 'w') as file:
        file.write(json)

except ModuleNotFoundError as e:
    print('Module Not found')
    print(e)
except FileNotFoundError as e:
    print('File does not exists')
except KeyError as e:
    print('Key does not exist in json data')
except ImportError as e:
    print('imported function does not exist in maths module')
except IndexError as e:
    print('list out of range')
except NameError as e:
    print('variable not defined')
except Exception as e:
    print(e)