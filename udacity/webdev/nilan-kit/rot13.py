"""ROT13 webpage"""

import webapp2
import html_util

form = """
<form method="post">
	Enter the text to be encoded using the ROT13 code. Punctuation and white space will be ignored.
	<br>

	<textarea style="height: 100px; width: 400px;" name="text">%(text)s</textarea>
	<br>

	<input type="submit">
</form>
"""

class Rotation13Handler(webapp2.RequestHandler):
	def write_form(self, text=""):
		self.response.out.write(form % {
			"text": html_util.escape_html(text)
		})

	def get(self):
		self.write_form()

	def post(self):
		user_text = self.request.get('text')
		code = html_util.rot13(user_text)
		self.write_form(html_util.escape_html(code))

if __name__ == "main":
	print rot13("halo")