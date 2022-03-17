numeric_words = {
    '.': 'দশমিক',
    '0': '',
    '1': 'এক',
    '01': 'এক',
    '2': 'দুই',
    '02': 'দুই',
    '3': 'তিন',
    '03': 'তিন',
    '4': 'চার',
    '04': 'চার',
    '5': 'পাঁচ',
    '05': 'পাঁচ',
    '6': 'ছয়',
    '06': 'ছয়',
    '7': 'সাত',
    '07': 'সাত',
    '8': 'আট',
    '08': 'আট',
    '9': 'নয়',
    '09': 'নয়',
    '10': 'দশ',
    '11': 'এগারো',
    '12': 'বারো',
    '13': 'তেরো',
    '14': 'চৌদ্দ',
    '15': 'পনেরো',
    '16': 'ষোল',
    '17': 'সতেরো',
    '18': 'আঠারো',
    '19': 'উনিশ',
    '20': 'বিশ',
    '21': 'একুশ',
    '22': 'বাইশ',
    '23': 'তেইশ',
    '24': 'চব্বিশ',
    '25': 'পঁচিশ',
    '26': 'ছাব্বিশ',
    '27': 'সাতাশ',
    '28': 'আঠাশ',
    '29': 'ঊনত্রিশ',
    '30': 'ত্রিশ',
    '31': 'একত্রিশ',
    '32': 'বত্রিশ',
    '33': 'তেত্রিশ',
    '34': 'চৌত্রিশ',
    '35': 'পঁয়ত্রিশ',
    '36': 'ছত্রিশ',
    '37': 'সাঁইত্রিশ',
    '38': 'আটত্রিশ',
    '39': 'ঊনচল্লিশ',
    '40': 'চল্লিশ',
    '41': 'একচল্লিশ',
    '42': 'বিয়াল্লিশ',
    '43': 'তেতাল্লিশ',
    '44': 'চুয়াল্লিশ',
    '45': 'পঁয়তাল্লিশ',
    '46': 'ছেচল্লিশ',
    '47': 'সাতচল্লিশ',
    '48': 'আটচল্লিশ',
    '49': 'ঊনপঞ্চাশ',
    '50': 'পঞ্চাশ',
    '51': 'একান্ন',
    '52': 'বায়ান্ন',
    '53': 'তিপ্পান্ন',
    '54': 'চুয়ান্ন',
    '55': 'পঞ্চান্ন',
    '56': 'ছাপ্পান্ন',
    '57': 'সাতান্ন',
    '58': 'আটান্ন',
    '59': 'ঊনষাট',
    '60': 'ষাট',
    '61': 'একষট্টি',
    '62': 'বাষট্টি',
    '63': 'তেষট্টি',
    '64': 'চৌষট্টি',
    '65': 'পঁয়ষট্টি',
    '66': 'ছেষট্টি',
    '67': 'সাতষট্টি',
    '68': 'আটষট্টি',
    '69': 'ঊনসত্তর',
    '70': 'সত্তর',
    '71': 'একাত্তর',
    '72': 'বাহাত্তর',
    '73': 'তিয়াত্তর',
    '74': 'চুয়াত্তর',
    '75': 'পঁচাত্তর',
    '76': 'ছিয়াত্তর',
    '77': 'সাতাত্তর',
    '78': 'আটাত্তর',
    '79': 'ঊনআশি',
    '80': 'আশি',
    '81': 'একাশি',
    '82': 'বিরাশি',
    '83': 'তিরাশি',
    '84': 'চুরাশি',
    '85': 'পঁচাশি',
    '86': 'ছিয়াশি',
    '87': 'সাতাশি',
    '88': 'আটাশি',
    '89': 'ঊননব্বই',
    '90': 'নব্বই',
    '91': 'একানব্বই',
    '92': 'বিরানব্বই',
    '93': 'তিরানব্বই',
    '94': 'চুরানব্বই',
    '95': 'পঁচানব্বই',
    '96': 'ছিয়ানব্বই',
    '97': 'সাতানব্বই',
    '98': 'আটানব্বই',
    '99': 'নিরানব্বই'
}

def processor(number):
    
    number = str(number)

    number = number.zfill(11)

    num_list = []


    a = number[0]
    if a == '0' or a == '00':
        pass
    else:
        a = (f'{numeric_words[a]} হাজার')
        num_list.append(a)


    b = number[1]
    if b == '0' or b == '00':
        pass
    else:
        b = (f'{numeric_words[b]}শত')
        num_list.append(b)



    c = number[2:4]
    if c == '0' or c == '00':
        pass
    else:
        c = (f'{numeric_words[c]} কোটি')
        num_list.append(c)


    d = number[4:6]
    if d == '0' or d == '00':
        pass
    else:
        d = (f'{numeric_words[d]} লক্ষ')
        num_list.append(d)


    e = number[6:8]
    if e == '0' or e == '00':
        pass
    else:
        e = (f'{numeric_words[e]} হাজার')
        num_list.append(e)


    f = number[8]
    if f == '0' or f == '00':
        pass
    else:
        f = (f'{numeric_words[f]}শত')
        num_list.append(f)


    g = number[9:]
    if g == '0' or g == '00':
        pass
    else:
        g = (f'{numeric_words[g]}')
        num_list.append(g)

    return (' '.join(x for x in num_list))




def func1(number):
    number = '{:.2f}'.format(number)
    number = str(number)
    x = number.split('.')
    a = x[0]
    b = int(x[1])
        
    return f'টাকা {processor(a)} এবং পয়সা {processor(b)} মাত্র'


def func2(number):
    number = '{:.2f}'.format(number)
    number = str(number)
    a = number[2:]

    return f'পয়সা {processor(a)} মাত্র'


def func3(number):
    return f'টাকা {processor(number)} মাত্র'


def func4(number):
	# this function deals with number that are bigger than 1 crore and have no fraction in them
	# function 4 done well

	number = str(number)
	number = number.zfill(12)

	first = number[0:5]
	int_first = int(first)

	second = number[5:]
	int_second = int(second)

	if int_second == 0:
		return f'টাকা {processor(int_first)} কোটি {processor(int_second)}মাত্র'
	else:
		return f'টাকা {processor(int_first)} কোটি {processor(int_second)} মাত্র'


def func5(number):
    # bigger number and have fraction
    number = '{:.2f}'.format(number)
    number = str(number)
    x = number.split('.')
    a = x[0]
    b = x[1]

    a = a.zfill(12)
    first = a[0:5]
    int_first = int(first)

    second = a[5:]
    int_second = int(second)

    if int_second == 0:
        return f'{processor(int_first)} কোটি {processor(int_second)}এবং পয়সা {processor(b)} মাত্র'
    else:
        return f'{processor(int_first)} কোটি {processor(int_second)} এবং পয়সা {processor(b)} মাত্র'



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main(number):
	str_number = str(number)

	if number >= 10000000:
		if '.' in str_number:
			return func5(number)
		else:
			return func4(number)

	else:
		if '.' in str_number:
			if number < 1:
				return func2(number)
			else:
				return func1(number)
		else:
			return func3(number)


print(main(12.35))