def Penjumlahan():
	hasil=500+200
	return hasil
  print Penjumlahan()
def Penjumlahan(*args):
	hasil=500+200
	return hasil
print Penjumlahan()
def Pengurangan():
	hasil=700-190
	return hasil
  print Pengurangan()
def Pengurangan(*args):
	hasil=700-190
	return hasil
  print Pengurangan()
def Tampil(func,func1):
	print "Anto memiliki bebek ",func()," ekor
	print "Bebek anto pada tahun 2013 menjadi "func1()" karena mati keracunan di Mataram"

def Utama():
	Tampil(Penjumlahan,Pengurangan)

#pemanggilan fungsi Utama
Utama()
