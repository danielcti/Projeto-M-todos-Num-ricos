from sympy import *
import matplotlib.pyplot as plt

#global variables
y, t = symbols('y t') # 
v_Aux = [] # list that store the points by AB, AM and IF
text_file = open("output.txt", "w") # file that stores all outputs
vx = []
vy = []
count = 0 
plotar = False

def f_calculate(f,yn,tn): #calculates the yn and tn applied in function f
	f = f.subs('t',tn)
	f = f.subs('y',yn)
	return f

def plot(vx, vy, metodo): #plot function
	global plotar
	global count
	count += 1
	if(plotar):
		plt.figure(0).canvas.set_window_title('Metodo %d' % int(count))
		plt.xlabel("t")
		plt.ylabel("y")
		plt.title(metodo)
		plt.plot(vx, vy, 'go')
		plt.plot(vx, vy, 'k:', color='blue')
		plt.show()
#######
#single methods
def euler(f,y0,t0,h,n):
	tn = t0 # o primeiro valor para o tn sera o t0
	yn = y0 # o primeiro valor para o yn sera o y0

	text_file.write("Metodo de Euler\n")
	text_file.write("y(%.5f) = %.8f\n" % (float(tn), float(yn)))
	text_file.write("h = %.5f\n" % (float(h)))
	text_file.write("0 %.5f\n" % (float(yn)))
	vx.append(tn) # append a t point to plot later
	vy.append(yn) # append a y point to plot later
	for x in range(1,n+1):
		yn = yn + h*f_calculate(f,yn,tn) # formula tradicional do metodo de euler
		tn = tn + h # incrementa o tn para a proxima iteracao
		vx.append(tn)
		vy.append(yn)
		text_file.write("%d %.8f\n" % (int(x), float(yn)))
	text_file.write("\n")
	plot(vx, vy,'Euler')
	return 

def euler_inverso(f,y0,t0,h,n):
	tn = t0
	yn = y0

	text_file.write("Metodo de Euler Inverso\n")
	text_file.write("y(%.5f) = %.8f\n" % (float(tn), float(yn)))
	text_file.write("h = %.5f\n" % (float(h)))
	text_file.write("0 %.5f\n" % (float(yn)))
	vx.append(t0)
	vy.append(y0)
	for x in range(1,n+1):
		k = yn + h*f_calculate(f,yn,tn)
		yn = yn + h*f_calculate(f, k, tn+h) 
		tn = tn + h 
		vx.append(tn)
		vy.append(yn)
		text_file.write("%d %.8f\n" % (int(x), float(yn)))
	text_file.write("\n")
	plot(vx,vy,'Euler Inverso')
	return

def euler_aprimorado(f,y0,t0,h,n):
	tn = t0
	yn = y0

	text_file.write("Metodo de Euler Aprimorado\n")
	text_file.write("y(%.5f) = %.8f\n" % (float(tn), float(yn)))
	text_file.write("h = %.5f\n" % (float(h)))
	text_file.write("0 %.5f\n" % (float(yn)))
	vx.append(t0)
	vy.append(y0)
	for x in range(1,n+1):
		k = yn + h*f_calculate(f,yn,tn)
		yn = yn + h/2*(f_calculate(f, yn, tn)+f_calculate(f, k, tn+h)) 
		tn = tn + h 
		vx.append(tn)
		vy.append(yn)
		text_file.write("%d %.8f\n" % (int(x), float(yn)))
	text_file.write("\n")
	plot(vx,vy,'Euler Aprimorado')
	return

