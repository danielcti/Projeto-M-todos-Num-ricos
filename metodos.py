from sympy import *
import matplotlib.pyplot as plt

#variaveis globais
y, t = symbols('y t')
# vy = []
# vx = []
F = []
text_file = open("output.txt", "w") # arquivo que vou guardar as respostas
v_Aux = []
def f_calcula(f,yn,tn): #calcula o valor da funcao dada com os parametros tn e yn
	f = f.subs('t',tn)
	f = f.subs('y',yn)
	return f

def euler(f,t,y,h,n):
	tn = t # o primeiro valor para o tn sera o t0
	yn = y # o primeiro valor para o yn sera o y0

	text_file.write("Metodo de Euler\n")
	text_file.write("y(%.5f) = %.8f\n" % (float(tn), float(yn)))
	text_file.write("h = %.5f\n" % (float(h)))
	text_file.write("0 %.5f\n" % (float(yn)))

	for x in range(1,n+1):
		yn = yn + h*f_calcula(f,yn,tn) # formula tradicional do metodo de euler
		tn = tn + h # incrementa o tn para a proxima iteracao
		text_file.write("%d %.8f\n" % (int(x), float(yn)))
	text_file.write("\n")
	return

def euler_inverso(f,t,y,h,n):
	tn = t # o primeiro valor para o tn sera o t0
	yn = y # o primeiro valor para o yn sera o y0

	text_file.write("Metodo de Euler Inverso\n")
	text_file.write("y(%.5f) = %.8f\n" % (float(tn), float(yn)))
	text_file.write("h = %.5f\n" % (float(h)))
	text_file.write("0 %.5f\n" % (float(yn)))

	for x in range(1,n+1):
		k = yn + h*f_calcula(f,yn,tn)

		yn = yn + h*f_calcula(f, k, tn+h) # formula tradicional do metodo de euler
		tn = tn + h # incrementa o tn para a proxima iteracao
		text_file.write("%d %.8f\n" % (int(x), float(yn)))
	text_file.write("\n")
	return

def euler_aprimorado(f,t,y,h,n):
	tn = t # o primeiro valor para o tn sera o t0
	yn = y # o primeiro valor para o yn sera o y0

	text_file.write("Metodo de Euler Aprimorado\n")
	text_file.write("y(%.5f) = %.8f\n" % (float(tn), float(yn)))
	text_file.write("h = %.5f\n" % (float(h)))
	text_file.write("0 %.5f\n" % (float(yn)))

	for x in range(1,n+1):
		k = yn + h*f_calcula(f,yn,tn)
		yn = yn + h/2*(f_calcula(f, yn, tn)+f_calcula(f, k, tn+h)) # formula tradicional do metodo de euler
		tn = tn + h # incrementa o tn para a proxima iteracao
		text_file.write("%d %.8f\n" % (int(x), float(yn)))
	text_file.write("\n")
	return

def runge_kutta(f,t,y,h,n):
	tn = t # o primeiro valor para o tn sera o t0
	yn = y # o primeiro valor para o yn sera o y0

	text_file.write("Metodo de Runge-Kutta\n")
	text_file.write("y(%.5f) = %.8f\n" % (float(tn), float(yn)))
	text_file.write("h = %.5f\n" % (float(h)))
	text_file.write("0 %.5f\n" % (float(yn)))

	for x in range(1,n+1):
		k1 = f_calcula(f, yn, tn)
		k2 = f_calcula(f, yn+(h/2*k1), tn+(h/2))
		k3 = f_calcula(f, yn+(h/2*k2), tn+(h/2))
		k4 = f_calcula(f, yn+(h*k3), tn+h)
		yn = yn + h/6*(k1+2*k2+2*k3+k4) # formula tradicional do metodo de euler
		tn = tn + h # incrementa o tn para a proxima iteracao
		text_file.write("%d %.8f\n" % (int(x), float(yn)))
	text_file.write("\n")
	return

def aux_euler(expr, t0, y0, h, n):
    t = t0
    y = y0
    v_Aux.append([y,t])
    for i in range(0, n):
	    y = y + (h*f_calcula(expr,y,t)) # formula tradicional do metodo de euler
	    t = t + h
	    v_Aux.append([y,t])
    return

