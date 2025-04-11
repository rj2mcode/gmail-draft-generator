
def email_body(first_name, last_name):
    return  f"""
<html>
    <body>
        <p>Dear {first_name} {last_name},</p>

        <p>This is your context</p>

        <p><strong>Best regards,</strong><br>
        Your Fullname<br>
        Email: <a href="mailto:yourmail@mail.com">yourmail@mail.com</a><br>
        Mobile: +123456789<br>
        LinkedIn: <a href="https://www.linkedin.com/in/Yourlink">Your linkedin</a><br>
        GitHub: <a href="https://github.com/Yourlink">Your Github</a>
        </p>
    </body>
</html>
"""