def runge_kutta(f,y0,t0,h,n):
	tn = t0
	yn = y0

	text_file.write("Metodo de Runge-Kutta\n")
	text_file.write("y(%.5f) = %.8f\n" % (float(tn), float(yn)))
	text_file.write("h = %.5f\n" % (float(h)))
	text_file.write("0 %.5f\n" % (float(yn)))
	vx.append(t0)
	vy.append(y0)
	for x in range(1,n+1):
		k1 = f_calculate(f, yn, tn)
		k2 = f_calculate(f, yn+(h/2*k1), tn+(h/2))
		k3 = f_calculate(f, yn+(h/2*k2), tn+(h/2))
		k4 = f_calculate(f, yn+(h*k3), tn+h)
		yn = yn + h/6*(k1+2*k2+2*k3+k4)
		tn = tn + h
		vx.append(tn)
		vy.append(yn)
		text_file.write("%d %.8f\n" % (int(x), float(yn)))
	text_file.write("\n")
	plot(vx,vy,'Runge Kutta')
	return
#######
# auxiliar methods
def aux_euler(f, y0, t0, h, n):
	t = t0
	y = y0
	v_Aux.append([y,t]) # da append na tupla para outro metodo utilizar os pontos
	for i in range(0, n):
		y = y + (h*f_calculate(f,y,t))
		t = t + h
		v_Aux.append([y,t])
	return

def aux_euler_inverso(f, y0 ,t0 ,h, n):
	t = t0 
	y = y0 
	v_Aux.append([y, t])
	for i in range(n):
		k = y + h*f_calculate(f, y, t)
		y = y + h*f_calculate(f, k, t+h) 
		t = t + h 
		v_Aux.append([y,t])
	return

def aux_euler_aprimorado(f, y0, t0, h, n):
    t = t0
    y = y0
    v_Aux.append([y,t])
    for i in range(n):
	    k = y + h*f_calculate(f,y,t)
	    y = y + h/2*(f_calculate(f,y,t)+f_calculate(f, k, t+h))
	    t = t + h 
	    v_Aux.append([y,t])
    return

def aux_runge_kutta(f, y0, t0, h, n):
    y=y0
    t=t0
    v_Aux.append([y,t])
    for i in range(0,n):
	    k1 = f_calculate(f, y, t)
	    k2 = f_calculate(f, y +(h/2)*k1, t + h/2)
	    k3 = f_calculate(f, y + (h/2)*k2, t + h/2)
	    k4 = f_calculate(f, y + h*k3, t + h)
	    y += (h/6)*(k1 + 2*k2 + 2*k3 + k4)
	    t += h
	    v_Aux.append([y,t])
    return
#######
def printInitialPoints(grau):
    for i in range(0,grau):
        y=v_Aux[i][0]
        t=v_Aux[i][1]
        vx.append(t)
        vy.append(y)
        text_file.write("%d %.5f\n" % (int(i), float(y)))
    return

def Adams__Bash(metodo, f, y0, t0, h, n, grau):
	if(metodo == 'adam_bashforth_by_euler'):
		text_file.write('Metodo Adams Bashforth por Euler\n')
		aux_euler(f,y0,t0,h,grau-1)
	elif(metodo == 'adam_bashforth_by_euler_inverso'):
		text_file.write('Metodo Adams Bashforth por Euler Inverso\n')
		aux_euler_inverso(f,y0,t0,h,grau-1)
	elif(metodo == 'adam_bashforth_by_euler_aprimorado'):
		text_file.write('Metodo Adams Bashforth por Euler Aprimorado\n')
		aux_euler_aprimorado(f,y0,t0,h,grau-1)
	elif(metodo == 'adam_bashforth_by_runge_kutta'):
		text_file.write('Metodo Adams Bashforth por Runge Kutta\n')
		aux_runge_kutta(f,y0,t0,h,grau-1)
	elif(metodo == 'adam_bashforth'):
		text_file.write('Metodo Adams Bashforth\n')

	text_file.write('y(%.2f) = %.5f\n' % (float(t0),float(y0)))
	text_file.write('h = %.2f\n' % float(h))
	printInitialPoints(grau)
	
	tf = t0 + (grau-1)*h
	yf = v_Aux[grau-1][0]
	for i in range(grau-1, n):
		yf += AdamBashF(f, h, grau, i)
		tf += h
		vx.append(tf)
		vy.append(yf)	
		v_Aux.append((yf, tf))
		text_file.write("%d %.5f\n" % (int(i+1), float(yf)))
	text_file.write('\n')
	plot(vx,vy,metodo)
	return

