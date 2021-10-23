#!/usr/bin/env python3

from integer import Integer

def main():
	f = Integer(40)
	print(f.get())
	f.set(10)
	print(f.fib())

if __name__ == '__main__':
	main()