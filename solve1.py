def solve(x,y,z):
    hasil = (x + y * z)/(x * y);
    return (hasil**z)

jawaban = solve(4,3,2);
print(jawaban);

# Cara lain

import math
def solve(x,y,z):
    hasil = (x + y * z)/(x * y);
    print (math.pow(hasil, z));
    return 'stop'

jawaban = solve(4,3,2);
print(jawaban);