def aux_euler_inverso(expr,t0 ,y0 ,h, n):
	t = t0 # o primeiro valor para o tn sera o t0
	y = y0 # o primeiro valor para o yn sera o y0
	v_Aux.append([y, t])
	for i in range(n):
		k = y + h*f_calcula(expr, y, t)
		y = y + h*f_calcula(expr, k, t+h) # formula tradicional do metodo de euler
		t = t + h # incrementa o tn para a proxima iteracao
		v_Aux.append([y,t])
	return

def aux_euler_aprimorado(expr, t0, y0, h, n):
    t = t0
    y = y0
    v_Aux.append([y,t])
    for i in range(n):
	    k = y + h*f_calcula(expr,y,t)
	    y = y + h/2*(f_calcula(expr,y,t)+f_calcula(expr, k, t+h)) # formula tradicional do metodo de euler
	    t = t + h # incrementa o tn para a proxima iteracao
	    v_Aux.append([y,t])
    return

def aux_runge_kutta(expre,t0,y0,h,n):
    yA=y0
    t=t0
    y=y0
    v_Aux.append([y,t])
    for i in range(0,n):
	    k1 = f_calcula(expre, y, t)
	    k2 = f_calcula(expre, y +(h/2)*k1, t + h/2)
	    k3 = f_calcula(expre, y + (h/2)*k2, t + h/2)
	    k4 = f_calcula(expre, y + h*k3, t + h)
	    y += (h/6)*(k1 + 2*k2 + 2*k3 + k4)
	    t += h
	    v_Aux.append([y,t])
    return

def TY(grau,expre,str_expr):
    for i in range(0,grau):
        y=v_Aux[i][0]
        t=v_Aux[i][1]
        text_file.write("%d %.5f\n" % (int(i), float(y)))
        F.append([eval(str_expr),t])
    return

def Adams__Bashforth(metodo, str_expr, expre, y0, t0, h, n, grau):
	if(metodo == 'adam_bashforth_by_euler'):
		text_file.write('Metodo Adams Bashforth por Euler\n')
		aux_euler(expre, t0, y0, h, grau-1)
	elif(metodo == 'adam_bashforth_by_euler_inverso'):
		text_file.write('Metodo Adams Bashforth por Euler Inverso\n')
		aux_euler_inverso(expre, t0, y0, h, grau-1)
	elif(metodo == 'adam_bashforth_by_euler_aprimorado'):
		text_file.write('Metodo Adams Bashforth por Euler Aprimorado\n')
		aux_euler_aprimorado(expre, t0, y0, h, grau-1)
	elif(metodo == 'adam_bashforth_by_runge_kutta'):
		text_file.write('Metodo Adams Bashforth por Runge Kutta\n')
		aux_runge_kutta(expre,t0,y0,h,grau-1)

	text_file.write('y(%.2f) = %.5f\n' % (float(t0),float(y0)))
	text_file.write('h = %.2f\n' % float(h))
	TY(grau,expre,str_expr)
	yA = v_Aux[grau-1][0]
	tA = t0 + h*grau
	for i in range(grau,n+1):
		yP=yA+FAdamsBashforth(grau,i,h)
		yA=yP
		y=yP
		t=tA
		F.append([eval(str_expr),t])
		text_file.write("%d %.5f\n" % (int(i), float(y)))
		tA=tA+h
	text_file.write('\n')
	return

