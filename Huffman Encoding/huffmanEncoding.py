import numpy as np
import cv2
import matplotlib.pyplot as plt
import queue

class Node:
	def __init__(self):
		self.prob = None
		self.code = None
		self.data = None
		self.left = None
		self.right = None 	
	def __lt__(self, other):
		if (self.prob < other.prob):		
			return 1
		else:
			return 0
	def __ge__(self, other):
		if (self.prob > other.prob):
			return 1
		else:
			return 0
def get2smallest(data):			
    first = second = 1;
    fid=sid=0
    for idx,element in enumerate(data):
        if (element < first):
            second = first
            sid = fid
            first = element
            fid = idx
        elif (element < second and element != first):
            second = element
    return fid,first,sid,second
    
def tree(probabilities):
	prq = queue.PriorityQueue()
	for color,probability in enumerate(probabilities):
		leaf = Node()
		leaf.data = color
		leaf.prob = probability
		prq.put(leaf)

	while (prq.qsize()>1):
		newnode = Node()		
		l = prq.get()
		r = prq.get()							
		newnode.left = l 		
		newnode.right = r
		newprob = l.prob+r.prob	
		newnode.prob = newprob
		prq.put(newnode)	
	return prq.get()		

def huffman_traversal(root_node,tmp_array):		
	if (root_node.left is not None):
		tmp_array[huffman_traversal.count] = 1
		huffman_traversal.count+=1
		huffman_traversal(root_node.left,tmp_array)
		huffman_traversal.count-=1
	if (root_node.right is not None):
		tmp_array[huffman_traversal.count] = 0
		huffman_traversal.count+=1
		huffman_traversal(root_node.right,tmp_array)
		huffman_traversal.count-=1
	else:
		huffman_traversal.output_bits[root_node.data] = huffman_traversal.count		
		bitstream = ''.join(str(cell) for cell in tmp_array[1:huffman_traversal.count]) 
		color = str(root_node.data)
		wr_str = color+' '+ bitstream+'\n'
		print(wr_str)

img = cv2.imread('baboon.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = np.bincount(gray_img.ravel(),minlength=256)
probabilities = hist/np.sum(hist)		
root_node = tree(probabilities)			
tmp_array = np.ones([64],dtype=int)
huffman_traversal.output_bits = np.empty(256,dtype=int) 
huffman_traversal.count = 0
huffman_traversal(root_node,tmp_array)		

