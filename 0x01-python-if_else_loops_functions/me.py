def curr (a=None, b=None):
   if a is None:
    a = input('fro:') 
   if b is None:
    b= input("to:")
   amount = int(input('enter amount:'))
   exchanges_rate = {
    'USD' :1,
    'CAD' : 0.73751,
    'GDP':0.323,
    'JPY':135.719,
    'NGN':0.00216,
    'EUR':1.08484,
    'IQD':0.00076

  }
  
    
   rate = exchanges_rate[a]/exchanges_rate[b]
   result = amount*rate
   print(result)

curr()
