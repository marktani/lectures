import cgi, re

## date validation
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def valid_month(month):
    if month and month in months:
        return month.title()
    return None


def valid_day(day):
        if day and day.isdigit():
            day = int(day)
            if day >= 1 and day <= 31:
                return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year>=1900 and year<=2020:
            return year

def escape_html(s):
	return cgi.escape(s, quote = True)


## rot13 encoding/decoding
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13(plain):
	code = []
	if isinstance(plain, basestring):
		for char in plain:
			if char in lower:
				code.append(lower[(lower.index(char) + 13) % len(lower)])
			elif char in upper:
				code.append(upper[(upper.index(char) + 13) % len(upper)])
			else:
				code.append(char)
		return "".join(code)
	return None


## signup validation

# Username: "^[a-zA-Z0-9_-]{3,20}$" Password: "^.{3,20}$" Email: "^[\S]+@[\S]+\.[\S]+$"
# r will make it being processed as a raw string!
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PW_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_username(username):
	return USER_RE.match(username)

def valid_password(password):
	return PW_RE.match(password)

def valid_email(email):
	return EMAIL_RE.match(email)

if __name__ == '__main__':
	print valid_username("hey")