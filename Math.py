import math
def kalshiFee(contracts, price):
     return math.ceil(.07 * contracts * price * (1-price))

# kpy = Kalshi Price Yes, kpn = Kalshi Price No
# opy = other price yes, opn = other price no
def binaryArbitrage(kpy, kpn, opy, opn):
     if(kalshiFee(1, kpy) + opn <1) :
          return list(kpy, opn)
     if(kalshiFee(1, kpn) + opy < 1) :
          return (list(kpn, opy))
     return False




     
     
     
