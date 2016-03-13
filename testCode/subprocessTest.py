import subprocess

def main():
	ret =  subprocess.getoutput('date')
	print ret

if __name__ == "__main__":
	main()