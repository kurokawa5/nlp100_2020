# Implement a function that receives arguments, x, y, and z and returns a string
#  “{y} is {z} at {x}”, where “{x}”, “{y}”, and “{z}” denote the values of x, y, and z,
# respectively. In addition, confirm the return string by giving the arguments x=12, y="temperature",
# and z=22.4.

def template_based_sentence_generation(x, y, z):
    return f'{x}時の{y}は{z}'
    #return '{}時の{}は{}'.format(x, y, z)

x = 12
y = "気温"
z = 22.4

print(template_based_sentence_generation(x, y, z))
