from math import exp

from math import tanh

class test:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.459987)/0.0509152
		self.input1 = (in1 - 0.188581)/0.0656804
		self.input2 = (in2 - 134.719)/16.5033
		if index==0: return self.neuron0x2707960();
		return 0.
	def neuron0x26f41c0(self):
		return self.input0
	def neuron0x26f4500(self):
		return self.input1
	def neuron0x27054d0(self):
		return self.input2
	def neuron0x2705820(self):
		input = 2.02861
		input = input + self.synapse0x26bc9c0()
		input = input + self.synapse0x2705ad0()
		input = input + self.synapse0x2705b10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2705b50(self):
		input = 0.305087
		input = input + self.synapse0x2705e90()
		input = input + self.synapse0x2705ed0()
		input = input + self.synapse0x2705f10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2705f50(self):
		input = -0.203123
		input = input + self.synapse0x2706290()
		input = input + self.synapse0x27062d0()
		input = input + self.synapse0x2706310()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2706350(self):
		input = 0.983547
		input = input + self.synapse0x2706690()
		input = input + self.synapse0x27066d0()
		input = input + self.synapse0x2706710()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2706750(self):
		input = -1.01972
		input = input + self.synapse0x2706a90()
		input = input + self.synapse0x2706ad0()
		input = input + self.synapse0x2706b10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2706b50(self):
		input = -0.702413
		input = input + self.synapse0x2706e90()
		input = input + self.synapse0x2706ed0()
		input = input + self.synapse0x252c7b0()
		input = input + self.synapse0x252c7f0()
		input = input + self.synapse0x2707020()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2707060(self):
		input = 0.794697
		input = input + self.synapse0x27073a0()
		input = input + self.synapse0x27073e0()
		input = input + self.synapse0x2707420()
		input = input + self.synapse0x2707460()
		input = input + self.synapse0x27074a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x27074e0(self):
		input = -0.247216
		input = input + self.synapse0x2707820()
		input = input + self.synapse0x2707860()
		input = input + self.synapse0x27078a0()
		input = input + self.synapse0x27078e0()
		input = input + self.synapse0x2707920()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2707960(self):
		input = 0.594293
		input = input + self.synapse0x2707b80()
		input = input + self.synapse0x2707bc0()
		input = input + self.synapse0x2707c00()
		return (input*1)+0
	def synapse0x26bc9c0(self):
		return (self.neuron0x26f41c0()*-0.866166)
	def synapse0x2705ad0(self):
		return (self.neuron0x26f4500()*3.04345)
	def synapse0x2705b10(self):
		return (self.neuron0x27054d0()*-2.71806)
	def synapse0x2705e90(self):
		return (self.neuron0x26f41c0()*-0.375732)
	def synapse0x2705ed0(self):
		return (self.neuron0x26f4500()*-0.595569)
	def synapse0x2705f10(self):
		return (self.neuron0x27054d0()*0.871977)
	def synapse0x2706290(self):
		return (self.neuron0x26f41c0()*0.31896)
	def synapse0x27062d0(self):
		return (self.neuron0x26f4500()*-2.39006)
	def synapse0x2706310(self):
		return (self.neuron0x27054d0()*2.69674)
	def synapse0x2706690(self):
		return (self.neuron0x26f41c0()*-1.67338)
	def synapse0x27066d0(self):
		return (self.neuron0x26f4500()*-1.49408)
	def synapse0x2706710(self):
		return (self.neuron0x27054d0()*-0.534733)
	def synapse0x2706a90(self):
		return (self.neuron0x26f41c0()*3.12499)
	def synapse0x2706ad0(self):
		return (self.neuron0x26f4500()*0.423476)
	def synapse0x2706b10(self):
		return (self.neuron0x27054d0()*-3.31871)
	def synapse0x2706e90(self):
		return (self.neuron0x2705820()*-0.56222)
	def synapse0x2706ed0(self):
		return (self.neuron0x2705b50()*-1.5755)
	def synapse0x252c7b0(self):
		return (self.neuron0x2705f50()*-0.352675)
	def synapse0x252c7f0(self):
		return (self.neuron0x2706350()*-0.160099)
	def synapse0x2707020(self):
		return (self.neuron0x2706750()*-0.792308)
	def synapse0x27073a0(self):
		return (self.neuron0x2705820()*0.658797)
	def synapse0x27073e0(self):
		return (self.neuron0x2705b50()*1.10686)
	def synapse0x2707420(self):
		return (self.neuron0x2705f50()*0.0664966)
	def synapse0x2707460(self):
		return (self.neuron0x2706350()*-0.236156)
	def synapse0x27074a0(self):
		return (self.neuron0x2706750()*1.54544)
	def synapse0x2707820(self):
		return (self.neuron0x2705820()*-1.98104)
	def synapse0x2707860(self):
		return (self.neuron0x2705b50()*-2.31196)
	def synapse0x27078a0(self):
		return (self.neuron0x2705f50()*1.09036)
	def synapse0x27078e0(self):
		return (self.neuron0x2706350()*0.943681)
	def synapse0x2707920(self):
		return (self.neuron0x2706750()*-0.723827)
	def synapse0x2707b80(self):
		return (self.neuron0x2706b50()*0.528521)
	def synapse0x2707bc0(self):
		return (self.neuron0x2707060()*-0.779889)
	def synapse0x2707c00(self):
		return (self.neuron0x27074e0()*2.19178)
