#--coding:utf-8--
ip = raw_input('Digite um endereço  IP: ')
#print 'O endereço ' + ip + ' é válido'
print 'O endereço %s é válido' %ip
#Abaixo agora com a quantidade de caracteres como inteiro
print 'O endereço %s tem o tamanho de %d caracteres' %(ip,len(ip))
#Abaixo agora com a quantidade de caracteres sendo sgtring
print 'O endereço %s tem o tamanho de %s caracteres' %(ip,str(len(ip)))
#Imprimindo na tela numero quebrado(float)
print 'Número quebrado %f' %1.23456789
#Imprimindo na tela o numero quebrado com dois digitos apenas
print 'Número quebrado reduzido %.2f' %1.23456789
