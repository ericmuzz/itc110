print("hello, world!")
#hello, world!
print("hello","world!")
#hello world!
print(3)
#3
print(3.0)
#3.0
print(2+3)
#5
print(2.0+3.0)
#5.0
print("2"+"3")
#23
print("2+3=",2+3)
#2+3= 5
print(2*3)
#6
print(2**3)
#8
print(7/3)
#2.3333333333333335
print(7//3)
#2

#File: Chaos.py
#A simple program illustrating chaotic behavior

def main():
	print("this program illustrates a chaotic function")
	x = eval(input("enter a number between 0 and 1: "))
	for i in range (10):
		x=3.9*x*(1-x)
		print(x)

main()
#this program illustrates a chaotic function
#enter a number between 0 and 1: .24
#0.71136
#0.80077510656
#0.6221839075679007
#0.916777261652611
#0.2975571852604691
#0.8151659363653104
#0.5876146869644107
#0.9450622998497004
#.2024862420847321
#0.6297936990194279

main()
#this program illustrates a chaotic function
#enter a number between 0 and 1: .28
#0.78624
#0.6554599833599999
#0.8807455549374634
#0.4096280073419158
#0.9431483214777279
#0.2091163041687422
#0.6450080344482383
#0.8929934127872883
#0.3726690922726202
#0.9117686757555539

main()
#this program illustrates a chaotic function
#enter a number between 0 and 1: .45
#0.96525
#0.1308155062499998
#0.44344095734076866
#0.9625241913045378
#0.1406783525865249
#0.4714630194302584
#0.9718239988858525
#0.10679024489391603
#0.37200574510871254
#0.9111081357878141

main()
#this program illustrates a chaotic function
#enter a number between 0 and 1: .76
#0.71136
#0.80077510656
#0.6221839075679007
#0.916777261652611
#0.2975571852604691
#0.8151659363653104
#0.5876146869644107
#0.9450622998497004
#0.2024862420847321
#0.6297936990194279

main()
#this program illustrates a chaotic function
#enter a number between 0 and 1: .91
#0.31940999999999986
#0.8478102824099998
#0.5032092290545171
#0.974959833310615
#0.09521131129205605
#0.3359698582270027
#0.8700670391007285
#0.4408965076277576
#0.9613764310386769
#0.14481397663985088

main()
#this program illustrates a chaotic function
#enter a number between 0 and 1: .43
#0.9558900000000001
#0.16444080080999954
#0.5358600929719658
#0.9699848095549637
#0.1135456872715796
#0.39254695027705655
#0.9299699842104306
#0.25399066944451987
#0.7389696961906136
#0.7522845887800067