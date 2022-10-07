Feature: Accounts
    Scenario: Creating Account
        Given a non admin account
        Then account has name and false app status

    Scenario: Creating Admin Acount
        Given an admin account
        Then account is admin

    Scenario: Creating Non-Admin Account
        Given a non admin account
        Then account is not admin

    Scenario: Acitivate Thingy
        Given an admin account
        When app is enabled
        Then app status is active