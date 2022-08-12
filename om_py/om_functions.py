

def om_scale(list, minout, maxout, minin=0, maxin=0):
    "return a list of samples between min and max"
    if minin == 0 and maxin == 0:
        minin = min(list)
        maxin = max(list)
    new_scale = []
    for i in list:
        new_scale.append(minout + (((i - minin) * (maxout - minout)) / (maxin - minin )))
    return new_scale