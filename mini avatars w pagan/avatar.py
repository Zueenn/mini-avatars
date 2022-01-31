import pagan

input = input("İsim: ")
img = pagan.Avatar(input, pagan.SHA512)
img.show()

outpath = "output/"
filename = input + ".png"
img.save(outpath, filename)