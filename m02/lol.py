#!/usr/bin/python 
import socket 
import os,sys

def zigzagzip(s1, s2):
	res = ''
	for i in range(0, len(s1), 2):
		res += s1[i]
		if i + 1 == len(s1):
			return res
		else:
			res += s2[i + 1]
	return res

operation = raw_input("put particular string in: ")

if operation == "abcd": 
	print zigzagzip('abcd', '1234')

if operation == "abc": 
	print zigzagzip('abc', '123') 
