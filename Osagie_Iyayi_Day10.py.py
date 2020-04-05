print('Ola!')
#Sieve of Eratosthenes
def sieve_of_eratos(limitingValue):
    '''
the function is created on the basis of finding the prime numbers less than the
limiting value
    '''

    for i in range(2, limitingValue+1):
        if i > 1:
            for t in range(2, i):
                if i % t !=0:
                    return i
                else:
                    break

print(sieve_of_eratos(200))
print('obrigado !')
                    
