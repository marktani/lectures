"""signup webpage"""

import webapp2
import html_util

form = """
<form method="post">
      <table>
        <tbody><tr>
          <td class="label">
            Username
          </td>
          <td>
            <input name="username" value="%(username)s" type="text">
          </td>
          <td class="error">
          %(usernameInvalid)s  
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input name="password" value="" type="password">
          </td>
          <td class="error">
          %(pwInvalid)s  
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input name="verify" value="" type="password">
          </td>
          <td class="error">
          %(pwMismatch)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input name="email" value="%(email)s" type="text">
          </td>
          <td class="error">
          %(emailInvalid)s   
          </td>
        </tr>
      </tbody></table>

      <input type="submit">
</form>
"""

welcome = """
Welcome, %(username)s!
"""
class SignUpHandler(webapp2.RequestHandler):
	def write_form(self, username="", email="", usernameInvalid="", pwInvalid="", pwMismatch="", emailInvalid=""):
		self.response.out.write(form % {
			"username": html_util.escape_html(username),
			"email": html_util.escape_html(email),
			"usernameInvalid": usernameInvalid,
			"pwInvalid": pwInvalid,
			"pwMismatch": pwMismatch,
			"emailInvalid": emailInvalid
		})

	def get(self):
		self.write_form()

	def post(self):
		redirect = True
		user_username = self.request.get('username')
		user_email = self.request.get('email')
		user_pw = self.request.get('password')
		user_verify = self.request.get('verify')

		username = html_util.escape_html(user_username)
		email = html_util.escape_html(user_email)

		usernameInvalid = ""
		pwInvalid = ""
		pwMismatch = ""
		emailInvalid = ""		
		
		if not (html_util.valid_username(username)):
			usernameInvalid = "That's not a valid username."
			redirect = False
		if (email):
			if not (html_util.valid_email(email)):
				emailInvalid = "That's not a valid email."
				redirect = False
		if not (html_util.valid_password(user_pw)):
			pwInvalid = "That wasn't a valid password."
			redirect = False
		if not (user_pw == user_verify):
			pwMismatch = "Your passwords didn't match."
			redirect = False

		if not (redirect):
			self.write_form(username, email, usernameInvalid, pwInvalid, pwMismatch, emailInvalid)
		else:
			self.redirect("/unit2/welcome?username=" + username)



class WelcomeHandler(webapp2.RequestHandler):
	def write_form(self, username=""):
		self.response.out.write(welcome % {
			"username": html_util.escape_html(username)
		})

	def get(self):
		username = html_util.escape_html(self.request.get('username'))
		if (username == "" or not html_util.valid_username(username)):
			self.redirect('/unit2/signup')
		else:
			self.write_form(username)


if __name__ == "main":
	print rot13("halo")