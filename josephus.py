import matplotlib.pyplot as plt

def create_dudes(n):
    result_list = []
    for i in range(1, n+1):
        result_list.append(i)
    return result_list

def circle_of_dudes(a_list):
    original_number_of_dudes = len(a_list)
    while len(a_list) != 1:
        a_list.pop(1)
        a_list += [a_list.pop(0)]
    return original_number_of_dudes, a_list[0]

my_arg = int(input('graph up to how many dudes in the circle?: '))
feed_me_to_the_plot = []
for i in range(1, my_arg + 1):
    feed_me_to_the_plot.append(circle_of_dudes(create_dudes(i)))

plt.plot(feed_me_to_the_plot)

plt.show()