def FAdamsBashforth(grau,i,h):
    if(grau==2):
        FN=F[i+1-grau][0]
        FN_1=F[i-grau][0]
        return (h/2)*(3*FN-FN_1)
    elif(grau==3):
        FN=F[i+2-grau][0]
        FN_1=F[i+1-grau][0]
        FN_2=F[i-grau][0]
        return ((h/12)*(23*FN-16*FN_1+5*FN_2)) 
    elif(grau==4):
        FN=F[i+3-grau][0]
        FN_1=F[i+2-grau][0]
        FN_2=F[i+1-grau][0]
        FN_3=F[i-grau][0]
        return ((h/24)*(55*FN-59*FN_1+37*FN_2-9*FN_3)) 
    elif(grau==5):
        FN=F[i+4-grau][0]
        FN_1=F[i+3-grau][0]
        FN_2=F[i+2-grau][0]
        FN_3=F[i+1-grau][0]
        FN_4=F[i-grau][0]
        return ((h/720)*(1901*FN-2774*FN_1+2616*FN_2-1274*FN_3+251*FN_4)) 
    elif(grau==6):
        FN=F[i+5-grau][0]
        FN_1=F[i+4-grau][0]
        FN_2=F[i+3-grau][0]
        FN_3=F[i+2-grau][0]
        FN_4=F[i+1-grau][0]
        FN_5=F[i-grau][0]
        return (h/1440)*(4277*FN-7923*FN_1+9982*FN_2-7298*FN_3+2877*FN_4-475*FN_5)
    elif(grau == 7):
        FN=F[i+6-grau][0]
        FN_1=F[i+5-grau][0]
        FN_2=F[i+4-grau][0]
        FN_3=F[i+3-grau][0]
        FN_4=F[i+2-grau][0]
        FN_5=F[i+1-grau][0]                
        FN_6=F[i-grau][0]
        return (h/60480)*(198721*FN-447288*FN_1+705549*FN_2-688256*FN_3+407139*FN_4 \
        	   - 134472*FN_5+19087*FN_6)
    elif(grau == 8):
        FN=F[i+7-grau][0]
        FN_1=F[i+6-grau][0]
        FN_2=F[i+5-grau][0]
        FN_3=F[i+4-grau][0]
        FN_4=F[i+3-grau][0]
        FN_5=F[i+2-grau][0]                
        FN_6=F[i+1-grau][0]
        FN_7=F[i-grau][0]
        return (h/120960)*(434241*FN-1152169*FN_1+2183877*FN_2-2664477*FN_3+2102243*FN_4 \
        	   - 1041723*FN_5+295767*FN_6-36799*FN_7)

def Adams__Multon(metodo, str_expr, expre, y0, t0, h, n, grau):
	if(metodo == 'adam_multon_by_euler'):
		text_file.write('Metodo Adams Multon por Euler\n')
		aux_euler(expre, t0, y0, h, grau-2)
	elif(metodo == 'adam_multon_by_euler_inverso'):
		text_file.write('Metodo Adams Multon por Euler Inverso\n')
		aux_euler_inverso(expre, t0, y0, h, grau-2)	
	elif(metodo == 'adam_multon_by_euler_aprimorado'):
		text_file.write('Metodo Adams Multon por Euler Aprimorado\n')
		aux_euler_aprimorado(expre, t0, y0, h, grau-2)
	elif(metodo == 'adam_multon_by_runge_kutta'):
		text_file.write('Metodo Adams Multon por Runge Kutta\n')
		aux_runge_kutta(expre,t0,y0,h,grau-2)

	text_file.write('y(%.2f) = %.5f\n' % (float(t0),float(y0)))
	text_file.write('h = %.2f\n' % float(h))
	TY(grau-1,expre,str_expr)
	yf = v_Aux[grau-2][0]
	tf = t0 + (grau-2)*h
	for i in range(grau-2, n):
		yf = FAdamsMoulton(yf, expre, h, grau, i)
		v_Aux.append((yf, tf))
		text_file.write("%d %.5f\n" % (int(i+1), float(yf)))
		tf += h
	text_file.write('\n')
	return