def Adams__Multon(metodo, f, y0, t0, h, n, grau):
	if(metodo == 'adam_multon_by_euler'):
		text_file.write('Metodo Adams Multon por Euler\n')
		aux_euler(f,y0,t0,h,grau-2)
	elif(metodo == 'adam_multon_by_euler_inverso'):
		text_file.write('Metodo Adams Multon por Euler Inverso\n')
		aux_euler_inverso(f,y0,t0,h,grau-2)	
	elif(metodo == 'adam_multon_by_euler_aprimorado'):
		text_file.write('Metodo Adams Multon por Euler Aprimorado\n')
		aux_euler_aprimorado(f,y0,t0,h,grau-2)
	elif(metodo == 'adam_multon_by_runge_kutta'):
		text_file.write('Metodo Adams Multon por Runge Kutta\n')
		aux_runge_kutta(f,y0,t0,h,grau-2)
	elif(metodo == 'adam_multon'):
		text_file.write('Metodo Adams Multon\n')

	text_file.write('y(%.2f) = %.5f\n' % (float(t0),float(y0)))
	text_file.write('h = %.2f\n' % float(h))
	printInitialPoints(grau-1)
	yf = v_Aux[grau-2][0]
	tf = t0 + (grau-2)*h
	for i in range(grau-2, n):
		yf = AdamMultonF(yf,f,h,grau,i)
		v_Aux.append((yf,tf))
		vx.append(tf)
		vy.append(yf)
		text_file.write("%d %.5f\n" % (int(i+1), float(yf)))
		tf += h
	text_file.write('\n')
	plot(vx,vy,metodo)
	return

def FInversa(metodo, f, y0, t0, h, n, grau):
	if (metodo == 'formula_inversa_by_euler'):
		text_file.write('Metodo Formula Inversa de Diferenciação por Euler\n')
		aux_euler(f,y0,t0,h,grau-1)
	elif (metodo == 'formula_inversa_by_euler_inverso'):
		text_file.write('Metodo Formula Inversa de Diferenciação por Euler Inverso\n')
		aux_euler_inverso(f,y0,t0,h,grau-1)	
	elif (metodo == 'formula_inversa_by_euler_aprimorado'):
		text_file.write('Metodo Formula Inversa de Diferenciação por Euler Aprimorado\n')
		aux_euler_aprimorado(f,y0,t0,h,grau-1)
	elif (metodo == 'formula_inversa_by_runge_kutta'):
		text_file.write('Metodo Formula Inversa de Diferenciação por Runge-Kutta\n')
		aux_runge_kutta(f,y0,t0,h,grau-1)
	elif (metodo == 'formula_inversa'):
		text_file.write('Formula Inversa\n')

	text_file.write('y(%.2f) = %.5f\n' % (float(t0),float(y0)))
	text_file.write('h = %.2f\n' % float(h))
	printInitialPoints(grau)
	tf = t0 + (grau-1)*h
	yf = v_Aux[grau-1][0]
	for i in range(grau-1, n):
		yf = FInversaF(yf,f,h,grau,i)
		tf += h
		v_Aux.append((yf, tf))
		vx.append(tf)
		vy.append(yf)
		text_file.write("%d %.5f\n" % (int(i+1), float(yf)))
	text_file.write('\n')
	plot(vx,vy,metodo)
	return

