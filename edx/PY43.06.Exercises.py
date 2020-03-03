#https://books.trinket.io/pfe/06-strings.html#exercises

str = 'X-DSPAM-Confidence:0.8475'

startPos = str.find(':')
strExtract = str[startPos+1:]
flExtract = float(strExtract)
print(flExtract)
type(flExtract)