def FAdamsMoulton(yf, expre, h, g, i):
	fn1 = f_calcula(expre, y, v_Aux[i][1]+h)
	fn2 = f_calcula(expre, v_Aux[i][0], v_Aux[i][1])
	if(g == 2):
		aux = yf + (h/2)*(fn1 + fn2)
	elif(g == 3):
		fn3 = f_calcula(expre, v_Aux[i-1][0], v_Aux[i-1][1])
		aux = (h/12)*(5*fn1 + 8*fn2 - fn3)
	elif(g == 4):
		fn3 = f_calcula(expre, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calcula(expre, v_Aux[i-2][0], v_Aux[i-2][1])
		aux = yf + (h/24)*(9*fn1 + 19*fn2 - 5*fn3 + 1*fn4)
	elif(g == 5):
		fn3 = f_calcula(expre, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calcula(expre, v_Aux[i-2][0], v_Aux[i-2][1])
		fn5 = f_calcula(expre, v_Aux[i-3][0], v_Aux[i-3][1])
		aux = yf + (h/720)*(251*fn1 + 646*fn2 - 264*fn3 + 106*fn4 - 19*fn5)
	elif(g == 6):
		fn3 = f_calcula(expre, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calcula(expre, v_Aux[i-2][0], v_Aux[i-2][1])
		fn5 = f_calcula(expre, v_Aux[i-3][0], v_Aux[i-3][1])
		fn6 = f_calcula(expre, v_Aux[i-4][0], v_Aux[i-4][1])
		aux = yf + (h/1440)*(475*fn1 + 1427*fn2 - 798*fn3 + 482*fn4 - 173*fn5 + 27*fn6)
	elif(g == 7):
		fn3 = f_calcula(expr, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calcula(expr, v_Aux[i-2][0], v_Aux[i-2][1])
		fn5 = f_calcula(expr, v_Aux[i-3][0], v_Aux[i-3][1])    	
		fn6 = f_calcula(expr, v_Aux[i-4][0], v_Aux[i-4][1])
		fn7 = f_calcula(expr, v_Aux[i-5][0], v_Aux[i-5][1])
		aux = yf + (h/60480)*(19087*fn1+65112*fn2-46461*fn3+37504*fn4-20211*fn5+6312*fn6-863*fn7)
	elif(g == 8):
		fn3 = f_calcula(expr, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calcula(expr, v_Aux[i-2][0], v_Aux[i-2][1])
		fn5 = f_calcula(expr, v_Aux[i-3][0], v_Aux[i-3][1])
		fn6 = f_calcula(expr, v_Aux[i-4][0], v_Aux[i-4][1])
		fn7 = f_calcula(expr, v_Aux[i-5][0], v_Aux[i-5][1])
		fn8 = f_calcula(expr, v_Aux[i-6][0], v_Aux[i-6][1])
		aux = yf + (h/120960)*(36799*fn1+139849*fn2-121797*fn3+123133*fn4 \
			  -88547*fn5+41499*fn6-11351*fn7+1375*fn8) # \ diz que a linha ainda nao acabou
	imp = Eq(aux, y)
	possibilidade = solve(imp, y)
	best = 1e18
	for i in range(0, len(possibilidade)):
		if(abs(yf-possibilidade[i]) < best):
			best = abs(yf-possibilidade[i])
			ind = i
	res = possibilidade[ind]
	return res

def FInversa(metodo, str_expr, expre, y0, t0, h, n, grau):
	if(metodo == 'formula_inversa_by_euler'):
		text_file.write('Metodo Formula Inversa de Diferenciação por Euler\n')
		aux_euler(expre, t0, y0, h, grau-1)
	elif(metodo == 'formula_inversa_by_euler_inverso'):
		text_file.write('Metodo Formula Inversa de Diferenciação por Euler Inverso\n')
		aux_euler_inverso(expre, t0, y0, h, grau-1)	
	elif(metodo == 'formula_inversa_by_euler_aprimorado'):
		text_file.write('Metodo Formula Inversa de Diferenciação por Euler Aprimorado\n')
		aux_euler_aprimorado(expre, t0, y0, h, grau-1)
	elif(metodo == 'formula_inversa_by_runge_kutta'):
		text_file.write('Metodo Formula Inversa de Diferenciação por Runge-Kutta\n')
		aux_runge_kutta(expre,t0,y0,h,grau-1)

	text_file.write('y(%.2f) = %.5f\n' % (float(t0),float(y0)))
	text_file.write('h = %.2f\n' % float(h))
	TY(grau, expre, str_expr)
	tf = t0 + (grau-1)*h
	yf = v_Aux[grau-1][0]
	for i in range(grau-1, n):
		yf = FInversaF(yf, expre, h, grau, i)
		v_Aux.append((yf, tf))
		text_file.write("%d %.5f\n" % (int(i+1), float(yf)))
		tf += h
	text_file.write('\n')
	return

def FInversaF(yf, expre, h, g, i):
	fn1 = f_calcula(expre, y, v_Aux[i][1]+h)
	fn2 = v_Aux[i-1][0]
	if(g == 2):
		aux = (1/3)*(4*yf - fn2 + 2*h*fn1)
	elif(g == 3):
		fn3 = v_Aux[i-2][0]
		aux = (1/11)*(18*yf - 9*fn2 + 2*fn3 + 6*h*fn1)
	elif(g == 4):
		fn3 = v_Aux[i-2][0]
		fn4 = v_Aux[i-3][0]
		aux = (1/25)*(48*yf - 36*fn2 + 16*fn3 - 3*fn4 + 12*h*fn1)
	elif(g == 5):
		fn3 = v_Aux[i-2][0]
		fn4 = v_Aux[i-3][0]
		fn5 = v_Aux[i-4][0]
		aux = (1/137)*(300*yf - 300*fn2 + 200*fn3 - 75*fn4 + 12*fn5 + 60*h*fn1)
	elif(g == 6):
		fn3 = v_Aux[i-2][0]
		fn4 = v_Aux[i-3][0]
		fn5 = v_Aux[i-4][0]
		fn6 = v_Aux[i-5][0]
		aux = (1/147)*(360*yf - 450*fn2 + 400*fn3 - 225*fn4 + 72*fn5 - 10*fn6 + 60*h*fn1)
	imp = Eq(aux, y)
	possibilidade = solve(imp, y)
	best = 1e18
	for i in range(0, len(possibilidade)):
		if(abs(yf-possibilidade[i]) < best):
			best = abs(yf-possibilidade[i])
			ind = i
	res = possibilidade[ind]
	return res

def main():
	adam_b = ['adam_bashforth_by_euler',
	          'adam_bashforth_by_euler_aprimorado',
	          'adam_bashforth_by_euler_inverso',
	          'adam_bashforth_by_runge_kutta']
	adam_m = ['adam_multon_by_euler',
	          'adam_multon_by_euler_aprimorado',
	          'adam_multon_by_euler_inverso',
	          'adam_multon_by_runge_kutta']
	formula_inversa = ['formula_inversa_by_euler',
	                   'formula_inversa_by_euler_aprimorado',
	                   'formula_inversa_by_euler_inverso',
	                   'formula_inversa_by_runge_kutta']
	
	start = False
	entrada = ''

	while(True):
		entrada = input()
		if(entrada == '///' and start == True): # ignora o primeiro '///'
			break
		if(entrada == '///'): # a partir de agora o proximo '///' finaliza o programa
			start = True
		entradas = entrada.split() # separa cada parte da entrada num indice do vetor
		if (entradas[0] == 'euler'):
			expr = sympify(entradas[5])
			t0 = float(entradas[1])
			y0 = float(entradas[2])
			h = float(entradas[3])
			n = int(entradas[4])
			euler(expr,t0,y0,h,n)
		elif (entradas[0] == 'euler_inverso'):
			expr = sympify(entradas[5])
			t0 = float(entradas[1])
			y0 = float(entradas[2])
			h = float(entradas[3])
			n = int(entradas[4])
			euler_inverso(expr,t0,y0,h,n)
		elif (entradas[0] == 'euler_aprimorado'):
			expr = sympify(entradas[5])
			t0 = float(entradas[1])
			y0 = float(entradas[2])
			h = float(entradas[3])
			n = int(entradas[4])
			euler_aprimorado(expr,t0,y0,h,n)
		elif (entradas[0] == 'runge_kutta'):
			expr = sympify(entradas[5])
			t0 = float(entradas[1])
			y0 = float(entradas[2])
			h = float(entradas[3])
			n = int(entradas[4])
			runge_kutta(expr,t0,y0,h,n)	
		elif (entradas[0] in adam_b): # se o metodo desejado estiver na lista adam_b entra no if
			expr = sympify(entradas[5])
			t0 = float(entradas[1])
			y0 = float(entradas[2])
			h = float(entradas[3])
			n = int(entradas[4])
			grau = int(entradas[6])
			Adams__Bashforth(entradas[0],entradas[5], expr, y0, t0, h, n, grau)
		elif (entradas[0] in adam_m): # se o metodo desejado estiver na lista adam_m entra no if
			expr = sympify(entradas[5])
			t0 = float(entradas[1])
			y0 = float(entradas[2])
			h = float(entradas[3])
			n = int(entradas[4])
			grau = int(entradas[6])
			tf = (t0 + (h*n))
			Adams__Multon(entradas[0], entradas[5], expr, y0, t0, h, n, grau)
		elif (entradas[0] in formula_inversa): # se o metodo desejado estiver na lista adam_m entra no if
			expr = sympify(entradas[5])
			t0 = float(entradas[1])
			y0 = float(entradas[2])
			h = float(entradas[3])
			n = int(entradas[4])
			grau = int(entradas[6])
			tf = (t0 + (h*n))
			FInversa(entradas[0], entradas[5], expr, y0, t0, h, n, grau)
		del F[:]
		del v_Aux[:]
	text_file.write('///')
	# vy.append(y0)
	# vx.append(t0)

	# print("y(%.5f) = %.5f" % (float(t0), float(y0)))
	# euler(expr,t0,y0,h,n)

	# plt.title("Metodo de Euler")
	# plt.xlabel('t')
	# plt.ylabel('y')     
	# plt.plot(vx, vy,'go')
	# plt.plot(vx, vy, 'k:', color='blue')

	# #Show graph
	# plt.show()

if __name__ == "__main__":
	main()