def AdamBashF(f, h, g, i):
	fn1 = f_calculate(f, v_Aux[i][0], v_Aux[i][1])
	fn2 = f_calculate(f, v_Aux[i-1][0], v_Aux[i-1][1])
	if(g == 2):
		res = (h/2)*(3*fn1 - fn2)
	elif(g == 3):
		fn3 = f_calculate(f, v_Aux[i-2][0], v_Aux[i-2][1])
		res = (h/12)*(23*fn1 - 16*fn2 + 5*fn3)
	elif(g == 4):
		fn3 = f_calculate(f, v_Aux[i-2][0], v_Aux[i-2][1])
		fn4 = f_calculate(f, v_Aux[i-3][0], v_Aux[i-3][1])
		res = (h/24)*(55*fn1 - 59*fn2 + 37*fn3 - 9*fn4)
	elif(g == 5):
		fn3 = f_calculate(f, v_Aux[i-2][0], v_Aux[i-2][1])
		fn4 = f_calculate(f, v_Aux[i-3][0], v_Aux[i-3][1])
		fn5 = f_calculate(f, v_Aux[i-4][0], v_Aux[i-4][1])
		res = (h/720)*(1901*fn1 - 2774*fn2 + 2616*fn3 - 1274*fn4 + 251*fn5)
	elif(g == 6):
		fn3 = f_calculate(f, v_Aux[i-2][0], v_Aux[i-2][1])
		fn4 = f_calculate(f, v_Aux[i-3][0], v_Aux[i-3][1])
		fn5 = f_calculate(f, v_Aux[i-4][0], v_Aux[i-4][1])
		fn6 = f_calculate(f, v_Aux[i-5][0], v_Aux[i-5][1])
		res = (h/1440)*(4277*fn1 - 7923*fn2 + 9982*fn3 - 7298*fn4 + 2877*fn5 - 475*fn6)
	return res

