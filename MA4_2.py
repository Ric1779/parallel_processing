#!/usr/bin/env python3

from integer import Integer
import time
import matplotlib.pyplot as plt

def main():
	f = Integer(8)
	t = []
	print(f.get())
	f.set(40)
	print(f.fib())
	for i in range(30,46):
		start = time.perf_counter()
		f.set(i)
		f.fib()
		end = time.perf_counter()
		t.append(end-start)
	plt.plot([i for i in range(30,46)],t)
	plt.xlabel('fibonacci ith term')
	plt.ylabel('computation time')
	plt.savefig('fib_c.png')


if __name__ == '__main__':
	main()
