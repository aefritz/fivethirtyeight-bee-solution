x = .99
z = .01
a = 1
accum = 0
accum_prev = 0
error = 100
def roundsurvival_prob(y):
    return float(pow(x,y)*(1-pow((x-1*z),y))*(1-pow((x-2*z),y))*(1-pow((x-3*z),y))*(1-pow((x-4*z),y))*(1-pow((x-5*z),y))*(1-pow((x-6*z),y))*(1-pow((x-7*z),y))*(1-pow((x-8*z),y))*(1-pow((x-9*z),y)))
while error > .0001:
    accum_prev = accum;
    accum += roundsurvival_prob(a)
    error = float(100 - float(100 * accum_prev / accum))
    print("Iteration: " + str(a) + ", value: " + str(accum))
    a += 1
