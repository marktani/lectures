"""Simple webapp2 server."""

import webapp2
import html_util, rot13, signup

form = """
<form method="post">
	What is your birthday?
	<br>

	<label> Month <input type="text" name="month" value="%(month)s"> </label>
	<label> Day <input type="text" name="day" value="%(day)s"> </label>
	<label> Year <input type="text" name="year" value="%(year)s"> </label>

	<div style="color: red">%(error)s</div>
	<br>
	<br>

	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {
			"error": error,
			"month": html_util.escape_html(month),
			"day": html_util.escape_html(day),
			"year": html_util.escape_html(year)
		})

	def get(self):
		self.write_form()

	def post(self):
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')

		month = html_util.valid_month(user_month)
		day = html_util.valid_day(user_day)
		year = html_util.valid_year(user_year)

		if not (month and day and year):
			self.write_form("That doesn't look valid to me, friend.", user_month, user_day, user_year)
			# self.write_form("%(month)s, %(day)s, %(year)s" % {"month": user_month, "day": user_day, "year": user_year})
		else:
			self.redirect("/thanks")		

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks! That's a totally valid day!")		

application = webapp2.WSGIApplication([
	('/', MainPage),
	('/thanks', ThanksHandler),
	('/unit2/rot13', rot13.Rotation13Handler),
	('/unit2/signup', signup.SignUpHandler),
	('/unit2/welcome', signup.WelcomeHandler)
], debug=True)

