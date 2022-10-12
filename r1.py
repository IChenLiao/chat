#讀取資料
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: #utf-8-sig可以讀中文編碼+首行特殊隱藏符號
		for line in f:
			lines.append(line.strip())
	return lines #回傳到line清單
#轉換資料
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line) #'+'是字串合併時使用
	return new


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines) #覆蓋&取代
	write_file('output.txt', lines)


main()
#沒有印出東西是正確，會產生output檔