def AdamMultonF(yf, f, h, g, i):
	fn1 = f_calculate(f, y, v_Aux[i][1]+h)
	fn2 = f_calculate(f, v_Aux[i][0], v_Aux[i][1])
	if(g == 2):
		aux = yf + (h/2)*(fn1 + fn2)
	elif(g == 3):
		fn3 = f_calculate(f, v_Aux[i-1][0], v_Aux[i-1][1])
		aux = (h/12)*(5*fn1 + 8*fn2 - fn3)
	elif(g == 4):
		fn3 = f_calculate(f, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calculate(f, v_Aux[i-2][0], v_Aux[i-2][1])
		aux = yf + (h/24)*(9*fn1 + 19*fn2 - 5*fn3 + 1*fn4)
	elif(g == 5):
		fn3 = f_calculate(f, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calculate(f, v_Aux[i-2][0], v_Aux[i-2][1])
		fn5 = f_calculate(f, v_Aux[i-3][0], v_Aux[i-3][1])
		aux = yf + (h/720)*(251*fn1 + 646*fn2 - 264*fn3 + 106*fn4 - 19*fn5)
	elif(g == 6):
		fn3 = f_calculate(f, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calculate(f, v_Aux[i-2][0], v_Aux[i-2][1])
		fn5 = f_calculate(f, v_Aux[i-3][0], v_Aux[i-3][1])
		fn6 = f_calculate(f, v_Aux[i-4][0], v_Aux[i-4][1])
		aux = yf + (h/1440)*(475*fn1 + 1427*fn2 - 798*fn3 + 482*fn4 - 173*fn5 + 27*fn6)
	elif(g == 7):
		fn3 = f_calculate(f, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calculate(f, v_Aux[i-2][0], v_Aux[i-2][1])
		fn5 = f_calculate(f, v_Aux[i-3][0], v_Aux[i-3][1])    	
		fn6 = f_calculate(f, v_Aux[i-4][0], v_Aux[i-4][1])
		fn7 = f_calculate(f, v_Aux[i-5][0], v_Aux[i-5][1])
		aux = yf + (h/60480)*(19087*fn1+65112*fn2-46461*fn3+37504*fn4-20211*fn5+6312*fn6-863*fn7)
	elif(g == 8):
		fn3 = f_calculate(f, v_Aux[i-1][0], v_Aux[i-1][1])
		fn4 = f_calculate(f, v_Aux[i-2][0], v_Aux[i-2][1])
		fn5 = f_calculate(f, v_Aux[i-3][0], v_Aux[i-3][1])
		fn6 = f_calculate(f, v_Aux[i-4][0], v_Aux[i-4][1])
		fn7 = f_calculate(f, v_Aux[i-5][0], v_Aux[i-5][1])
		fn8 = f_calculate(f, v_Aux[i-6][0], v_Aux[i-6][1])
		aux = yf + (h/120960)*(36799*fn1+139849*fn2-121797*fn3+123133*fn4 \
			  -88547*fn5+41499*fn6-11351*fn7+1375*fn8) # \ diz que a linha ainda nao acabou
	res = solve(Eq(aux, y), y) # solve the equation
	return res[0]

def FInversaF(yf, f, h, g, i):
	fn1 = f_calculate(f, y, v_Aux[i][1]+h)
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
	res = solve(Eq(aux, y), y) # solve the equation
	return res[0]

def init(entradas):# function that chooses which method will be called
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

	if (entradas[0] == 'euler'):
		f = sympify(entradas[5])
		y0 = float(entradas[1])
		t0 = float(entradas[2])
		h = float(entradas[3])
		n = int(entradas[4])
		euler(f,y0,t0,h,n)
	elif (entradas[0] == 'euler_inverso'):
		f = sympify(entradas[5])
		y0 = float(entradas[1])
		t0 = float(entradas[2])
		h = float(entradas[3])
		n = int(entradas[4])
		euler_inverso(f,y0,t0,h,n)
	elif (entradas[0] == 'euler_aprimorado'):
		f = sympify(entradas[5])
		y0 = float(entradas[1])
		t0 = float(entradas[2])
		h = float(entradas[3])
		n = int(entradas[4])
		euler_aprimorado(f,y0,t0,h,n)
	elif (entradas[0] == 'runge_kutta'):
		f = sympify(entradas[5])
		y0 = float(entradas[1])
		t0 = float(entradas[2])
		h = float(entradas[3])
		n = int(entradas[4])
		runge_kutta(f,y0,t0,h,n)	
	elif (entradas[0] == 'adam_bashforth'):
		grau = int(entradas[-1])
		f = sympify(entradas[-2])
		n = int(entradas[-3])
		h = float(entradas[-4])
		t0 = float(entradas[-5])
		y0 = float(entradas[1])
		v_Aux.append([float(entradas[1]),t0]) # primeiro ponto
		if (grau == 2):
			Adams__Bash(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 3):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			Adams__Bash(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 4):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto				
			Adams__Bash(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 5):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto				
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			Adams__Bash(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 6):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			v_Aux.append([float(entradas[5]),t0+h*4]) # quinto ponto
			Adams__Bash(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 7):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			v_Aux.append([float(entradas[5]),t0+h*4]) # quinto ponto
			v_Aux.append([float(entradas[6]),t0+h*5]) # sexto ponto
			Adams__Bash(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 8):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			v_Aux.append([float(entradas[5]),t0+h*4]) # quinto ponto
			v_Aux.append([float(entradas[6]),t0+h*5]) # sexto ponto
			v_Aux.append([float(entradas[7]),t0+h*6]) # setimo ponto
			Adams__Bash(entradas[0], f, y0, t0, h, n, grau-1)
	elif (entradas[0] in adam_b): # se o metodo desejado estiver na lista adam_b entra no if
		f = sympify(entradas[5])
		y0 = float(entradas[1])
		t0 = float(entradas[2])
		h = float(entradas[3])
		n = int(entradas[4])
		grau = int(entradas[6])
		Adams__Bash(entradas[0], f, y0, t0, h, n, grau)
	elif (entradas[0] == 'adam_multon'):
		grau = int(entradas[-1])
		f = sympify(entradas[-2])
		n = int(entradas[-3])
		h = float(entradas[-4])
		t0 = float(entradas[-5])
		y0 = float(entradas[1])
		v_Aux.append([float(entradas[1]),t0]) # primeiro ponto
		if (grau == 2):
			Adams__Multon(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 3):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			Adams__Multon(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 4):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto				
			Adams__Multon(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 5):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto				
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			Adams__Multon(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 6):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			v_Aux.append([float(entradas[5]),t0+h*4]) # quinto ponto
			Adams__Multon(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 7):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			v_Aux.append([float(entradas[5]),t0+h*4]) # quinto ponto
			v_Aux.append([float(entradas[6]),t0+h*5]) # sexto ponto
			Adams__Multon(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 8):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			v_Aux.append([float(entradas[5]),t0+h*4]) # quinto ponto
			v_Aux.append([float(entradas[6]),t0+h*5]) # sexto ponto
			v_Aux.append([float(entradas[7]),t0+h*6]) # setimo ponto
			Adams__Multon(entradas[0], f, y0, t0, h, n, grau-1)
	elif (entradas[0] in adam_m): # se o metodo desejado estiver na lista adam_m entra no if
		f = sympify(entradas[5])
		y0 = float(entradas[1])
		t0 = float(entradas[2])
		h = float(entradas[3])
		n = int(entradas[4])
		grau = int(entradas[6])
		tf = (t0 + (h*n))
		Adams__Multon(entradas[0], f, y0, t0, h, n, grau)
	elif (entradas[0] == 'formula_inversa'):
		grau = int(entradas[-1])
		f = sympify(entradas[-2])
		n = int(entradas[-3])
		h = float(entradas[-4])
		t0 = float(entradas[-5])
		y0 = float(entradas[1])
		v_Aux.append([float(entradas[1]),t0]) # primeiro ponto
		if (grau == 2):
			FInversa(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 3):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			FInversa(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 4):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto				
			FInversa(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 5):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto				
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			FInversa(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 6):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			v_Aux.append([float(entradas[5]),t0+h*4]) # quinto ponto
			FInversa(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 7):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			v_Aux.append([float(entradas[5]),t0+h*4]) # quinto ponto
			v_Aux.append([float(entradas[6]),t0+h*5]) # sexto ponto
			FInversa(entradas[0], f, y0, t0, h, n, grau-1)
		elif (grau == 8):
			v_Aux.append([float(entradas[2]),t0+h]) # segundo ponto
			v_Aux.append([float(entradas[3]),t0+h*2]) # terceiro ponto
			v_Aux.append([float(entradas[4]),t0+h*3]) # quarto ponto
			v_Aux.append([float(entradas[5]),t0+h*4]) # quinto ponto
			v_Aux.append([float(entradas[6]),t0+h*5]) # sexto ponto
			v_Aux.append([float(entradas[7]),t0+h*6]) # setimo ponto
			FInversa(entradas[0], f, y0, t0, h, n, grau-1)
	elif (entradas[0] in formula_inversa): # se o metodo desejado estiver na lista adam_m entra no if
		f = sympify(entradas[5])
		y0 = float(entradas[1])
		t0 = float(entradas[2])
		h = float(entradas[3])
		n = int(entradas[4])
		grau = int(entradas[6])
		tf = (t0 + (h*n))
		FInversa(entradas[0], f, y0, t0, h, n, grau)

def main():
	global plotar
	entrada = ''
	if(input() == 'plot'): # will plot the graphs
		plotar = True
	
	while(True):
		entrada = input() # reads user input
		if(entrada == '///'): # end of program
			break
		entradas = entrada.split() # splits all 'words' of entrada in an index of entradas
		init(entradas) # function that chooses which method will be called
		del v_Aux[:] # clears v_Aux list to use in the next iteration
		del vx[:]
		del vy[:]
	text_file.write('///')

if __name__ == "__main__":
	main()