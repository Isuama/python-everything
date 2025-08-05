from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import get_servant_service  # import instances

auth_bp = Blueprint("auth", __name__)
servant_service=get_servant_service()

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    servants = servant_service.get_all_active_servants()
    return render_template("register.html", servants=servants)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    servants = servant_service.get_all_active_servants()
    return render_template("login.html", servants=servants)

@auth_bp.route("/logout", methods=["GET", "POST"])
def logout():
    servants = servant_service.get_all_active_servants()
    return render_template("logout.html", servants=servants)