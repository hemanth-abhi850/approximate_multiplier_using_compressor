## this code converts decimal number to eight bit binary number
def Decimal2binary(pxl):

    """ Input : Decimal Value ; Output : Ternary string """

    """if pxl > 242:
        pxl = 242"""

    tern = np.zeros(8, dtype="int")
    value = [2**(7 - i) for i in range(8)]

    for i in range(8):

        if pxl >= value[i]:
            tern[i] = pxl // value[i]
            pxl = pxl % value[i]

    tern = tern.astype("str")
    tern = "".join(tern)

    return tern

## this code converts binary number into decimal number

def decimal(n):

  k = list(n)
  sum = 0
  k.reverse()
  for i in range(len(k)):
      sum = sum + (int(k[i])* (2**i))

  return sum
