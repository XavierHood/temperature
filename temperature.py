def iscold(temp):

    if temp > 100:
        print('hot')
    elif temp < 75:
        print('cold')
    elif temp <= 100 and temp >= 75:
        print('warm')

#                              (femto)
# 1e-12                        (pico) []
# 1e-9 = .000 000 001          (nano)  [billionth]
# 1e-6 = .000 001              (micro) [millionth]
# 1e-3 = .001                  (milla) [thousandth]
# 0
# 1e3  = 1,000                 (killa)  [thousand]
# 1e6  = 1,000,000             (Mega)   [million]
# 1e9  = 1,000,000,000         (Giga)   [billion]
# 1e12 = 1,000,000,000,000     (Tera)   [Trillion]
# 1e15 = 1,000,000,000,000,000                  (Peta)   [Quadrillion]
# 10,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000.

temp = 1e12
iscold(temp)