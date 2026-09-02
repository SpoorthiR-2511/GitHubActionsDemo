SCENARIOS = {

    "User Login": [
        "valid_login",
        "invalid_username",
        "invalid_password",
        "empty_username",
        "empty_password",
        "empty_username_password"
    ],

    "Search Function": [
        "valid_search",
        "invalid_search",
        "empty_search",
        "special_character_search",
        "partial_search"
    ],

    "Logout Function": [
        "valid_logout",
        "logout_without_login",
        "multiple_logout"
    ],

    "Forgot Password": [
        "registered_email",
        "unregistered_email",
        "invalid_email",
        "empty_email",
        "special_character_email"
    ],

    "Add Item To Cart": [
        "add_single_product",
        "add_multiple_products",
        "duplicate_product",
        "add_after_search",
        "add_without_selection"
    ]
}