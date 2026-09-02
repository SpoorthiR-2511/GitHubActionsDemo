import re

import streamlit as st


class AutomationPortal:
    def __init__(self):
        self.products = [
            "Laptop",
            "TV",
            "Phone",
            "Calculator",
        ]

        self.registered_emails = [
            "admin@gmail.com",
            "user@gmail.com",
        ]

    def validate_login(self, username, password):
        if username.strip() == "":
            return "Username Required"

        if not username.endswith("@gmail.com"):
            return "Username must end with @gmail.com"

        if password.strip() == "":
            return "Password Required"

        if len(password) < 8:
            return "Password must be at least 8 characters"

        if not re.search(r"[A-Z]", password):
            return "Password must contain an uppercase letter"

        if not re.search(r"[a-z]", password):
            return "Password must contain a lowercase letter"

        if not re.search(r"\d", password):
            return "Password must contain a number"

        if not re.search(
            r'[!@#$%^&*(),.?":{}|<>]',
            password,
        ):
            return "Password must contain a special character"

        return "Login Successful"

    def search_product(self, product):
        product = product.strip()

        if product == "":
            return "Enter Product Name"

        if re.search(r"[^a-zA-Z0-9 ]", product):
            return "Invalid Search Input"

        for item in self.products:
            if product.lower() in item.lower():
                return "Products Found"

        return "No Products Found"

    def forgot_password(self, email):
        if email.strip() == "":
            return "Email Required"

        if any(char in "#$%^&*" for char in email):
            return "Invalid Email"

        if "@" not in email or "." not in email:
            return "Invalid Email Format"

        if email not in self.registered_emails:
            return "Email Not Registered"

        return "Password Reset Confirmation Displayed"


class AutomationDemoPortal:
    def __init__(self):
        self.portal = AutomationPortal()

        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False

        if "cart_count" not in st.session_state:
            st.session_state.cart_count = 0

        if "cart_items" not in st.session_state:
            st.session_state.cart_items = []

    def login_section(self):
        st.divider()
        st.subheader("🔐 Login")

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password",
        )

        if st.button("Login"):
            result = self.portal.validate_login(
                username,
                password,
            )

            if result == "Login Successful":
                st.session_state.logged_in = True
                st.success("Home Page Displayed")
            else:
                st.error(result)

    def search_section(self):
        st.divider()
        st.subheader("🔍 Search Product")

        product = st.text_input(
            "Enter Product Name"
        )

        if st.button("Search"):
            result = self.portal.search_product(
                product
            )

            if result == "Products Found":
                st.success(result)
            else:
                st.error(result)

    def forgot_password_section(self):
        st.divider()
        st.subheader("📧 Forgot Password")

        email = st.text_input(
            "Registered Email"
        )

        if st.button("Reset Password"):
            result = self.portal.forgot_password(
                email
            )

            if (
                result
                == "Password Reset Confirmation Displayed"
            ):
                st.success(result)
            else:
                st.error(result)

    def logout_section(self):
        st.divider()
        st.subheader("🚪 Logout")

        if st.button("Logout"):
            if st.session_state.logged_in:
                st.session_state.logged_in = False

                st.success(
                    "User Logged Out Successfully"
                )

                st.info(
                    "Redirected To Login Page"
                )
            else:
                st.error(
                    "User Not Logged In"
                )

    def cart_section(self):
        st.divider()
        st.subheader("🛒 Shopping Cart")

        selected_product = st.radio(
            "Select Product",
            [
                "Select Product",
                "Laptop",
                "TV",
                "Phone",
            ],
        )

        if st.button("Add to Cart"):
            if (
                selected_product
                == "Select Product"
            ):
                st.error(
                    "Please Select Product"
                )
            else:
                st.session_state.cart_items.append(
                    selected_product
                )

                st.session_state.cart_count += 1

                st.success(
                    f"{selected_product} added to cart"
                )

        st.write(
            f"Cart Count: {st.session_state.cart_count}"
        )

        st.write("Items in Cart")

        for item in st.session_state.cart_items:
            st.write(f"• {item}")

    def display_test_cases(self):
        st.divider()
        st.subheader(
            "✅ Generated Test Cases"
        )

        test_cases = [
            "valid_login",
            "empty_username",
            "empty_password",
            "invalid_domain",
            "password_without_uppercase",
            "password_without_lowercase",
            "password_without_number",
            "password_without_special_character",
            "valid_search",
            "invalid_search_input",
            "product_not_found",
            "valid_forgot_password",
            "invalid_email_format",
            "email_not_registered",
            "add_product_to_cart",
            "add_without_selection",
        ]

        for case in test_cases:
            st.write(f"✅ {case}")

    def run(self):
        st.set_page_config(
            page_title="Automation Demo Portal",
            page_icon="🚀",
            layout="wide",
        )

        st.title(
            "🚀 Automation Demo Portal"
        )

        self.login_section()
        self.search_section()
        self.forgot_password_section()
        self.logout_section()
        self.cart_section()
        self.display_test_cases()


if __name__ == "__main__":
    app = AutomationDemoPortal()
    app.run()