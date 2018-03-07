def reverse(numero):
    maxdiv = len(str(numero))-1;
    if(maxdiv<=0):
        return str(numero);
    final="1";
    for i in range(maxdiv):
        final+="0";
    maxdiv = int(final);
    maxwd = int(numero)/maxdiv;
    maxld = int(numero)//maxdiv;
    dec = str(round((maxwd-maxld)*int(final)));
    return str(reverse(dec)+""+str(maxld));

numero = input("What's your number? ")
print ("original:  "+numero);
print ("invertido: " + reverse(numero));
input()
