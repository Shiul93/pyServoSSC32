


def mappossition(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;


def move(grados, tiempo, servo, ser):
    gradstr = str(mappossition(grados, 0, 180, 600, 2500))
    retstr = '#' + str(servo) + 'P'
    retstr += gradstr
    retstr += 'T'
    retstr += str(int(tiempo * 1000))
    retstr += '\r\n'
    print(retstr)
    ser.write(retstr)


def center(servo, ser):
    move(90, 0.1, servo, ser)