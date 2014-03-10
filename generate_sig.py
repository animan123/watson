import os
import cPickle
import tokenizer
import generate_fingerprint
class generate_sig:
	def generate_signature(self,filename):
		self.filename=filename
		self.t=tokenizer.tokenizer(self.filename)
		self.L=self.t.parse()
		self.gf= generate_fingerprint.generate_fingerprint()
		self.gf.group(self.L)
		self.filepath=os.path.splitext(filename)
		self.sigpath=self.filepath[0]+".sig"
		self.sigfile=open(self.sigpath,"w")
		cPickle.dump(self.gf.x,self.sigfile)
		#use list = cPickle.unload(sigfile) to retrive list from sigfile
if __name__ == "__main__" :
	gs=generate_sig()
	gs.generate_signature("test.txt")