from flask import Blueprint, render_template
from flask_login import current_user

contact = Blueprint("contact", __name__)

@contact.route('/contact', methods=['POST', 'GET'])
def about():
    return render_template("contact.html", user=current_user)